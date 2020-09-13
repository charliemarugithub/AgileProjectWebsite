from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    weekly_subs = models.BooleanField(default=False)
    monthly_subs = models.BooleanField(default=False)
    annual_subs = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 250:
            output_size = (300, 250)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Subscription(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    sub_type = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    zip = models.CharField(max_length=10)
    same_address = models.BooleanField()
    save_info = models.BooleanField()
    credit = models.BooleanField()
    debit = models.BooleanField()
    paypal = models.BooleanField()
    cc_name = models.CharField(max_length=100)
    cc_number = models.IntegerField()
    cc_expiration = models.CharField(max_length=10)
    cc_cvv = models.IntegerField()

    def __str__(self):
        return f'{self.firstName} {self.lastName}'