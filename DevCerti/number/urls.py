"""
TODO DOC
"""
from django.urls import re_path
from number import views as nview

urlpatterns = [
    re_path(r'^[-]\d{1,5}', nview.Numberify.as_view(), {'sign':-1}),
    re_path(r'^\d{1,5}', nview.Numberify.as_view(), {'sign':1}),
]
