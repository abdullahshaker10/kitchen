from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from django.conf import settings
from .models import *
from clients.models import Client
User = settings.AUTH_USER_MODEL


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


class SimpleSignupForm(SignupForm):
    user_type = forms.ChoiceField(required=True, choices=USER_CHOICES)

    def save(self, request):
        user = super(SimpleSignupForm, self).save(request)
        user.user_type = self.cleaned_data['user_type']
        if user.user_type == 'CHIEF':
            Chief.objects.create(user=user)
        elif user.user_type == 'ASSISTANT':
            Assistant.objects.create(user=user)
        elif user.user_type == 'CLIENT':
            Client.objects.create(user=user)
        else:
            Waiter.objects.create(user=user)
        user.save()
        return user
