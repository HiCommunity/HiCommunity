# coding=utf-8
import json

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import HttpResponse, Http404
from django.template.response import TemplateResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import F
from datetime import datetime

from common.constants.common import RET_FORMAT
from common.exception import EmptyContent
from common.utils.string_ import str2int
from questions import models as questions_models
from questions.models import Question, Answer
from questions import views_helper
from questions.exception import *
from users.models import Account
from users.constants.common import SESSION_LOGIN_USER
from users.utils.security import request_method, login_required, role_restrict


@request_method('GET')
def question_index(request):
    return TemplateResponse(request, 'questions/index.html')


@request_method('GET')
def question_list_page(request, region, board):
    """
    Question list page
    """

    page = request.GET.get('page')
    items_per_page = str2int(request.GET.get('items', 5), 20)
    question_objects = Question.objects.filter(
        board__address=board,
        board__region__address=region)

    # Pagination
    paginator = Paginator(question_objects, items_per_page)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    # context
    context = {'questions': questions}
    # Note: regions and board information will be rendered at
    # common/middlewares.py for all templates with a
    # question-started URL.
    # add current region and board to context
    _ = views_helper.region_and_board_context(region, board)
    context.update(_)
    return TemplateResponse(request, 'questions/board.html', context=context)


def question_detail_page(request, *args, **kwargs):
    pid = kwargs.get('pid')
    try:
        question_object = Question.objects.get(id=pid)
    except Question.DoesNotExist:
        raise Http404

    context = {'question_detail': question_object}

    return TemplateResponse(request, 'questions/detail.html', context=context)


@login_required
@request_method('POST')
def new_question(request, region, board, *args, **kwargs):
    ret = RET_FORMAT
    title = request.POST.get('title')
    content = request.POST.get('content')
    if not all((title, content)):
        raise EmptyContent
    uid = kwargs[SESSION_LOGIN_USER]['id']
    try:
        Question.objects.create(
            title=title,
            content=content,
            owner=Account.objects.get(id=uid),
            board=questions_models.Board.objects.get(address=board))
    except Exception as e:
        print(str(e))
        raise CreateQuestionFailed
    else:
        ret['result'] = True
    return HttpResponse(json.dumps(ret))


@login_required
@request_method('POST')
def new_answer(request, region, board, qid, **kwargs):
    ret = RET_FORMAT
    content = request.POST.get('content')
    if not content:
        raise EmptyContent
    uid = kwargs[SESSION_LOGIN_USER]['id']
    try:
        Question.objects.filter(id=qid).update(answer_count=F('answer_count') + 1,
                                               update_at=datetime.utcnow())
        Answer.objects.create(question_id=qid, content=content, owner_id=uid)
        ret['result'] = True
    except Exception as e:
        print(str(e))
        raise CreateAnswerFailed
    return HttpResponse(json.dumps(ret))


@login_required
@request_method('POST')
def new_comment(request, region, board, qid, **kwargs):
    pass


@login_required
@request_method('POST')
def close_question(request):
    pass


@login_required
@request_method('DELETE')
@role_restrict('admin')
def delete_question(request):
    pass
