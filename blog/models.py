from django.db import models

# Create your models here.
class Post(models.Model):
    #create columns / field
    title = models.CharField(max_length=100)
    content = models.TextField()
    img_url = models.URLField(null=True) #defaultlength 200
    #nullable data for missing data = blank=true = attributes

    created_at = models.DateTimeField(auto_now_add=True)

    #function for printing model data (not necessary)
    def __str__(self) :
        return self.title
    
    