from django.urls import path
from .views import index, single_blog, contact, category, blog

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('category/', category, name='category'),
    path('blog/', blog, name='blog'),
    path('single_blog/<int:id>/', single_blog, name='single_blog'),
]