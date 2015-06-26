# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Eduardo Klosowski
# License: MIT (see LICENSE for details)
#

from __future__ import unicode_literals

from django.views.generic import CreateView, UpdateView, DeleteView

from .base import FilterUserMixin, SetUserMixin


class UserCreateView(SetUserMixin, CreateView):
    """
    Rendeniza uma view de criação de objeto.

    Adiciona a PrimaryKey do usuário retornado pala função `self.get_user()`
    como o campo `self.get_user_field()` do POST.
    """


class UserUpdateView(FilterUserMixin, UpdateView):
    """
    Rendeniza uma view de atualização de objeto.

    O objeto deve estar associado ao usuário retornado
    pela função `self.get_user()`.
    """


class UserDeleteView(FilterUserMixin, DeleteView):
    """
    Rendeniza uma view para deletar um objeto.

    O objeto deve estar associado ao usuário retornado
    pela função `self.get_user()`.
    """
