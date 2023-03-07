from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.text import slugify
# Create your models here.


class Country(models.Model):
    name =models.CharField(max_length=50)
    code =models.CharField( max_length=2)

    def __str__(self):
        return f"{self.name} {self.code}"

    class Meta:
        #this class is used to add the correct spell of the plurals in admin panel
        # it shows instead Countrys table to Country Entries in admin panel but Country will be there in database
        verbose_name_plural = "Countries"

 

class Address(models.Model):
    street =models.CharField(max_length=200)
    postal_code =models.CharField(max_length=50)
    city =models.CharField( max_length=50)

    def full_address(self):
        return f"{self.street}, {self.city}, {self.postal_code}"

    # adding this str method to show the data instead of objects in admin dashboard
    def __str__(self):
        return self.full_address()

    class Meta:
        #this class is used to add the correct spell of the plurals in admin panel
        # it shows instead Addresss table to Address Entries in admin panel but it will Address will be there in database
        verbose_name_plural = "Address Entries"
    
class Author(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField( max_length=50)
    #creating one to one relationship between tables 
    address =models.OneToOneField(Address, on_delete=models.CASCADE,editable =True, null=True, db_index=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # adding this str method to show the data instead of objects in admin dashboard
    def __str__(self):
        return self.full_name()
    
    



class Book(models.Model):
    title =models.CharField(max_length=100)
    #adding the foreignkey for field
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True,related_name="books")
    rating =models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    year =models.IntegerField()
    is_bestselling=models.BooleanField(default=False)
    slug= models.SlugField(default="",blank =True,editable =True, null=False, db_index=True)# harry-potter-1  format
    published_countries =models.ManyToManyField(Country,null=False)    




    def get_absolute_url(self):
        """
        This inbuilt function loads the data object of this class
        """
        return reverse("book-detail", args=[self.id])
    
     # adding this str method to show the data instead of objects in admin dashboard
    def __str__(self):
        return f"{self.title}, {self.rating},{self.year},{self.slug}"
    