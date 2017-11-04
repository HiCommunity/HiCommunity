# coding=utf-8
from HiCommunity.settings import MEDIA_ROOT, MEDIA_URL
import os

__all__ = [
    'SESSION_LOGIN_USER',
    'Media'
]

# Session
SESSION_LOGIN_USER = 'login_user'


class Media(object):
    """
    Users Media constants
    """

    USERS_DIR = 'users'
    AVATAR_DIR = 'avatar'
    # DEFAULT_AVATAR_URL = os.path.join(MEDIA_URL, USERS_DIR, 'default', 'avatar')
    USERS_PATH = os.path.join(MEDIA_ROOT, USERS_DIR, '%s')
    USERS_URL = os.path.join(MEDIA_URL, USERS_DIR, '%s')
    USERS_AVATAR_PATH = os.path.join(USERS_PATH, AVATAR_DIR)
    USERS_AVATAR_URL = os.path.join(USERS_URL, AVATAR_DIR)
