
from django.urls import reverse_lazy
from django.views import View
from django.db.models import Q

from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import DetailView, ListView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404

from .forms import CreatePostForm, ImageFormSet
from .models import Post, PostImage, Category


class IndexPageView(ListView):
    model = Post
    template_name = 'post/index.html'
    context_object_name = 'posts'




class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = 'posts'
    paginate_by = 1




# product/id/

class PostDetailsView(DetailView):
    queryset = Post.objects.all()
    template_name = 'post/post_details.html'
    context_object_name = 'post'





class IsAdminCheckMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and (self.request.user.is_staff or self.request.user.is_superuser)


class CreatePostView(IsAdminCheckMixin, View):
    def get(self, request):
        form = CreatePostForm()
        images_form = ImageFormSet(queryset=PostImage.objects.none())
        return render(request, 'post/create.html', locals())

    def post(self, request):
        form = CreatePostForm(request.POST)
        images_form = ImageFormSet(request.POST, request.FILES, queryset=PostImage.objects.none())

        if form.is_valid() and images_form.is_valid():
            post = form.save()
            for i_form in images_form.cleaned_data:
                image = i_form.get('image')
                if image is not None:
                    pic = PostImage(post=post, image=image)
                    pic.save()
            return redirect(post.get_absolute_url())

        print(form.errors, images_form.errors)


class PostDeleteView(IsAdminCheckMixin, DeleteView):
    model = Post
    template_name = 'post/delete.html'
    success_url = reverse_lazy('index-page')


class PostEditView(IsAdminCheckMixin, View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CreatePostForm(instance=post)
        images_form = ImageFormSet(queryset=post.images.all())
        return render(request, 'post/edit.html', locals())

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CreatePostForm(instance=post, data=request.POST)
        images_form = ImageFormSet(request.POST,
                                   request.FILES,
                                   queryset=post.images.all())

        if form.is_valid() and images_form.is_valid():
            product = form.save()
            for i_form in images_form.cleaned_data:
                image = i_form.get('image')
                if image is not None and not PostImage.objects.filter(post=post, image=image).exists():
                    pic = PostImage(post=post, image=image)
                    pic.save()
            for i_form in images_form.deleted_forms:
                image = i_form.cleaned_data.get('id')
                if image is not None:
                    image.delete()
            return redirect(post.get_absolute_url())
        print(form.errors, images_form.errors)



class SearchResultsView(View):
    def get(self, request):
        search_param = request.GET.get('q')
        results = Post.objects.filter(Q(title__icontains=search_param) | Q(description__icontains=search_param))
        return render(request, 'post/search_results.html', locals())