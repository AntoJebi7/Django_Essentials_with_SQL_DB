from django.db import models
from django.core.exceptions import ValidationError
import re

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
    ]

    username = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    year = models.CharField(max_length=10, choices=YEAR_CHOICES)
    age = models.PositiveIntegerField()
    password = models.CharField(max_length=128)  # Store plain text passwords
    pin = models.CharField(max_length=6)  # Adjusted for general cases
    department = models.CharField(max_length=20, choices=DEPARTMENT_CHOICES)

    def __str__(self):
        return self.username

    def clean(self):
        super().clean()

        # Validate age
        if self.age <= 0 or self.age > 100:
            raise ValidationError('Age must be between 1 and 100')

        # Validate pin code (exactly 6 digits)
        if not re.match(r'^\d{6}$', self.pin):
            raise ValidationError('Pin must be a 6-digit number')

    class Meta:
        ordering = ['username']
        verbose_name = 'Registration'
        verbose_name_plural = 'Registrations'
        unique_together = ('roll_no', 'year')  # Optional: Unique roll_no-year combination
