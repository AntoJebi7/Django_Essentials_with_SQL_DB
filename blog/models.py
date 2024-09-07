from django.db import models
from django.utils.text import slugify

# used to take control of database schemas
# create tables in database with models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    #many to many relationship with post


    def __str__(self) :
        return self.name


class Post(models.Model):
    #create columns / field
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True) #defaultlength 200
    #nullable data for missing data = blank=true = attributes

    created_at = models.DateTimeField(auto_now_add=True)
    #unique url
    slug = models.SlugField(unique=True, max_length=255)

    # many to one relationship with post
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    #function for printing model data (not necessary)
    def __str__(self) :
        return self.title
    
    

#category model

