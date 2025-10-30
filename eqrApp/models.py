from django.db import models
from django.utils import timezone
from django_cryptography.fields import encrypt
from PIL import Image

class Employee(models.Model):
    employee_code = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=250)
    middle_name = models.CharField(max_length=250, null=True, blank=True)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(
        max_length=50,
        choices=(("Male", "Male"), ("Female", "Female")),
        default="Male"
    )
    dob = models.DateField()
    contact = encrypt(models.CharField(max_length=100))  # encrypted
    email = encrypt(models.EmailField(max_length=250, blank=True))  # encrypted
    address = models.TextField(null=True, blank=True)
    department = models.CharField(max_length=250, null=True, blank=True)
    position = models.CharField(max_length=250, null=True, blank=True)
    avatar = models.ImageField(upload_to="employee-avatars/", null=True, blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        full_name = f"{self.first_name} "
        if self.middle_name:
            full_name += f"{self.middle_name} "
        full_name += self.last_name
        return f"{self.employee_code} - {full_name.strip()}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.avatar:
            imag = Image.open(self.avatar.path)
            if imag.width > 200 or imag.height > 200:
                output_size = (200, 200)
                imag.thumbnail(output_size)
                imag.save(self.avatar.path)
