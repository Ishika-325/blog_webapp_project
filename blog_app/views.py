from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'blogapp/home.html')

def dashboard(request):
    return render(request, 'blogapp/dashboard.html')

def blog_detail(request):
    return render(request, 'blogapp/blog_detail.html')

def blog_list(request):
    return render(request, 'blogapp/blog_list.html')

def comments(request):
    return render(request, 'blogapp/comments.html')

def add_blogs(request):
    return render(request, 'blogapp/add_blogs.html')
