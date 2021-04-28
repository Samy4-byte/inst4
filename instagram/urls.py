"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from post.views import IndexPageView, PostDetailsView, PostListView, PostDeleteView, CreatePostView, \
    PostEditView, SearchResultsView

urlpatterns = [
  path('admin/', admin.site.urls),
  path('account/', include('account.urls')),
  path('', IndexPageView.as_view(), name='index-page'),
  path('post/create/', CreatePostView.as_view(), name='create-post'),
  path('post/search/', SearchResultsView.as_view(), name='search-results'),
  path('post/<slug:post_slug>/', PostListView.as_view(), name='post-list'),
  path('post/details/<int:pk>/', PostDetailsView.as_view(), name='post-details'),
  path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='delete-post'),
  path('post/edit/<int:pk>/', PostEditView.as_view(), name='edit-post'),
  path('post/', PostListView.as_view(), name='post-list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

