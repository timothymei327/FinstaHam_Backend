from rest_framework import serializers
from .models import Forum, Post, Comment

class ForumSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        view_name='post_detail',
        many=True,
        read_only=True
    )
    class Meta:
       model = Forum
       fields = ('id', 'name', 'description', 'photo_url', 'posts')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    forum = serializers.HyperlinkedRelatedField(
        view_name='forum_detail',
        read_only=True
    )
    comments = serializers.HyperlinkedRelatedField(
        view_name='comment_detail',
        many=True,
        read_only=True
    )
    class Meta:
       model = Post
       fields = ('id', 'forum', 'photo_urls', 'caption', 'hashtags', 'comments')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = serializers.HyperlinkedRelatedField(
        view_name='post_detail',
        read_only=True
    )
    class Meta:
       model = Comment
       fields = ('id', 'post', 'body')