from rest_framework import generics

from .models import Blog
from .serailizers import BlogDetailSerializer, BlogSerializer


class BlogListApiView(generics.ListAPIView):
    """
    list all
    published(their publish_time is gte than time.now())
    post  ️
    """

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogDetailApiView(generics.RetrieveAPIView):
    """
    detail endpoint for  published  post ️
    """

    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
