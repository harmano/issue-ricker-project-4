from django.shortcuts import render
from accounts.models import Post

def do_search(request):
    post = Post.objects.filter(title__icontains=request.GET['q'])
    return render(request, "home.html", {"post": post})
    
