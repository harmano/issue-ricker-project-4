from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm
from django.utils import timezone
from .models import Post, Feat
from .forms import BlogPostForm, BlogFeatForm
from django.http import HttpResponseRedirect

def index(request):
    """Return the login and regestiration form page"""
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('home'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    
    return render(request,  'index.html', {'login_form': login_form})

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))


def login(request):
    """Return a login page"""
    if request.user.is_authenticated:
        return redirect(reverse('home'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'index.html', {'login_form': login_form})


def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('home'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered, welcome to the Home Page!")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'registration.html', {
        "registration_form": registration_form})

@login_required
def user_profile(request):
    """The user's profile page"""
    user = User.objects.get(email=request.user.email)
    return render(request, "profile.html", {"profile": user})




@login_required   
def home(request):
    """Returns home page"""
    return render(request, 'home.html')

@login_required    
def cart2(request):
    """Returns cart page"""
    return render(request, 'cart2.html')
    
@login_required    
def get_posts(request):
    """
    Return Home Page
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-views')
    return render(request, "home.html", {'posts': posts})

@login_required    
def post_detail(request, pk):
    """
    Return Posts Page
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
    }
    return render(request, "postdetail.html", context)

@login_required    
def like_post(request):
    """
    Show Like Amount
    """
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(post.get_absolute_url())
    
@login_required    
def create_or_edit_post(request, pk=None):
    """
    Create a Post
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'postform.html', {'form': form})
    

@login_required    
def community(request):
    """Returns community page"""
    return render(request, 'community.html')



@login_required    
def get_feats(request):
    """
    Create A Feature
    """
    feats = Feat.objects.filter(published_date__lte=timezone.now()
        ).order_by('-views')
    return render(request, "feat.html", {'feats': feats})

@login_required    
def feat_detail(request, pk):
    """
    Feature Detail
    """
    feat = get_object_or_404(Feat, pk=pk)
    feat.views += 1
    feat.save()
    return render(request, "featdetail.html", {'feat': feat})

@login_required    
def create_or_edit_feat(request, pk=None):
    """
    View Page
    """
    feat = get_object_or_404(Feat, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogFeatForm(request.POST, request.FILES, instance=feat)
        if form.is_valid():
            feat = form.save()
            return redirect(feat_detail, feat.pk)
    else:
        form = BlogFeatForm(instance=feat)
    return render(request, 'featform.html', {'form': form})


@login_required    
def get_completed(request):
    """
    Return Completed Page
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-views')
    return render(request, "completed.html", {'posts': posts})


"""
@login_required    
  def get_posts(request, pk):
 
    posts = Post.objects.filter(published_date__lte=timezone.now()
        ).order_by('-views')
        
    post = get_object_or_404(Post, pk=pk) if pk else None
    post.views += 1
    post.save()
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True
    context = {
        'posts':'posts',
        'post': post,
        'is_liked': is_liked,
        'total_likes': post.total_likes(),
    }
    
    return render(request, "home.html", context) 
"""