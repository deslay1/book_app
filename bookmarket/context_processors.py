from django.utils.timezone import now, timedelta
from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.template.loader import get_template, render_to_string
from django.contrib.auth.models import Permission


def messages(request):
    if request.user.is_authenticated:
        received_messages = request.user.received_messages.all().filter(
            recipient_deleted_at__isnull=True
        )
        unread_messages = received_messages.filter(read_at__isnull=True)
        read_messages = received_messages.filter(read_at__isnull=False)
        sent_messages = request.user.sent_messages.all().filter(
            sender_deleted_at__isnull=True
        )

        seconds = now() - timedelta(hours=1)
        for rm in sent_messages.filter(parent__isnull=True, sent_at__gte=seconds):
            recipient_has_permission = Permission.objects.filter(
                user=rm.recipient, codename="email_on_message_receive"
            ).exists()

            if recipient_has_permission:
                if rm.email == "":
                    rm.email = "Sent"
                    rm.save()
                    from_email = settings.EMAIL_HOST_USER
                    recipient_list = [rm.recipient.email]
                    url = "https://bookmarket-app.herokuapp.com/messages/inbox/"

                    subject = f"Message received: '{rm.subject}'"
                    html_message = render_to_string(
                        "email_templates/receive_message.html",
                        {"message": rm, "url": url},
                    )
                    plain_message = strip_tags(html_message)
                    send_mail(
                        subject,
                        plain_message,
                        from_email,
                        recipient_list,
                        fail_silently=False,
                        html_message=html_message,
                    )

        return {
            "received_messages": received_messages,
            "read_messages": read_messages,
            "unread_messages": unread_messages,
            "sent_messages": sent_messages,
        }
    else:
        return {}
