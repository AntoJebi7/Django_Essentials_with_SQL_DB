from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password, check_password

class Registration(models.Model):
    YEAR_CHOICES = [
        ('1st', '1st Year'),
        ('2nd', '2nd Year'),
        ('3rd', '3rd Year'),
        ('4th', '4th Year'),
    ]
    
    DEPARTMENT_CHOICES = [
        ('cs', 'Computer Science'),
        ('ee', 'Electrical Engineering'),
        ('me', 'Mechanical Engineering'),
        ('ce', 'Civil Engineering'),
        ('bt', 'Biotechnology'),
        ('che', 'Chemical Engineering'),
        # Add more departments as needed
    ]

    username = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    year = models.CharField(max_length=10, choices=YEAR_CHOICES)
    age = models.PositiveIntegerField()
    password = models.CharField(max_length=128)  # Increased length for hashed passwords
    pincode = models.CharField(max_length=6)  # Adjusted for general cases

    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return self.username

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def clean(self):
        super().clean()
        if self.age <= 0:
            raise ValidationError('Age must be a positive number')
        # Add any other validations as needed

    class Meta:
        ordering = ['username']
        verbose_name = 'Registration'
        verbose_name_plural = 'Registrations'
