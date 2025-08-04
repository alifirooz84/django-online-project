from django.db import models

class PhoneNumber(models.Model):
    number = models.CharField(max_length=20)

    def __str__(self):
        return self.number

