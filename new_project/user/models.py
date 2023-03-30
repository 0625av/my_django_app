from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "ADMIN", 'Admin'
        PATIENT = 'PATIENT', 'Patient'
        DOCTOR = "DOCTOR", 'Doctor'

    base_role = Role.ADMIN

    profile_picture = models.ImageField(upload_to='profile_pictures', height_field=None, width_field=None, max_length=None, blank=True)
    address_line1 = models.CharField(max_length=100, default="Example Street")
    city = models.CharField(max_length=50, default="Kolkata")
    state = models.CharField(max_length=50, default="West Bengal")
    pincode = models.CharField(max_length=10, default="700089")

    role = models.CharField(max_length=50, choices=Role.choices)
    def create_address(self):
        self.address_line1 = input("Enter address: ")
        self.city = input("Enter city: ")
        self.state = input("Enter state: ")
        self.pincode = input("Enter pincode: ")

    def save(self, *args, **kwargs):
        if not self.pk:
            self.create_address()
            self.role = self.base_role
            return super().save(*args, **kwargs)

class Patient(User):
    base_role = User.Role.PATIENT

    class Meta:
        proxy = True

    def welcome(self):
        return "Only for students"
