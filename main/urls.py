from django.urls import include, path
from .views import MyProfile, CreateProfile, UpdateProfile, ConsultationView

urlpatterns = [
    path('', MyProfile.as_view()),
    path('create/', CreateProfile.as_view(), name='create_profile'),
    path('update/', UpdateProfile.as_view(), name='update_profile'),
    path('consultation/', ConsultationView.as_view(), name='consultations'),


]


