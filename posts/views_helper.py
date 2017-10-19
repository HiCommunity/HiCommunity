# coding=utf-8
from posts import models as posts_models
from posts.exception import RegionOrBoardNotExist


def region_and_board_context(region, board):
    # add current region and board information
    context = dict()
    regions = posts_models.Region.objects.all()
    # context['regions'] = regions
    try:
        context['current_region'] = regions.get(address=region)
        if board:
            context['current_board'] = posts_models.Board.objects.get(address=board)
        else:
            context['current_board'] = regions.get(address=region)
    except Exception as e:
        print(str(e))
        raise RegionOrBoardNotExist
    return context
