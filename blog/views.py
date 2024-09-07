from django.shortcuts import render, redirect  #import redirect module for redirecting the urls
from django.http import HttpResponse
from .models import Post
from django.http import Http404
from .forms import ContactForm
import logging  #Logger
from django.core.paginator import Paginator
from django.urls import reverse  # for reverse and named urls
# Create your views here.

#variable interpolation
blog_title = "Latest Blog Posts "
base_title = "Base Title dynamic"



posts_wdb = [
    {'id':1, 'title': 'Post 1', 'content': 'Content of Post 1', 'img_src': 'https://picsum.photos/id/233/200'},
    {'id':2,'title': 'Post 2', 'content': 'Content of Post 2', 'img_src': 'https://picsum.photos/id/231/200'},
    {'id':3,'title': 'Post 3', 'content': 'Content of Post 3', 'img_src': 'https://picsum.photos/id/221/200'},
    {'id':4,'title': 'Post 4', 'content': 'Content of Post 4', 'img_src': 'https://picsum.photos/id/211/200'},
]



def index(request):
    # return HttpResponse("Hello First Page")
    # render the html files
    # variable interpolation
    
    all_posts = Post.objects.all()  #send post data as list
    #paginate
    paginator = Paginator(all_posts,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request,'index.html' , {'blog_title':blog_title,'base_title':base_title, 'posts':page_obj} ) #dict value

        #str:post_id from urls.py
        # f for format string 

def detail(request,slug):  # datatype mismatch may occurs
    #iterator concept - python
    #post = next((item for item in posts_wdb if item['id']==int(post_id)), None)
    #logger=logging.getLogger("TESTING")
    #logger.debug(f'Post variable is {post}')
    #return HttpResponse(f"post detail page , ID is {post_id}")
    try:
    # getting data from model by id
        post_db = Post.objects.get(slug=slug)  # pk = primary key
        related_posts = Post.objects.filter(category = post_db.category).exclude(pk=post_db.id)
    except Post.DoesNotExist:
        raise Http404("Post Does not exist , userdefined raise")


    return render(request,'detail.html', {'post':post_db , 'related_posts':related_posts}) 
    
    
# redirect scenario from this 
def old_url_redirect(request):
                            # app name : url_name    usage -> go to -> urls.py(blog)
    return redirect(reverse('blog:new_page_url'))

# redirected to this
def new_url_view(request):
    return HttpResponse("This is New Url")

def contact_view(request):
    if request.method == 'POST':
        ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        form = ContactForm(request.POST)
        if form.is_valid():
            logger=logging.getLogger("TESTING")
            logger.debug(f'POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}')
            success_message = "your email has been sent !"
            return render(request,'contact.html',{'form':form , 'success_message':success_message})
        else :
            logger.debug('Form Data Failure')

        return render(request,'contact.html',{'form':form , 'name':name,'email':email,'message':message})
    
    return render(request,'contact.html')