
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarket', '0002_auto_20190910_0711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='price',
        ),
    ]