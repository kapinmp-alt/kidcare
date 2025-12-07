from django.contrib.auth.models import User
from django.db import models

from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.urls import reverse



class Company(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    location = models.CharField(max_length=255)
    image = CloudinaryField('images')
    phone_number = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

    def create_company(self):
        self.save()

    def delete_company(self):
        self.delete()

    @classmethod
    def find_company(cls, search_term):
        companies = cls.objects.filter(name__icontains=search_term)
        return companies

    def update_company(self):
        name = self.name
        self.name = name
        self.save()

    def save(self, *args, **kwargs):
        """Auto-generate a unique slug from the company name if not provided."""
        if not self.slug and self.name:
            base = slugify(self.name)[:240]
            slug_candidate = base
            counter = 1
            while Company.objects.filter(slug=slug_candidate).exclude(pk=self.pk).exists():
                slug_candidate = f"{base}-{counter}"
                counter += 1
            self.slug = slug_candidate
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        if self.slug:
            return reverse('companydetails', args=[self.slug])
        return reverse('companydetails_pk', args=[self.pk])
     # get all images

    @classmethod
    def get_all_images(cls):
        images = Company.objects.all()
        return images


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, blank=True)
    profile_pic = CloudinaryField('profile', blank=True)
    # created = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"{self.created.strftime('%d-%m-%Y')}"
    def __str__(self):
        return f"{self.user.username} profile"


class Nanny(models.Model):
    profile_pic = CloudinaryField('profilepic')
    name = models.CharField(max_length=50, blank=True)
    experience = models.CharField(max_length=50, blank=True)
    rates = models.IntegerField(blank=True)
    availability = models.BooleanField(max_length=50, blank=True)
    age = models.IntegerField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    about = models.TextField(default="Some String")
    skills = models.TextField(default="Some String")
    company = models.ForeignKey(Company,on_delete=models.CASCADE, default=1 )
    

    def save_profile(self):
        self.save()

    def __str__(self):
        return self.name

    def get_image_by_id(cls):
        # incorrect signature previously; provide proper classmethod to fetch by id
        raise NotImplementedError('Use Company.objects.get(pk=...) or implement a classmethod with id parameter')


class Bio(models.Model):
    about = models.TextField()
    skills = models.TextField()


class Booking(models.Model):
    """Model to store booking details for nanny services"""
    BOOKING_TYPES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    nanny = models.ForeignKey(Nanny, on_delete=models.CASCADE, related_name='bookings')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='bookings')
    booking_type = models.CharField(max_length=10, choices=BOOKING_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.nanny.name} ({self.booking_type})"
    
    class Meta:
        ordering = ['-created_at']

