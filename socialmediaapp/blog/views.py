from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView
from django.views.generic import DetailView # This view is imported for blogpost details.
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

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
    return render(request,'blog/about.html',{'title':'About Page'})

class PostListView(ListView):
    model= Post
    template_name = 'blog/home.html'
    context_object_name='posts'
    ordering = ['-date_posted']  # Ordering of posts so that newest comes on top

class PostDetailView(DetailView):
    model = Post

#LoginRequiredMixin post entry sayfasına girildiğinde logine yönlendirme için kullanılıyor.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title' , 'content', 'link']
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title' , 'content', 'link']
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return 1
        return 0


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url='/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return 1
        return 0