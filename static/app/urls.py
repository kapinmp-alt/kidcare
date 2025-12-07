from django.urls.conf import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.Index, name='index'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('booking/<str:username>', views.booking, name='booking'),
    path('booking/<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
    path('nannies/', views.details, name='welcome'),
    path('search/', views.search_product, name='search'),
    path('home/', views.home, name='home'),
    path('companydetails/', views.company_list, name='company_list'),
    path('companydetails/<slug:slug>/', views.companydetails, name='companydetails'),
    path('companydetails/<int:pk>/', views.companydetails, name='companydetails_pk'),
    path('company/add/', views.company_create, name='company_create'),
    path('company/<int:pk>/edit/', views.company_update, name='company_update'),
    path('company/<int:pk>/delete/', views.company_delete, name='company_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
