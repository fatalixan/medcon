from django.contrib import admin
from .models import Profile, Query, Consultation


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['birth_date', 'tnumber']

@admin.register(Query)
class QueryAdmin(admin.ModelAdmin):
    pass

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    pass