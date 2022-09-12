from rest_framework import serializers
from .models import Forum, Post, Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'post', 'body')


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Post
        fields = ('id', 'forum', 'photo_urls',
                  'caption', 'hashtags', 'comments')


class ForumSerializer(serializers.ModelSerializer):
    posts = PostSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = Forum
        fields = ('id', 'name', 'description', 'photo_url', 'posts')
