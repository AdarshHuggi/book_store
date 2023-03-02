from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
# Create your models here.
class Book(models.Model):
    title =models.CharField(max_length=100)
    author=models.CharField(null=True,max_length=50)
    rating =models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    year =models.IntegerField()
    is_bestselling=models.BooleanField(default=False)
    slug= models.SlugField(default="",null=False)# harry-potter-1  format
    

    def save(self,**kwargs):
        self.slug =slugify(self.title)
        super().save(*args, **kwargs)


    def get_absolute_url(self):
        """
        This inbuilt function loads the data object of this class
        """
        return reverse("book-detail", args=[self.id])
    

    def __str__(self):
        return f"{self.title}, {self.rating},{self.year}"
    