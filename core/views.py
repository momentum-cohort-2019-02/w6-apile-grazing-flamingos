from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import generic
from core.models import User, UserPost, Topic, Comment, Vote
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views.generic.edit import CreateView, UpdateView
from core.forms import PostForm, EditProfileForm, CommentForm
# from django.urls import reverse, reverse_lazy


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



# class PostDetailView(generic.DetailView):
#     '''Generic detail view for a post'''
#     model = UserPost

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
    comments = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            #### Not sure if the below statement works????
            # comments.save()
            return redirect(to='post.detail.html')

    else:
        form = CommentForm()

    return render(request, "post_detail.html", {
        "form": form,
        "post": post,
        "comments": comments,
    })
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




