from django.shortcuts import render
from django.views.generic import DetailView, CreateView, UpdateView
from django.shortcuts import redirect

from .models import Profile, Query

def home(request):
    return render(request, 'index.html')

class ConsultationView(DetailView):
    model = Query
    template_name = 'consultation.html'
    context_object_name = 'que'
    def get_object(self):
        return Query.objects.all()


class MyProfile(DetailView):
    model = Profile
    template_name = 'profile.html'

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

    def get(self, request, *args, **kwargs):
        if not Profile.objects.filter(user=self.request.user):
            return redirect('create_profile')
        return super().get(request, *args, **kwargs)


class CreateProfile(CreateView):
    model = Profile
    template_name = 'profile_create.html'

    fields = ['user','birth_date', 'tnumber', 'sex', 'lang']


class UpdateProfile(UpdateView):
    model = Profile
    template_name = 'profile_update.html'
    fields = ['birth_date', 'tnumber', 'sex', 'lang']

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)





