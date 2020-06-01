from django.contrib.auth.forms import UserCreationForm
from django.core.files.images import get_image_dimensions
from django import forms
from django.contrib.auth.models import User
from blog.models import MyUser, Post, Comment
import datetime


class RegisterForm(UserCreationForm):

    username = forms.CharField(label='Username', max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Sherlock42"}))
    first_name = forms.CharField(label='First name (optional)', max_length=30, required=False,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "John"}))
    last_name = forms.CharField(label='Last name (optional)', max_length=30, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Watson"}))
    email = forms.EmailField(label='Email', max_length=254,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "hello@gmail.com"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class LoadAvatarForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ('avatar',)

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:

            # validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, GIF or PNG image.')

            # validate file size
            if avatar._size > 4 * 1024 * 1024:
                raise forms.ValidationError(u'Avatar file size may not exceed 4mb.')

            w, h = get_image_dimensions(avatar)

            # validate dimensions
            max_width = max_height = 500
            if w > max_width or h > max_height:
                raise forms.ValidationError(u'Avatar sizes may not exceed 1000px')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        return avatar


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'image')

    title = forms.CharField(label='Title',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}))
    text = forms.CharField(label=False,
                           widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text'}))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    def clean_img(self):
        img = self.cleaned_data['img']

        try:
            # validate content type
            main, sub = img.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'gif', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, GIF or PNG image.')

            # validate file size
            if img._size > 20 * 1024 * 1024:
                raise forms.ValidationError(u'Image file size may not exceed 20mb.')

        except AttributeError:
            """
            Handles case when we are updating the post
            and do not supply a new img
            """
            pass

        return img


class CommentForm(forms.ModelForm):

    text = forms.CharField(label=False,
                           widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'rows': "3",
                                                        'placeholder': 'Comment'}))

    class Meta:
        model = Comment
        fields = ('text',)

