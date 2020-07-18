from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostUpdate
from faker import Faker
from django.core.paginator import Paginator

# Create your views here.
def main(request):
    posts = Post.objects

    #Post 를 쿼리셋으로 가져옴
    post_list = Post.objects.all()

    #그걸 몇개씩 잘라서 페이지를 만들어줘
    paginator = Paginator(post_list,10)

    #실제로 페이지에 들어가는 내용을 가져와줘
    page = request.GET.get('page')

    #그걸 뿌릴 수 있게 바꿔줘
    articles = paginator.get_page(page)

    return render(request,"main.html",{'posts':posts, 'articles':articles})

def detail(request,post_id):
    post_detail = get_object_or_404(Post, pk=post_id)
    return render(request,'detail.html',{'post':post_detail})

def new(request):
    return render(request,'new.html')

def create(request):
    post = Post()
    post.title = request.GET['title']
    post.body = request.GET['body']
    post.pub_date = timezone.datetime.now()
    post.save()
    return redirect('/post/'+str(post.id))

def delete(request,post_id):
    Post.objects.get(id=post_id).delete()
    return redirect('/')

def update(request,post_id):

    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        form = PostUpdate(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data['title']
            post.body = form.cleaned_data['body']
            post.pub_date = timezone.now()
            post.save()
            return redirect('/post/'+str(post.id))
            
    else:
        form = PostUpdate(instance = post)
        return render(request,'update.html',{'form':form})

def fake(request):
    for i in range(10):
        post = Post()
        fake = Faker()
        post.title = fake.name()
        post.body = fake.sentence()
        post.pub_date = timezone.datetime.now()
        post.save()

    return redirect('/')
        