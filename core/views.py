from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import generic
from core.models import User, UserPost, Vote
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.edit import CreateView, UpdateView
from core.forms import PostForm, EditProfileForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Count

# Create your views here.

# Class Based Views
class HomePageView(generic.ListView):
    '''List view for the post on the homepage'''
    model = UserPost
    template_name = 'index.html'
    paginate_by = 20

    def get_queryset(self):
        """Return the last five published questions."""
        return UserPost.objects.all()

class PostDetailView(generic.DetailView):
    '''Generic detail view for a post'''
    model = UserPost

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

def post_detail_view(request, slug):
    post = get_object_or_404(UserPost, slug=slug)
    
    return render(request, "post_detail.html", {
        "post": post,
    })

# @login_required    
# def vote_view(request, slug):   
#      poll_votes = PollVote.objects.filter(poll=poll_id).annotate(num_votes=Count('answer__id'))

#     post = get_object_or_404(UserPost, slug)

#     vote, created = request.user.vote_set.get_or_create(post=post)

#     if created:
#         messages.success(request, f"You liked {post.title}.")
#     else:
#         messages.info(request, f"You unliked for {post.title}.")
#         vote.delete()

#     return redirect('post_detail', slug)

def vote(request, slug):
    vote = get_object_or_404(UserPost, slug)
    try:
        selected = Vote.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Vote.DoesNotExist):
        return render(request, 'polls_detail.html', {
            'vote': vote,
        })
    else:
        selected.vote += 1
        selected.save()

        return HttpResponseRedirect(reverse('post_detail', args=(selected.id,)))

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




