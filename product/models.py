from django.db import models
from django.utils.text import slugify
# Create your models here.

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "product/%s.%s"%(instance.slug,extension) 

GENDER_CHOICES = (
    ('Men', 'Men'),
    ('Women', 'Women'),
)
class Proucts(models.Model):
    name= models.CharField(max_length=50,default="")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    price=models.IntegerField(default=0)
    img=models.ImageField( upload_to=image_upload)
    slug = models.SlugField(blank=True ,null=True)
    
    class Meta:
        verbose_name = 'Prouct'
        verbose_name_plural = 'Proucts'
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.name)
        else:
            self.slug= slugify(self.name)
        super(Proucts, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name



# class EmailAddress(models.Model):
#     # Your EmailAddress model fields and methods go here

#     class Meta:
#         app_label = 'allauth.account'