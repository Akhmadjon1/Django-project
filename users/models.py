from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile-pics')

    def __self__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        Old_usr = Profile.objects.get(id=self.id)
        super().save(*args, **kwargs)

        # # resizing larger image for better performance
        New_img = Image.open(self.image.path)

        # deleting old one
        if Old_usr.image != self.image:
            Old_usr.image.delete(save=False)


        if New_img.height > 300 or New_img.width > 300:
            # 300 X 300 pixel
            output_size = (300, 300)

            New_img.thumbnail(output_size)
            New_img.save(self.image.path)
            
