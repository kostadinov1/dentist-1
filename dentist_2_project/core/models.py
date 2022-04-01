from django.contrib.auth import get_user_model
from django.db import models

from dentist_2_project.services.models import Service

UserModel = get_user_model()


class Appointment(models.Model):
    VENUES = (('Balchik', 'Balchik'), ('Kavarna', 'Kavarna'), ('Varna', 'Varna'),)

    venue = models.CharField(max_length=20, choices=VENUES)
    time = models.TimeField()
    date = models.DateField()
    message = models.TextField()
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.DO_NOTHING)




class Review(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
