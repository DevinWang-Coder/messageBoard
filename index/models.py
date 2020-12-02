from django.db import models

# Create your models here.
class Message(models.Model):
    id = models.AutoField('mber', primary_key=True)
    name = models.CharField('name', max_length=50)
    content = models.CharField('content', max_length=200)
    timestamp = models.DateField('time', auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'information table'
        verbose_name_plural = 'information table'
        
        