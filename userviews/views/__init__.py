# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Eduardo Klosowski
# License: MIT (see LICENSE for details)
#

from .detail import UserDetailView
from .edit import UserCreateView, UserUpdateView, UserDeleteView
from .list import UserListView


__all__ = [
    'UserDetailView',
    'UserCreateView', 'UserUpdateView', 'UserDeleteView',
    'UserListView',
]
