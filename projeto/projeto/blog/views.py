#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.utils import timezone

def post_list(request):
	template_name = 'blog/post_list.html'
	posts = Post.objects.all()
	return render(request, template_name, {'posts':posts})

def post_details(request, pk):
	template_name = 'blog/post_detail.html'
	post = Post.objects.get(pk=pk)
	return render(request, template_name, {'post': post})

def post_new(request):
	template_name = 'blog/post_edit.html'
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			post.publish_date = timezone.now()
			post.save()
			return redirect('/')
	else:
		form = PostForm()

	return render(request, template_name, {'form':form})

def post_edit(request, pk):
	template_name = 'blog/post_edit.html'
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = PostForm(request.POST, instance=post)
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			post.publish_date = timezone.now()
			post.save()
			return redirect('/')
	else:
		form = PostForm(instance=post)
	return render(request, template_name, {'form':form})