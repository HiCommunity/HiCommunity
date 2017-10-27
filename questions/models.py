# coding=utf-8
from django.db import models
from users.models import Account


class Region(models.Model):
    """
    Region contains one or more boards
    """
    name = models.CharField(max_length=32, verbose_name='区域名')
    address = models.CharField(max_length=16, verbose_name='区域URL地址')

    def __unicode__(self):
        return '%s 区域' % self.name


class Board(models.Model):
    """
    Board
    """
    region = models.ForeignKey(to=Region, related_name='board_of_region')
    name = models.CharField(max_length=32, verbose_name='版块名')
    address = models.CharField(max_length=16, verbose_name='版块URL地址')

    def __unicode__(self):
        return '%s 版块' % self.name


class Question(models.Model):
    """
    Questions belong to a board
    """
    board = models.ForeignKey(to=Board, related_name='question_of_board')
    title = models.CharField(max_length=128, verbose_name='标题')
    content = models.TextField(max_length=65535, verbose_name='内容')
    owner = models.ForeignKey(to=Account, related_name='question_owner')
    # metadata = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_date = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __unicode__(self):
        return '%s ...' % self.title if len(self.title) > 20 else self.title


class Answer(models.Model):
    """
    Replies of Questions
    对象为question owner或回帖中的某人
    """
    question = models.ForeignKey(to=Question, related_name='answer_of_question')
    content = models.TextField(max_length=65535, verbose_name='内容')
    up = models.PositiveIntegerField(default=0)
    down = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(to=Account, related_name='answer_owner')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_date = models.DateTimeField(auto_now=True, verbose_name='修改时间')

    def __unicode__(self):
        content = self.content if len(self.content) > 10 else self.content
        return 'Answer(question id %d): %s ...' % (self.question.id, content)


class Comment(models.Model):
    """
    Comments to an answer
    """
    answer = models.ForeignKey(to=Answer, related_name='comment_of_answer')
    content = models.CharField(max_length=512, verbose_name='评论')
    up = models.PositiveIntegerField(default=0)
    owner = models.ForeignKey(to=Account, related_name='answer_comment_owner')
    create_date = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __unicode__(self):
        content = self.content if len(self.content) > 10 else self.content
        return 'AnswerComment(answer id %d): %s ...' % (self.answer.id, content)
