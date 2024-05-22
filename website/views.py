from django.shortcuts import render
from blog.models import Post
from website.models import Contact
from website.forms import NameForm,ContactForm
from django.utils import timezone
from django.http import HttpResponse


# Create your views here.
def index_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.datetime.now(),status=1)
    print(posts)
    content = {'posts':posts}
    return render(request,'mysite/index.html',content)

def about_view(request):
    return render(request,'mysite\\about.html')
def contact_view(request):
    return render(request,'mysite\\contact.html')
def elements_view(request):
    return render(request,'mysite\\elements.html')

def test_view(request):    
    if request.method == 'POST':
        # name = request.POST.get('name')
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']            
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # print(name,email,subject,message)

            return HttpResponse('done')
        else:
            return HttpResponse('not valid.')       
    # elif request.method == 'GET':
    #     print('GET')
    form = ContactForm()
    
    return render(request,'mysite\\test.html',{'form':form})

    