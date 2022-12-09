from django.db.models import Q
from .models import Post
from .models import Comment
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from users.models import Profile
from itertools import chain
from .forms import CommentForm
from django.db.models import Count

def searchposts(request):
    if request.method == "POST":
        searched = request.POST['searched']
        posts = Post.objects.filter(Q(title__icontains=searched) | Q(content__icontains=searched))
        post_count = posts.count()
        if post_count > 0:
            return render(request, 'blog/searchposts.html',
                      {'searched':searched,
                       'posts':posts})
        else:
            return render(request, 'blog/searchposts.html',
                          {'searched': searched, 'post_count':post_count})

    else:
        context = {
            'posts': Post.objects.all()
        }
        return render(request, 'blog/searchposts.html', context)


def SaveView(request,pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.saving.filter(id=request.user.id).exists():
        post.saving.remove(request.user.id)
    else:
        post.saving.add(request.user.id)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


def posts_of_following_profiles(request):
    profile = Profile.objects.get(user=request.user)
    users = [user for user in profile.following.all()]
    posts = []
    qs = None
    for u in users:
        userposts = Post.objects.filter(author=u)
        posts.append(userposts)
    if len(posts)>0:
        qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.date_posted)
    return render(request, 'blog/about.html', {'posts':qs})

def saved_posts (request):
    context =  {
        'posts': Post.objects.filter(saving=request.user)
       }
    return render(request, 'blog/savedposts.html', context)

def tagged_posts (request,pk):
    context =  {
        'posts': Post.objects.filter(tags=pk)
       }
    return render(request, 'blog/tags.html', context)
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

class PostListView(LoginRequiredMixin, ListView):
    model= Post
    template_name = 'blog/home.html'
    context_object_name='posts'
    ordering = ['-date_posted']  # Ordering of posts so that newest comes on top

class SavedPostListView(ListView):
    model= Post
    template_name = 'blog/savedposts.html'
    context_object_name='posts'
    ordering = ['-date_posted']  # Ordering of posts so that newest comes on top
class AllPostListView(ListView):
    model= Post
    template_name = 'blog/allposts.html'
    context_object_name='posts'
    ordering = ['-date_posted']  # Ordering of posts so that newest comes on top
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        mypost = get_object_or_404(Post, id=self.kwargs['pk'])
        save = False
        if mypost.saving.filter(id=self.request.user.id).exists():
            save = True
        context["save"] = save
        return context

#LoginRequiredMixin post entry sayfasına girildiğinde logine yönlendirme için kullanılıyor.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title' , 'content', 'link', 'tags']
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title' , 'content', 'link', 'tags']
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return 1
        return 0

class AddCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        form.instance.name=self.request.user
        form.instance.post_id = self.kwargs['pk']
        postnum = self.kwargs['pk']
        print (postnum)
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        return reverse("post-detail", kwargs={'pk':self.kwargs['pk']})
 #   success_url = reverse_lazy('blog-allposts')


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url='/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return 1
        return 0