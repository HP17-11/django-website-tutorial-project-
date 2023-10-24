from cProfile import Profile
from django import forms
from django.forms import models, ModelForm, widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Skill, Profile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description', 'user']
        labels = {
            'name': 'Skill',
            'user': 'User Id',
        }
        exclude = ['user']
        # widgets = {'user': forms.ChoiceField(widget=forms.RadioSelect)}

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ['name', 'email', 'short_intro', 'location', 'description', 'username', 'profile_image', 
                  'social_twitter', 'social_github',  'social_linkedin', 
                  'social_website', ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})