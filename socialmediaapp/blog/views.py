from django.shortcuts import render
from .models import Post

# Create your views here.

posts = [
    {
'author': 'Sehmuz',
'title':'Post 1',
'content':'First post content',
'date_posted':' 29 Ekim 2022'
    },
    {
'author': 'Cihan Cebiroglu',
'title':'Euroleague',
'content':'Fenerbahçe Euroleague şampisi olacak.',
'date_posted':' 30 Ekim 2022'
    }
]

def home(request):
    context =  {
        'posts': Post.objects.all()
       }     
    return render(request,'blog/home.html', context)

def about(request):
    context =  {
        'posts': Post.objects.all()
       }     
    return render(request,'blog/about.html',{'title':'AboutView'})

