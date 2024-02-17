from django.db import models
from django.contrib.auth.models import User

class TODO(models.Model):
    status_choices = [
        ('C', 'COMPLETED'),
        ('P', 'PENDING'),
    ]
    priority_choices = [
        ('🟥High', 'High'),
        ('🟧Medium', 'Medium'),
        ('🟩Low', 'Low'),
        
    ]
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, default="")
    status = models.CharField(max_length=2, choices=status_choices)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()  # Field for selecting date
    priority = models.CharField(max_length=7, choices=priority_choices)
    time = models.TimeField(default='00:00')  # Manually define default time as '00:00'
