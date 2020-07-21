from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from .models import Profile


def join_group(user):
    group, created = Group.objects.get_or_create(name='general')

    content_type = ContentType.objects.get_for_model(Profile)

   # either create new permission or get a current one,
   # needs modification later

    if created:
        """ permission = Permission.objects.create(
            codename='can_delete_comment',
            name='Can delete comment',
            content_type=content_type,
        ) """
        permission = Permission.objects.get(name='Can delete comment')
        group.permissions.add(permission)
    else:
        print("fix this later")
        """ permission = Permission.objects.get(name='Can delete comment') """

    user.groups.add(group)
    user.save()
