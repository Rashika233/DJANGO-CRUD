from django.db import models

# Create your models here.
class StudentModel(models.Model):
    id = models.IntegerField(primary_key = True)
    name = models.CharField(max_length = 20)
    subject = models.CharField(max_length = 20)
    rollnumber = models.IntegerField()

    def __str__(self):
        return self.name