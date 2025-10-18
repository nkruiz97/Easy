from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    

class Type(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Element(models.Model):
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=255, null=True, blank=True)
    
    description = models.TextField()
    content = models.TextField(null=True, blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    image = models.ImageField(upload_to='elements/', blank=True, null=True)

    def __str__(self):
        return self.title
