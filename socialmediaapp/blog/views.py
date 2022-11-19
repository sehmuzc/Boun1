from django.shortcuts import render
from .models import Post
from django.views.generic import ListView
from django.views.generic import DetailView # This view is imported for blogpost details.



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

class PostListView(ListView):
    model= Post
    template_name = 'blog/home.html'
    context_object_name='posts'
    ordering = ['-date_posted']  # Ordering of posts so that newest comes on top

class PostDetailView(DetailView):
    model = Post
