# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Eduardo Klosowski
# License: MIT (see LICENSE for details)
#

from __future__ import unicode_literals


class GetUserMixin(object):
    """
    Mixin para selecionar o usuário que será utilizado.
    """

    def get_user(self):
        """
        Retorna o objeto do usuário.

        Por padrão seleciona o usuário em `self.request.user`.
        """
        return self.request.user


class UserFieldMixin(object):
    """
    Mixin para definir o campo do usuário.
    """
    user_field = 'user'

    def get_user_field(self):
        """
        Retorna uma string com o nome do campo do usuário.
        """
        return self.user_field


class FilterUserMixin(GetUserMixin, UserFieldMixin):
    """
    Mixin para filtrar o usuário no QuerySet.
    """

    def get_queryset(self):
        """
        Retorna o QuerySet com o filtro pelo usuário.
        """
        queryset = super(FilterUserMixin, self).get_queryset()
        queryset_filter = {self.get_user_field(): self.get_user()}
        return queryset.filter(**queryset_filter)


class SetUserMixin(GetUserMixin, UserFieldMixin):
    """
    Mixin para definir a PrimaryKey do usuário no campo POST.
    """

    def post(self, request, *args, **kwargs):
        """
        Adicionado a PrimaryKey do usuário no campo `self.get_user_field()` do POST.
        """
        post = request.POST.copy()
        post[self.get_user_field()] = self.get_user().pk
        request.POST = post
        return super(SetUserMixin, self).post(request, *args, **kwargs)
