from django.views.generic.detail import DetailView

from .models import Profile


class Profile(DetailView):
    model = Profile
    template_name = 'profile.html'

    def get_object(self):
        return self.request.user.profile





