from django.shortcuts import render, redirect
from .models import Post, Comment, Profile
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm, CommentForm, PostForm
from django.contrib.auth.models import User
from django.utils.text import slugify

def index(request):
	posts = Post.objects.order_by('-created_on')
	return render(request, 'index.html', {'posts': posts})

def detail(request, slug):
    post = Post.objects.get(slug=slug)
    user_comments = post.comments.all()
    form = CommentForm()
    new_comment = None
    if request.method == 'POST':
    	form = CommentForm(request.POST)
    	if form.is_valid():
    		content = request.POST.get('content')
    		new_comment = Comment.objects.create(post=post, author=request.user, content=content)
    		new_comment.save()
    		form = CommentForm()
    	else:
    		form = CommentForm()
    context = {'post': post, 'user_comments': user_comments, 'form': form}
    return render(request, 'detail.html', context)

def register(request):
	form = UserCreationForm()
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			form = UserCreationForm()
	return render(request, 'register.html', {'form': form})

def profile(request):
	return render(request, 'profile.html')

def edit_profile(request):
	form = ProfileForm(instance=request.user.profile)
	if request.method == 'POST':
		form = ProfileForm(request.POST,request.FILES, instance=request.user.profile)
		if form.is_valid():
			print('Form Saved')
			form.save()
			return redirect('profile')
		else:
			form = ProfileForm(instance=request.user.profile)
	return render(request, 'edit_profile.html', {'form': form})

def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'user_profile.html', {"user":user})

def create_post(request):
	form = PostForm()
	new_post = None
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			content = request.POST.get('content')
			title = request.POST.get('title')
			slug = slugify(title)
			new_post = Post.objects.create(author=request.user, content=content, title=title, slug=slug)
			new_post.save()
			return redirect('home')
		else:
			form = PostForm()
	return render(request, 'create_post.html', {'form': form})

def edit_post(request, post_id):
	post = Post.objects.get(pk=post_id)
	form = PostForm(instance=post)
	if request.method == 'POST':
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			form = PostForm(instance=post)
	return render(request, 'edit_post.html', {'form': form})

def delete_post(request, post_id=None):
	post = Post.objects.filter(pk=post_id)
	post.delete()
	return redirect('home')
