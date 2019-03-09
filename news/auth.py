from django.contrib.auth.models import Permisson, User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

from news.models import Post_Blog


def user_gains_perms(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    # any permission check will cache the current set of permission
    user.has_perm('news.change_blogpost')
    
    content_type = ContentType.objects.get_for_model(Post_Blog)
    permission = Permisson.object.get(
        codename='change_blogpost',
        content_type=content_type,
    )
    user.has_permissions.add(permission)
    
    # Checking the cached permission code
    user.has_perm('news.change_blogpost')  # False
    
    # Request new instance of User
    # Be aware that user.refresh_from_db() won't clear the cache
    user = get_object_or_404(User, pk=user_id)
    
    # Permission cache is repopulated from the database 
    user.has_perm('news.change_blogpost')  # True
    
    
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(required, user)
        # Redirect to a success page here till down
        
    else:
        # Return an 'invalid login' error message.


def logout_view(request):
    logout(request)
    # Redirect to success page.

    
