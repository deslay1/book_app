

def check_session_item(request, session_item, session_name):
    if session_item is None:
        if session_name in request.session:
            session_item = request.session[session_name]
        else:
            request.session[session_name] = session_item
    else:
        request.session[session_name] = session_item

    return session_item
