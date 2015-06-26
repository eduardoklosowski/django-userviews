# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Eduardo Klosowski
# License: MIT (see LICENSE for details)
#

from __future__ import unicode_literals

from django.views.generic import ListView

from .base import FilterUserMixin


class UserListView(FilterUserMixin, ListView):
    """
    Rendeniza uma view listando objetos.

    Os objectos devem estar associados ao usuário retornados
    pela função `self.get_user()`.
    """
