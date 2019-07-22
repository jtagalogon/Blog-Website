from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NewPost
from datetime import datetime
from .models import Post, Blog

# Create your views here.


def base(request):
    #User.objects.all().delete()
    return render(request, 'blog/base.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if User.objects.get(username=username) is not None:
            return HttpResponse("this username already exists.", content_type='text/plain')
        else:
            password = request.POST.get('password') 
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            email = request.POST.get('email')
            if validate_email(email):
                user = User(username=username, password=password,
                firstname=firstname, lastname=lastname, email=email)

                user.save()
                return render(request, 'blog/base.html')
            else:
                return HttpResponse("wrong email!", content_type='text/plain')                  
    else:
        return render(request, 'blog/signup.html')

def login(request):
    if request.method == 'POST':
        loginname = request.POST.get('loginname')
        #print(loginname)       
        loginpassword = request.POST.get('loginpassword')
        #print(loginpassword)
        try:
            tempname = User.objects.get(username=loginname)
            print(tempname)
            if tempname.password == loginpassword:
                context= {'loginname':loginname}
                return render(request, 'blog/home.html', context)
            else:
                return HttpResponse("wrong password!", content_type='text/plain')
        except User.DoesNotExist:
            return HttpResponse("User not exist.", content_type='text/plain')     
    
    else:
        return render(request, 'blog/login.html')

def home(request):
    return render(request, 'blog/home.html')

def delete(request):
    if request.method == 'POST':
        name = request.POST.get('loginname')
        #print(loginname)       
        password = request.POST.get('loginpassword')
        #print(loginpassword)
        try:
            tempname = User.objects.get(username=name)
            print(tempname)
            if tempname.password == password:
                User.objects.get(username=name).delete()
                return render(request, 'blog/base.html')
            else:
                return HttpResponse("wrong password!", content_type='text/plain')
        except User.DoesNotExist:
            return HttpResponse("User not exist.", content_type='text/plain')     
    
    else:
        return render(request, 'blog/delete.html')


def post_page(request):
    if request.method == 'POST':
        form = NewPost(request.POST)
        if form.is_valid():
            title = form.cleaned_data['new_title']
            body = form.cleaned_data['new_body']
            new_post = Post(postTitle=title, text=body, created_on=datetime.now())
            new_post.save()
            return HttpResponseRedirect('/blogs/')
    else:
        form = NewPost()
    return render(request, 'blog/post_page.html', {'form': form})
    # return render(request, 'posts/post_page.html')

def blog_page(request):
	posts = Post.objects.all().order_by('created_on') # grabs all records from the posts database table.
	return render(request, 'blog/blog_page.html', {'posts':posts})

# This posts all the posts in order by date created on the blog page.