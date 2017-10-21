# coding=utf-8
from questions import models as questions_models
from questions.exception import RegionOrBoardNotExist


def region_and_board_context(region, board):
    # add current region and board information
    context = dict()
    regions = questions_models.Region.objects.all()
    # context['regions'] = regions
    try:
        context['current_region'] = regions.get(address=region)
        context['current_board'] = questions_models.Board.objects.get(address=board)
    except Exception as e:
        print(str(e))
        raise RegionOrBoardNotExist
    return context
