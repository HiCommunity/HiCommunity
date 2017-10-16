from django.shortcuts import render
from common.utils.security import request_method
from posts import models as posts_models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from common.utils.string import str2int


@request_method('GET')
def post_index_page(request):
    page = request.GET.get('page')
    items_per_page = str2int(request.GET.get('items', 20), 20)
    post_objects = posts_models.Post.objects.all().order_by('-create_date')

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

    return render(request, 'posts/index.html', context=context)
