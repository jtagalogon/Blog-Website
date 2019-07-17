from django.shortcuts import render
from .models import User


def index(request):
	user = User.objects.get(user_id = "1")

	context ={
		'user': user
	}
	return render(request, 'users/index.html', context)
# Create your views here.
