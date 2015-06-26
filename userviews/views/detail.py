# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Eduardo Klosowski
# License: MIT (see LICENSE for details)
#

from __future__ import unicode_literals

from django.views.generic import DetailView

from .base import FilterUserMixin


class UserDetailView(FilterUserMixin, DetailView):
    """
    Rendeniza uma view detalhada de um objeto.

    O objeto deve estar associado ao usuário retornado
    pela função `self.get_user()`.
    """
