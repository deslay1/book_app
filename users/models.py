from django.db import models
from django.contrib.auth.models import User, Permission
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import filesizeformat
from PIL import Image


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


# A validion on save where we set a max height and width of the uploaded profile picture.
# We also crop out a max square out of the uploaded image for consistent dimensions.

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # self.image is the same as self.image.name locally
        # self.image.path is the full absolute path
        # Postgres backend (this app's production database)
        # does not support absolute paths.
        # Use self.image, which points to the media files in prod.
        if settings.IMAGE_TESTING == False:
            if settings.USE_POSTGRES == False:
                img = Image.open(self.image.path)
            else:
                img = Image.open(self.image)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)

            thumb_width = 300
            img = self.crop_max_square(img).resize(
                (thumb_width, thumb_width), Image.LANCZOS)

            if settings.USE_POSTGRES == False:
                img.save(self.image.path)
            else:
                img.save(self.image)

    def crop_max_square(self, image):
        return self.crop_center(image, min(image.size), min(image.size))

    def crop_center(self, image, crop_width, crop_height):
        img_width, img_height = image.size
        return image.crop(((img_width - crop_width) // 2,
                           (img_height - crop_height) // 2,
                           (img_width + crop_width) // 2,
                           (img_height + crop_height) // 2))
