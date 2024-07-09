from django.db import models
from django.utils import timezone

# Create your models here.

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50) 
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True) #exibir ou não um contato
    picture = models.ImageField(default=True, upload_to='pictures/%Y/%m') #upload_to cria uma pasta dentro da pasta media, que cria a pasta do ano e dentro cria uma pasta com o mêspip 


    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'