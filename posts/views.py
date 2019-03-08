from rest_framework import generics

from .models import Post
from .permissions import (IsAuthorOrReadOnly, IsAuthor)
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthorOrReadOnly,)
    permission_classes = (IsAuthor,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer