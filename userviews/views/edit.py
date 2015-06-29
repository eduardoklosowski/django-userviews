# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Eduardo Klosowski
# License: MIT (see LICENSE for details)
#

from __future__ import unicode_literals

from django.views.generic import CreateView, UpdateView, DeleteView

from .base import FilterUserMixin, SetSharedMixin, SetUserMixin, SharedMixin


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


# Shared Object

class SharedUserCreateView(SetSharedMixin, SharedMixin, UserCreateView):
    """
    Rendeniza uma view para criação de objeto relacionado ao objeto compartilhado pela `pk`.

    - A view deve ter:
    get_shared_model
    get_context_shared_name
    get_shared_field
    """


class SharedUserUpdateView(SharedMixin, UserUpdateView):
    """
    Rendeniza uma view para atualização de objeto relacionado ao objeto compartilhado.

    get_shared_field
    """


class SharedUserDeleteView(SharedMixin, UserDeleteView):
    """
    Rendeniza uma view para deletar um objeto relacionado ao objeto compartilhado.

    get_shared_field
    """
