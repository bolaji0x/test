from django.urls import path

from .views import (
    NoteListView,
    NoteDetailView,
    NoteCreateView,
    NoteUpdateView,
    NoteDeleteView
)

app_name = 'notes'
urlpatterns = [
    path('', NoteListView.as_view(), name='note-list'),
    path('<int:id>/', NoteDetailView.as_view(), name='note-detail'),
    path('create/', NoteCreateView.as_view(), name='note-create'),
    path('<int:id>/update/', NoteUpdateView.as_view(),name='note-create'),
    path('<int:id>/delete/', NoteDeleteView.as_view(), name='note-delete')
]


