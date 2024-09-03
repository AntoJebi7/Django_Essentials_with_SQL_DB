from django.shortcuts import render, redirect  #import redirect module for redirecting the urls
from django.http import HttpResponse
from .models import Post
import logging  #Logger
from django.urls import reverse  # for reverse and named urls
# Create your views here.
blog_title = "Latest Posts dynamic"
base_title = "Base title dynamic"

'''
posts = [
    {'id':1, 'title': 'Post 1', 'content': 'Content of Post 1', 'img_src': 'https://picsum.photos/id/233/200'},
    {'id':2,'title': 'Post 2', 'content': 'Content of Post 2', 'img_src': 'https://picsum.photos/id/231/200'},
    {'id':3,'title': 'Post 3', 'content': 'Content of Post 3', 'img_src': 'https://picsum.photos/id/221/200'},
    {'id':4,'title': 'Post 4', 'content': 'Content of Post 4', 'img_src': 'https://picsum.photos/id/211/200'},
]
'''


def index(request):
    # return HttpResponse("Hello First Page")
    # render the html files
    # variable interpolation
    
    posts = Post.objects.all()  #send post data as list
    
    return render(request,'index.html' , {'blog_title':blog_title,'base_title':base_title, 'posts':posts} ) #dict value

        #str:post_id from urls.py
        # f for format string 
def detail(request,post_id):  # datatype mismatch may occurs
    #iterator concept - python
    post = next((item for item in posts if item['id']==int(post_id)), None)
    #logger=logging.getLogger("TESTING")
    #logger.debug(f'Post variable is {post}')
    #return HttpResponse(f"post detail page , ID is {post_id}")
    return render(request,'detail.html', {'post':post}) 
    
    
# redirect scenario from this 
def old_url_redirect(request):
                            # app name : url_name    usage -> go to -> urls.py(blog)
    return redirect(reverse('blog:new_page_url'))

# redirected to this
def new_url_view(request):
    return HttpResponse("This is New Url")