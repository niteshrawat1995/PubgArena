from django import forms


class PostForm(forms.ModelForm):

    class Meta:
        from .models import Post

        model = Post
        fields = ('title', 'content', )