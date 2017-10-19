from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse
from users.utils.security import request_method, login_required, role_restrict
from posts import models as posts_models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from common.utils.string import str2int
from posts.exception import *
from common.exception import EmptyContent
from users.models import Account
from common.constants.common import RET_FORMAT
import json
from posts import views_helper


@request_method('GET')
def post_index(request):
    return TemplateResponse(request, 'posts/index.html')


@request_method('GET')
def post_list_page(request, region, board):
    """
    Post list page
    """

    page = request.GET.get('page')
    items_per_page = str2int(request.GET.get('items', 20), 20)
    post_objects = posts_models.Post.objects.filter(board__address=board,
                                                    board__region__address=region
                                                    ).order_by('-create_date')

    # Pagination
    paginator = Paginator(post_objects, items_per_page)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    # context
    context = {'posts': posts}
    _ = views_helper.region_and_board_context(region, board)
    context.update(_)
    return TemplateResponse(request, 'posts/board.html', context=context)


def post_detail_page(request, *args, **kwargs):
    pid = kwargs.get('id')
    try:
        post_object = posts_models.Post.objects.get(id=pid)
    except Exception as e:
        print(str(e))
        raise

    context = {'post_detail': post_object}

    return render(request, 'posts/detail.html', context=context)


@login_required
@request_method('POST')
def new_post(request, region, board, *args, **kwargs):
    ret = RET_FORMAT
    title = request.POST.get('title')
    content = request.POST.get('content')
    if not all((title, content)):
        raise EmptyContent
    uid = kwargs['user_id']
    try:
        posts_models.Post.objects.create(title=title,
                                         content=content,
                                         owner=Account.objects.get(id=uid),
                                         board=posts_models.Board.objects.get(address=board))
    except Exception as e:
        print(str(e))
        raise CreatePostFailed
    else:
        ret['result'] = True
    return HttpResponse(json.dumps(ret))


@login_required
@request_method('POST')
def close_post(request):
    pass


@login_required
@request_method('DELETE')
@role_restrict('admin')
def delete_post(request):
    pass