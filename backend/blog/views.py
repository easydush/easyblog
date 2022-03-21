# Create your views here.
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from blog.models import Post, Comment
from blog.permissions import IsAuthorOrReadOnly
from blog.serializers import PostSerializer, CommentWithChildrenSerializer, PostWithCommentsSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostWithCommentsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostWithCommentsSerializer(post)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.id)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def list(self, request):
        queryset = Comment.objects.all()
        serializer = CommentWithChildrenSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Comment.objects.all()
        comment = get_object_or_404(queryset, pk=pk)
        serializer = CommentWithChildrenSerializer(comment)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.id)
