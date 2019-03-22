from django.views.generic import TemplateView
from django.views import generic
from core.models import User, UserPost
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from core.forms import PostForm


# Create your views here.

class HomePageView(generic.ListView):
    '''List view for the post on the homepage'''
    model = UserPost
    template_name = 'index.html'
    paginate_by = 25

    def get_queryset(self):
        """Return the last five published questions."""
        return UserPost.objects.all()

class NewPostView(CreateView, LoginRequiredMixin):
    '''    '''
    model = UserPost
    fields = ['title', 'source_name', 'post_url', 'body', 'topic']
    template_name = 'user_post.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.username
        return super().form_valid(form)

class PostDetailView(generic.DetailView):
    '''Generic detail view for a post'''
    model = UserPost

class OtherUserProfileView(generic.DetailView):
    '''Detail view for user's profiles'''
    model = User
    slug_field = 'User.username'

class UserProfileView(generic.FormView, LoginRequiredMixin):
    '''Allows a user to view and edit their own profile'''
    model = User
    template_name = 'user_profile.html'
    slug_field = 'User.username'

class WelcomeView(TemplateView):
    template_name = 'welcome.html'

class CCView(TemplateView):
    template_name = 'codeofconduct.html'

class FAQView(TemplateView):
    template_name = 'faq.html'


