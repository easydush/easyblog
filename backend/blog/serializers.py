from rest_framework import serializers

from blog.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['post', 'parent_comment']


class CommentWithPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class PostWithCommentsSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
