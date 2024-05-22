from django.shortcuts import render
from blog.models import Post
from website.models import Contact
# from website.forms import NameForm,ContactForm
from website.forms import ContactForm, NewsletterForm
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages


# Create your views here.
def index_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.datetime.now(),status=1)
    print(posts)
    content = {'posts':posts}
    return render(request,'mysite/index.html',content)

def about_view(request):
    return render(request,'mysite\\about.html')
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your ticket submitted succesfuly.')
        else:
            messages.add_message(request,messages.ERROR,'Your ticket didn\'t submitted.')
    form = ContactForm()
    return render(request,'mysite\\contact.html',{'form':form})

def elements_view(request):
    return render(request,'mysite\\elements.html')

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')

def test_view(request):    
    if request.method == 'POST':        
        # name = request.POST.get('name')
        # form = NameForm(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            # name = form.cleaned_data['name']            
            # email = form.cleaned_data['email']
            # subject = form.cleaned_data['subject']
            # message = form.cleaned_data['message']

            # print(name,email,subject,message)
            form.save()
            return HttpResponse('done')
        
        else:
            return HttpResponse('not valid.')       
    # elif request.method == 'GET':
    #     print('GET')
    form = ContactForm()
    
    return render(request,'mysite\\test.html',{'form':form})

    