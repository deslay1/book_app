from django import template
from bookmarket.models import Comment, Reply

register = template.Library()


@register.filter(name='check_user_reply')
def check_user_reply(value, arg):
    print(value.replies.all())
    comment_replies = Reply.objects.filter(comment=value)
    user_replies = Reply.objects.filter(user=arg)
    list_cr = list(comment_replies)
    list_ur = list(user_replies)
    return not bool(set(list_cr) & set(list_ur))
