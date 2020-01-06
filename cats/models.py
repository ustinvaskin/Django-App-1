from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'

class Owner(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return f'{self.name} - {self.age}'

class Cat(models.Model):
    name = models.CharField(max_length=50, unique=True)
    breed = models.CharField(max_length=50)
    image = models.CharField(max_length=500)
    owner = models.ForeignKey(Owner, related_name='cats', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='cats')

    def __str__(self):
        return f'{self.name} - {self.breed}'