from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100, verbose_name='email address', unique=True)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    dob = models.DateField(verbose_name='date of birth', null=True)
    batch = models.SmallIntegerField(null=True)
    department = models.CharField(max_length=100, null=True)
    group = models.CharField(max_length=50, null=True)
    semester = models.SmallIntegerField(null=True)
    phone_no = models.CharField(max_length=15, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}' 


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()