from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', views.main, name='main'),
    url(r'^templates/(?P<template>\w+)$', views.templates),
)


