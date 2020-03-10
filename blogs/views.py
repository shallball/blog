from django.shortcuts import render
from .models import BlogPost
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from .forms import PostForm
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request,'blogs/index.html')
	
def posts(request):
	"""显示帖子列表"""
	posts=BlogPost.objects.order_by('-date_added')
	context={'posts':posts}
	return render(request,'blogs/posts.html',context)
		
def post(request,post_id):
	"""显示单篇帖子内容"""
	post=BlogPost.objects.get(id=post_id)
	context={'post':post}
	return render(request,'blogs/post.html',context)

@login_required			
def new_post(request):
	"""发布新帖子"""
	if request.method!='POST':
		#未提交数据，创建新表单
		form=PostForm()
	else:
		#提交数据，对数据进行处理
		form=PostForm(request.POST)
		if form.is_valid():
			new_post=form.save(commit=False)
			new_post.owner=request.user
			new_post.save()
			return HttpResponseRedirect(reverse('blogs:posts'))		
	context={'form':form}	
	return 	render(request,'blogs/new_post.html',context)

@login_required	
def edit_post(request,post_id):
	post=BlogPost.objects.get(id=post_id)
	#确认请求的帖子编辑页面属于当前用户
	if post.owner!=request.user:
		raise Http404
	if request.method !='POST':
		#初次请求，填充表单
		form=PostForm(instance=post)
	else:
		#提交数据，对数据进行处理
		form=PostForm(instance=post,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:post',
				args=[post_id]))
	
	context={'post':post,'form':form}			
	return render(request,'blogs/edit_post.html',context)

@login_required						
def my_posts(request):
	"""显示当前用户发表的帖子"""
	posts=BlogPost.objects.filter(owner=request.user).order_by('date_added')
	context={'posts':posts}
	return render(request,'blogs/my_posts.html',context)

	
		
