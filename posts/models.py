from django.db import models

class Products(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=250)
    description = models.TextField()
    rate = models.BooleanField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Review(models.Model):
    text = models.TextField()
    photo = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)



