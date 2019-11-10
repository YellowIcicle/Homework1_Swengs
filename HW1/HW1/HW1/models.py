from django.db import models

# Create your models here.


class Country(models.Model):

    name = models.TextField()

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'

    def __str__(self): return self.name


class Producer(models.Model):

    name = models.TextField()
    founded = models.DateField()
    headquaters = models.ForeignKey(Country,on_delete=models.CASCADE)
    founder = models.TextField()

    def __str__(self): return self.name + '' + self.founded.__str__() + '' + self.headquaters.name + '' + self.founder

class Smartphone(models.Model):
    CHOICES = (
        ('I' , 'iOS'),
        ('A' , 'Android')
    )

    name = models.TextField()
    OS = models.CharField(max_length=1,choices=CHOICES)
    release_date = models.DateField()
    description = models.TextField()
    price = models.PositiveIntegerField(help_text="in Euros")
    producer = models.ForeignKey(Producer,on_delete=models.CASCADE)

    def __str__(self): return self.name

