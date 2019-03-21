from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from core.models import User, UserPost
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class HomePageView(generic.ListView):
    model = UserPost
    template_name = 'index.html'
    paginate_by = 25

    def get_queryset(self):
        """Return the last five published questions."""
        return UserPost.objects.all()

class OtherUserProfileView(generic.DetailView):
    model = User
    slug_field = 'User.username'

class UserProfileView(generic.FormView, LoginRequiredMixin):
    model = UserPost
    template_name = 'user_post'
    slug_field = 'User.username'

    # def form_valid(self, form):
    #     # This method is called when valid form data has been POSTed.
    #     # It should return an HttpResponse.
    #     form.send_email()
    #     return super().form_valid(form)
