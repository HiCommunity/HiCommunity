# coding=utf-8
import time
import os
from users.constants.common import Media
from common.utils.image_ import Avatar

__all__ = [
    'generate_avatar'
]

Avatar = Avatar()


def generate_avatar(account_id):
    timestamp = str(int(time.time()))
    avatar_path = Media.USERS_AVATAR_PATH % account_id
    avatar_url = Media.USERS_AVATAR_URL % account_id
    avatar_url = avatar_url
    avatar_size = 256
    avatar_name = '%s_%dx%d.jpg' % (timestamp, avatar_size, avatar_size)
    avatar = os.path.join(avatar_url, avatar_name).replace('\\', '/')
    big_size = 100
    big_name = '%s_%dx%d.jpg' % (timestamp, big_size, big_size)
    small_size = 40
    small_name = '%s_%dx%d.jpg' % (timestamp, small_size, small_size)
    thumb_big = os.path.join(avatar_url, big_name).replace('\\', '/')
    thumb_small = os.path.join(avatar_url, small_name).replace('\\', '/')
    _path = Avatar.generate_avatar(avatar_path, avatar_name,
                                   size=avatar_size)
    Avatar.generate_thumb(_path, big_size, fn=big_name)
    Avatar.generate_thumb(_path, small_size, fn=small_name)
    return avatar, thumb_big, thumb_small

