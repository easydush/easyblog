from rest_framework import serializers

from blog.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        exclude = ['author']


class SubCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentWithChildrenSerializer(serializers.ModelSerializer):
    children = SubCommentSerializer(many=True)

    class Meta:
        model = Comment
        fields = '__all__'


class PostWithCommentsSerializer(serializers.ModelSerializer):
    comments = CommentWithChildrenSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['author']
