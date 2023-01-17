from django.db import models
from django.conf import settings
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)

    Country = (
        ('AU','Australia'),
        ('CA','Canada'),
        ('IN','India'),
        ('NZ','New Zealand'),
        ('JP','Japan'),
        ('GB','United Kingdom'),
        ('US','United States'),
    )                          
    country =  models.CharField(max_length=20,choices= Country)
    
    Category = (
        ('Technology', 'Technology'),
        ('Business', 'Business'),
        ('Sports', 'Sports'),
    )
    
    news_category = models.CharField(max_length=20,choices= Category)
    
    Category_two = (
        ('Technology', 'Technology'),
        ('Business', 'Business'),
        ('Sports', 'Sports'),
    )
    news_category_two = models.CharField(max_length=20,choices= Category_two, default = 'Technology')

    Category_three = (
        ('Technology', 'Technology'),
        ('Business', 'Business'),
        ('Sports', 'Sports'),
    )
    news_category_three = models.CharField(max_length=20,choices= Category_three, default = 'Technology')


    def __str__(self):
        return f'Profile of {self.user.username}'

# Create your models here.
