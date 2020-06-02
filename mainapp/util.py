def is_decan(request):
    return not request.session.get('tid') and request.user.is_authenticated
