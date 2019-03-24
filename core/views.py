from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import generic
from core.models import User, UserPost, Topic, Comment, Vote
from core.forms import PostForm, EditProfileForm, CommentForm
from django.contrib.auth.decorators import login_required
# from django.db.models import Count
# from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
# from django.http import HttpResponseRedirect

# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.edit import CreateView, UpdateView


# Create your views here.

# Class Based Views
class HomePageView(generic.ListView):
    '''List view for the post on the homepage'''
    model = UserPost
    template_name = 'index.html'
    paginate_by = 20
    num_comments = Comment.objects.count()
    comment = Comment.objects.all()
    userpost = UserPost.objects.all()

    def get_queryset(self):
        """Return the last five published questions."""
        return UserPost.objects.all()

# class UserProfileView(generic.DetailView):
#     '''Detail view for user's profiles'''
#     model = User
#     template_name = 'user_profile.html'

class WelcomeView(TemplateView):
    template_name = 'welcome.html'

class CCView(TemplateView):
    template_name = 'codeofconduct.html'

class FAQView(TemplateView):
    template_name = 'faq.html'


# Function based views

# User profile editing - needs to be worked on
def view_profile(request, slug):
    if slug:
        user = User.objects.filter(user__exact=user)
    else:
        user = request.user
    context = {
        'user': user,
    }
    return render(request, 'user_profile.html', context=context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts/profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'user_view.html', args)

@login_required
def new_post(request):
    
    if request.method=="POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'user_post.html', {'form': form})

# def post_detail_view(request, slug):
#     post = get_object_or_404(UserPost, slug=slug)
#     comments = Comment.objects.all()
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             #### Not sure if the below statement works????
#             # comments.save()
#             return redirect(to='post.detail.html')

#     else:
#         form = CommentForm()

#     return render(request, "post_detail.html", {
#         "form": form,
#         "post": post,
#         "comments": comments,
#     })

def post_detail_view(request, slug):
    post = get_object_or_404(UserPost, slug=slug)
    comments = Comment.objects.all()
    context = { 
        'post': post,
        'comments': comments,
    }

    return render(request, 'post_detail.html', context=context)

@login_required
def remove_post(request, slug):
    post = get_object_or_404(UserPost, slug=slug)
    post.delete()
    return redirect('index') 

# This needs to be adjusted because posting the comment returns this error: "Direct assignment to the reverse side of a related set is prohibited. Use post.set() instead." It is because the
@login_required
def new_comment(request, slug):
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = UserPost.objects.comments.set(slug=slug)
            comment.save()
            return redirect('post_detail', slug=slug)
    else:

        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form}) 

# @login_required
# def comment_remove(request, slug):
#     comment = get_object_or_404(Comment)
#     comment.delete()
#     return redirect('post_detail', slug)  

# the votes are not displaying on the detail page and the redirection gets a value error
@require_http_methods(['POST'])
@login_required
def vote(request, slug):
    vote = get_object_or_404(UserPost, slug)
    
    vote, created = request.user.voted_set.get_or_create(vote=vote)

    if created:
        messages.success(request, f"You liked {vote.title}.")
    else:
        messages.info(request, f"You unliked for {vote.title}.")
        vote.delete()

    return redirect(to='post_vote.html')

# I had some issues that I couldn't figure out with the classed based views, so I am leaving them alone for now. 

# class NewPostView(CreateView, LoginRequiredMixin):
#     '''View that allows users to create a post'''
#     model = UserPost
#     success_url = reverse_lazy('index')
#     fields = ['title', 'source_name', 'post_url', 'body', 'topic']
#     template_name = 'user_post.html'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

# class EditUserProfileView(UpdateView, LoginRequiredMixin):
#     '''Allows a user to view and edit their own profile'''
#     model = User
#     fields = ['profile_picture', 'about', 'email', 'gender_pronouns', 'about',]
#     template_name = 'user_view.html'
#     slug_field = 'username'
#     slug_url_kwarg = 'slug'
    

#     def get_success_url(self):
#         return reverse('user-profile', kwargs={'slug': self.slug})

    # def form_valid(self, form):
    #     form.instance.created_by = self.request.username
    #     return super().form_valid(form)
