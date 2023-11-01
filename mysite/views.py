from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime
from .models import Post


def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())

def showpost(request, slug):
    try:
        post = Post.objects.get(slug = slug)
        if post != None:
            return render(request, 'post.html', locals())
        else:
            return redirect("/")
    except:
        return redirect("/")




'''
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts): #enumerate 回傳回圈次數、內容
        post_lists.append(f'No.{count}-{post}<br>') 
    return HttpResponse(post_lists)
'''

