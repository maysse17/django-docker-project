import os
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from board.views import CreateBoardView
from board.views import ShowBoardsView
from board.views import ListBoardsView


urlpatterns = [
    path('create/', CreateBoardView.as_view(), name='create'),
    path('show', ShowBoardsView.as_view(), name='show'),
    path('ajax/boards', ListBoardsView.as_view(), name='boards_list'),
]

if settings.DEBUG:
    static_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static', 'borad'))
    urlpatterns += static(settings.STATIC_URL + 'board/', document_root=static_folder)
