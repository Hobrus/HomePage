from django.db import models


# Create your models here.
class Good(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
