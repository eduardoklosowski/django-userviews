# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Eduardo Klosowski
# License: MIT (see LICENSE for details)
#

from .detail import UserDetailView, SharedUserDetailView
from .edit import (UserCreateView, UserUpdateView, UserDeleteView,
                   SharedUserCreateView, SharedUserUpdateView, SharedUserDeleteView)
from .list import UserListView


__all__ = [
    'UserDetailView', 'SharedUserDetailView'
    'UserCreateView', 'UserUpdateView', 'UserDeleteView',
    'SharedUserCreateView', 'SharedUserUpdateView', 'SharedUserDeleteView',
    'UserListView',
]
