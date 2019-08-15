from django.db import models

# Create your models here.


class File(models.Model):
    name=models.CharField(max_length=100)
    file_type=models.CharField(max_length=100)
    create_time=models.DateTimeField()

    def __str__(self):
        return self.name



class Case(models.Model):
    name=models.CharField(max_length=100)
    file=models.ForeignKey(File,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.name




class Data(models.Model):
    name=models.CharField(max_length=100)
    data_type=models.CharField(max_length=100)
    case=models.ForeignKey(Case,on_delete=models.CASCADE,blank=True)

    def __str__(self):
        return self.name
