from django.db import models


# Create your models here.
class Patient(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default="")
    age = models.IntegerField()

    class Meta:
        db_table = "patient"
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    def __str__(self):
        return self.name
