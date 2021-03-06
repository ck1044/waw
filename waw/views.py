from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .forms import WriteForm


def index(request):
    """
    post 리스트 출력
    """
    post_list = Post.objects.order_by("?")
    context = {'post_list': post_list} # 쿼리셋 {key:value}
    return render(request, 'waw/post_list.html', context)
    # C:/projects/waw/templates/waw/post_list.html


def detail(request, post_id):
    """
    post 내용 출력
    """
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'waw/post_detail.html', context)


def aboutUS(request):
    """
    aboutUs 내용 출력
    """
    return render(request, 'waw/post_aboutUs.html')


def write(request):
    """
    post write
    """
    if request.method == 'POST':
        form = WriteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('waw:index')
    else:
        form = WriteForm()
    context = {'form': form}
    return render(request, 'waw/post_write.html', context)


def login(request):
    """
    login page
    """
    return render(request, 'waw/login_views.html')
