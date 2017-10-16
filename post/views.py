from django.shortcuts import render


def post_index_page(request):
    return render(request, 'post/index.html')
