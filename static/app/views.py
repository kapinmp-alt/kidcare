from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string

from django.contrib.auth.models import User
from .models import Nanny, Bio, UserProfile, Company, Booking
from .forms import UpdateProfileForm, UpdateUserForm
from .forms import CompanyForm

# Create your views here.


def Index(request):
    """Landing page - accessible to everyone (no login required)."""
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def home(request):
    companies=Company.objects.all()
    # Fetch user's recent bookings
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')[:5]
    # Count bookings by status
    total_bookings = Booking.objects.filter(user=request.user).count()
    pending_bookings = Booking.objects.filter(user=request.user, status='pending').count()
    confirmed_bookings = Booking.objects.filter(user=request.user, status='confirmed').count()
    
    context={
        "companies":companies,
        "bookings": bookings,
        "total_bookings": total_bookings,
        "pending_bookings": pending_bookings,
        "confirmed_bookings": confirmed_bookings,
        }
    
    return render(request, 'home.html', context)


@login_required(login_url='/accounts/login/')
def profile(request, username):
    user = get_object_or_404(User, username=username)
    
    # Fetch user's bookings
    bookings = Booking.objects.filter(user=user)

    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        # ensure the user has a profile instance
        profile_instance, _ = UserProfile.objects.get_or_create(user=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=profile_instance)
        if profile_form.is_valid() and user_form.is_valid():
            profile_form.save()
            user_form.save()
            return redirect('profile', username=request.user.username)

    else:
        profile_instance, _ = UserProfile.objects.get_or_create(user=user)
        profile_form = UpdateProfileForm(instance=profile_instance)
        user_form = UpdateUserForm(instance=user)

    context = {
        'user': user,
        'form': profile_form,
        'user_form': user_form,
        'bookings': bookings,
    }
    return render(request, 'profile/profile.html', context)


@login_required(login_url='/accounts/login/')
def booking(request, username):
    """Handle booking page - gracefully handle missing nanny and save bookings"""
    try:
        selected_nanny = Nanny.objects.get(name=username)
    except Nanny.DoesNotExist:
        # If nanny not found, redirect to companies list
        return redirect('company_list')
    
    if request.method == 'POST':
        # Get form data
        booking_type = request.POST.get('booking_type')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        
        # Validate data
        if not booking_type or not start_date or not end_date:
            messages.error(request, 'Please fill in all required fields.')
            params = {'nanny': selected_nanny}
            return render(request, 'book/booking.html', params)
        
        try:
            # Create booking
            booking_obj = Booking.objects.create(
                user=request.user,
                nanny=selected_nanny,
                company=selected_nanny.company,
                booking_type=booking_type,
                start_date=start_date,
                end_date=end_date,
                status='pending'
            )
            messages.success(
                request, 
                f'Booking confirmed for {selected_nanny.name}! Your booking is pending approval.'
            )
            return redirect('profile', username=request.user.username)
        except Exception as e:
            messages.error(request, f'Error creating booking: {str(e)}')
            params = {'nanny': selected_nanny}
            return render(request, 'book/booking.html', params)
    
    # GET request - show booking form
    params = {'nanny': selected_nanny}
    return render(request, 'book/booking.html', params)


@login_required(login_url='/accounts/login/')
def details(request):
    """Show nannies details - login required"""
    nanny = Nanny.objects.all()
    return render(request, 'nannydetails/nannydetails.html', {'nanny': nanny})


@login_required(login_url='/accounts/login/')
def search_product(request):
    """ search function  """
    if request.method == "POST":
        query_name = request.POST.get('name', None)
        if query_name:
            results = Nanny.objects.filter(name__contains=query_name)
            return render(request, 'nannydetails/nannydetails.html', {"results": results})

    return render(request, 'nannydetails/nannydetails.html')


@login_required(login_url='/accounts/login/')
def companydetails(request, slug=None, pk=None):
    """Resolve company either by slug or pk and render detail view.

    The URL patterns pass either `slug` or `pk` depending on which route was used.
    """
    company = None
    if slug:
        company = get_object_or_404(Company, slug=slug)
    elif pk:
        company = get_object_or_404(Company, pk=pk)
    else:
        # no identifier — return 404
        return HttpResponse(status=404)

    nannies = Nanny.objects.filter(company=company)

    context = {
        "nannies": nannies,
        'company': company
    }

    return render(request, 'companydetails/company_detail.html', context)


@login_required(login_url='/accounts/login/')
def company_list(request):
    """Show a list of companies (login required)."""
    companies = Company.objects.all()
    context = {
        'companies': companies,
    }
    return render(request, 'companydetails/company_list.html', context)


@login_required(login_url='/accounts/login/')
def company_create(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company = form.save()
            if is_ajax:
                return JsonResponse({'success': True, 'redirect': company.get_absolute_url()})
            return redirect('companydetails', slug=company.slug)
        else:
            if is_ajax:
                html = render_to_string('companydetails/company_form_fragment.html', {'form': form, 'action': 'Create'}, request=request)
                return JsonResponse({'success': False, 'html': html})
    else:
        form = CompanyForm()

    if is_ajax:
        html = render_to_string('companydetails/company_form_fragment.html', {'form': form, 'action': 'Create'}, request=request)
        return JsonResponse({'success': True, 'html': html})

    return render(request, 'companydetails/company_form.html', {'form': form, 'action': 'Create'})


@login_required(login_url='/accounts/login/')
def company_update(request, pk):
    company = get_object_or_404(Company, pk=pk)
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES, instance=company)
        if form.is_valid():
            company = form.save()
            if is_ajax:
                return JsonResponse({'success': True, 'redirect': company.get_absolute_url()})
            return redirect('companydetails', slug=company.slug)
        else:
            if is_ajax:
                html = render_to_string('companydetails/company_form_fragment.html', {'form': form, 'action': 'Edit', 'company': company}, request=request)
                return JsonResponse({'success': False, 'html': html})
    else:
        form = CompanyForm(instance=company)

    if is_ajax:
        html = render_to_string('companydetails/company_form_fragment.html', {'form': form, 'action': 'Edit', 'company': company}, request=request)
        return JsonResponse({'success': True, 'html': html})



    return render(request, 'companydetails/company_form.html', {'form': form, 'action': 'Edit', 'company': company})


@login_required(login_url='/accounts/login/')
def company_delete(request, pk):
    company = get_object_or_404(Company, pk=pk)
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if request.method == 'POST':
        company.delete()
        if is_ajax:
            return JsonResponse({'success': True})
        return redirect('company_list')
    if is_ajax:
        html = render_to_string('companydetails/company_confirm_delete_fragment.html', {'company': company}, request=request)
        return JsonResponse({'success': True, 'html': html})
    return render(request, 'companydetails/company_confirm_delete.html', {'company': company})


@login_required(login_url='/accounts/login/')
def cancel_booking(request, booking_id):
    """Cancel a booking"""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    
    if request.method == 'POST':
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, f'Booking for {booking.nanny.name} has been cancelled.')
        return redirect('profile', username=request.user.username)
    
    # If accessed via GET, show confirmation
    return render(request, 'booking_confirm_cancel.html', {'booking': booking})
