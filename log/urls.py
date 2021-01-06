from django.urls import path
from .views import *

urlpatterns = [
    path('', LogList.as_view(), name='log_list'),
    path('create/', LogCreate.as_view(), name='log_create'),
    path('<int:pk>/', LogView.as_view(), name='log_view'),
    path('<int:pk>/reply/', LogReply.as_view(), name='log_reply'),
]
