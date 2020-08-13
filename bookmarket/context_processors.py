def messages(request):
    if request.user.is_authenticated:
        received_messages = request.user.received_messages.all()
        """ for m in received_messages:
            print(m)
            print(m.child_messages.all().filter(
                read_at__isnull=True, sender_deleted_at__isnull=True).count()) """
        unread_messages = received_messages.filter(
            read_at__isnull=True, sender_deleted_at__isnull=True
        )
        read_messages = received_messages.filter(
            read_at__isnull=False, sender_deleted_at__isnull=True
        )
        sent_messages = request.user.sent_messages.all()
        return {
            "received_messages": received_messages,
            "read_messages": read_messages,
            "unread_messages": unread_messages,
            "sent_messages": sent_messages,
        }
    else:
        return {}
