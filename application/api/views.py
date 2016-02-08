# -*- coding: utf-8 -*-
from rest_framework.views import APIView
from rest_framework import viewsets
from application.api.models import Store, Article
from application.api.serializers import StoreSerializer, ArticleSerializer
from rest_framework.serializers import ValidationError
from rest_framework import exceptions
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.response import Response


class list_formatted(object):

    def __init__(self, results_key, not_found_exception=False):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print("Inside __init__()")
        self.results_key = results_key
        self.not_found_exception = not_found_exception

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        print("Inside __call__()")

        def wrapped_f(*args, **kwargs):
            print("Inside wrapped_f()")
            print("Decorator arguments:", self.results_key)

            if not args[1].user.is_authenticated():
                raise exceptions.NotAuthenticated()

            results = f(*args)
            total_elements = len(results)
            main_key = getattr(self.results_key.Meta, 'model')._meta
            if self.not_found_exception and total_elements == 0:
                raise exceptions.NotFound()
            elif total_elements == 1:
                main_key = main_key.verbose_name
                results = results[0]
            else:
                main_key = main_key.verbose_name_plural

            return Response({
                main_key.title().lower(): results,
                'total_elements': total_elements,
                'success': True
            })
        return wrapped_f


class ErrorView(APIView):

    def get(self, request):
        '''
        Exception for NotFound URLs.
        '''
        raise exceptions.NotFound()


class ArticleViewSet(viewsets.ModelViewSet):
    """
    Viewset for Article model.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    @list_formatted(serializer_class)
    def list(self, request):
        serializer = StoreViewSet.serializer_class(StoreViewSet.queryset, many=True)
        return serializer.data


class StoreViewSet(viewsets.ModelViewSet):
    """
    Viewset for Store model.
    """

    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    @list_formatted(serializer_class)
    def list(self, request):
        serializer = StoreViewSet.serializer_class(StoreViewSet.queryset, many=True)
        return serializer.data


class ArticleFilterList(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        """
        Return a list of all the articles for
        the store as determined by the store_id portion of the URL.
        """
        store_id = self.kwargs.pop('store_id')
        try:
            return Article.objects.filter(store__id=store_id)
        except Exception as e:
            raise ValidationError({
                'detail': e.message
            })

    @list_formatted(serializer_class, not_found_exception=True)
    def list(self, request):
        """
        Return a serialized list of all the filtered articles for
        the store.
        """
        serializer = ArticleFilterList.serializer_class(self.get_queryset(), many=True)
        return serializer.data

