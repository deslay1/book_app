from django.db import models
from django.contrib.auth.models import User, Permission
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import filesizeformat


class Profile(models.Model):
    def validate_image(file):
        if file.size > settings.MAX_UPLOAD_SIZE:
            raise ValidationError(_('Filesize can be maximum %s. The file you uploaded was %s') % (
                filesizeformat(settings.MAX_UPLOAD_SIZE), filesizeformat(file.size)))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics',
                              default='default.jpg', validators=[validate_image])
    # permissions = models.CharField(blank=True,
    #                               choices=getBasicUserPermissions(), verbose_name="What kind of notifications would you like to choose?")

    def __str__(self):
        return f'{self.user.username}'


# Another validion where we look at the height and width of the uploaded profile picture
"""     def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path) """
