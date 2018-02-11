from django.shortcuts import render
from Users.models import users
# Create your views here.
def index(request):
    return render(request, 'Users/index.html')

def user(request):
    user_list = users.objects.order_by('first_name')
    user_dict = {
        'users': user_list,
    }
    return render(request, 'Users/users.html', context=user_dict)
