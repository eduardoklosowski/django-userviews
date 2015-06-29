# -*- coding: utf-8 -*-
#
# Copyright (c) 2015 Eduardo Klosowski
# License: MIT (see LICENSE for details)
#

from __future__ import unicode_literals

from django.http import Http404


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


# Shared Object

class SharedObjectException(Exception):
    """
    Exceção para implementação incorretas do objeto compartilhado
    """


class SharedMixin(object):
    """
    Mixin que define o objeto compartilhado na view.
    """
    shared_model = None
    shared_field = None
    context_shared_name = None

    def get_shared_field(self):
        """
        Retorna uma string com o nome do campo do objeto compartilhado.
        Este campo deve ser um ForeignKey.

        Caso não seja informado, o valor padrão é o `model_name` do `self.shared_model`.
        """
        shared_field = self.shared_field
        if shared_field:
            return shared_field
        return self.shared_model._meta.model_name

    def get_context_shared_name(self):
        """
        Retorna uma string com o nome da variável do objeto compartilhado no template.
        """
        context_shared_name = self.context_shared_name
        if context_shared_name:
            return context_shared_name

        shared_field = self.get_shared_field()
        return shared_field

    def get_shared_object(self):
        """
        Busca o objeto compartilhado no banco.
        """
        if self.object:
            shared_field = self.get_shared_field()
            shared_object = getattr(self.object, shared_field)
        else:
            queryset = self.shared_model._default_manager
            pk = self.kwargs.get(self.pk_url_kwarg, None)
            slug = self.kwargs.get(self.slug_url_kwarg, None)
            if pk is not None:
                queryset = queryset.filter(pk=pk)
            if slug is not None and (pk is None or self.query_pk_and_slug):
                slug_field = self.get_slug_field()
                queryset = queryset.filter(**{slug_field: slug})
            if pk is None and slug is None:
                raise SharedObjectException('A view %s deve receber como parâmetro pk ou slug.' %
                                            self.__class__.__name__)
            try:
                shared_object = queryset.get()
            except queryset.model.DoesNotExist:
                raise Http404('%s não encontrado' % queryset.model._meta.verbose_name)
        return shared_object

    def get_object(self, queryset=None):
        """
        Busca o objeto do usuário pelo objeto compartilhado.
        """
        if queryset is None:
            queryset = self.get_queryset()
        shared_field = self.get_shared_field()
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        slug = self.kwargs.get(self.slug_url_kwarg, None)
        if pk is not None:
            queryset = queryset.filter(**{'%s__pk' % shared_field: pk})
        if slug is not None and (pk is None or self.query_pk_and_slug):
            slug_field = self.get_slug_field()
            queryset = queryset.filter(**{'%s__%s' % (shared_field, slug_field): slug})
        if pk is None and slug is None:
            raise SharedObjectException('A view %s deve receber como parâmetro pk ou slug.' % self.__class__.__name__)
        try:
            obj = queryset.get()
        except queryset.model.DoesNotExist:
            raise Http404('%s não encontrado' % queryset.model._meta.verbose_name)
        return obj

    def get_context_data(self, **kwargs):
        """
        Adicionado o objeto compartilhado ao contexto do template.
        """
        shared_object = self.get_shared_object()
        context_shared_name = self.get_context_shared_name()

        context = super(SharedMixin, self).get_context_data(**kwargs)
        context['shared_object'] = shared_object
        context[context_shared_name] = shared_object
        return context


class SetSharedMixin(SharedMixin):
    """
    Mixin para definir a PrimaryKey do objeto compartilhado no campo do POST.
    """

    def post(self, request, *args, **kwargs):
        """
        Adicionado a PrimaryKey do objeto no campo `self.get_shared_field()` do POST.
        """
        shared_field = self.get_shared_field()
        post = request.POST.copy()
        post[shared_field] = kwargs['pk']
        request.POST = post
        return super(SetSharedMixin, self).post(request, *args, **kwargs)
