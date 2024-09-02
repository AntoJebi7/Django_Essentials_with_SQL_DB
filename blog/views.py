from django.shortcuts import render, redirect  #import redirect module for redirecting the urls
from django.http import HttpResponse
from django.urls import reverse  # for reverse and named urls
# Create your views here.

def index(request):
    # return HttpResponse("Hello First Page")
    # render the html files
    return render(request,'index.html') 


        #str:post_id from urls.py
        # f for format string 
def detail(request,post_id):

    #return HttpResponse(f"post detail page , ID is {post_id}")
    return render(request,'detail.html') 
    
    
# redirect scenario from this 
def old_url_redirect(request):
                            # app name : url_name    usage -> go to -> urls.py(blog)
    return redirect(reverse('blog:new_page_url'))

# redirected to this
def new_url_view(request):
    return HttpResponse("This is New Url")