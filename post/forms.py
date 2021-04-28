from django import forms

from post.models import Post, PostImage


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class ImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']

ImageFormSet = forms.modelformset_factory(
    PostImage,
    form=ImageForm,
    extra=3,
    max_num=5,
    can_delete=True
)

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'