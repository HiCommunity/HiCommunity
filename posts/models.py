# coding=utf-8
from django.db import models
from users.models import Profile


class Post(models.Model):
    """
    Posts
    """
    title = models.CharField(max_length=128, verbose_name='标题')
    content = models.TextField(max_length=65535, verbose_name='内容')
    owner = models.ForeignKey(to=Profile, related_name='post_owner')
    # metadata = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_date = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __unicode__(self):
        return '%s ...' % self.title if len(self.title) > 20 else self.title


class Reply(models.Model):
    """
    Replies of Posts
    对象为poster owner或回帖中的某人
    """
    post = models.ForeignKey(to=Post, related_name='post_of_reply')
    content = models.TextField(max_length=65535, verbose_name='内容')
    up = models.PositiveIntegerField()
    down = models.PositiveIntegerField()
    owner = models.ForeignKey(to=Profile, related_name='reply_owner')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_date = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __unicode__(self):
        content = self.content if len(self.content) > 10 else self.content
        return 'Reply(post id %d): %s ...' % (self.post.id, content)


class ReplyComment(models.Model):
    """
    Comments of a reply
    """
    reply = models.ForeignKey(to=Reply, related_name='reply_of_comment')
    content = models.CharField(max_length=512, verbose_name='评论')
    owner = models.ForeignKey(to=Profile, related_name='reply_comment_owner')
    target = models.ForeignKey(to=Profile, related_name='target_of_reply')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __unicode__(self):
        content = self.content if len(self.content) > 10 else self.content
        return 'ReplyComment(reply id %d): %s ...' % (self.reply.id, content)
