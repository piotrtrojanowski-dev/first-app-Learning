"""Defines patters URL for learning_log. """

from django.urls import path
from .views import EntryDeleteView, TopicDeleteView

from . import views

urlpatterns = [
    #Home
    path('', views.index, name='index'),
    #List of topics
    path("topics/", views.topics, name='topics'),
    #Single topic
    path("topics/<int:pk>/", views.topic, name='topic'),
    #New topic
    path("new-topic/", views.new_topic, name='new_topic'),
    #New entry
    path("topics/<int:pk>/new-entry/", views.new_entry, name='new_entry'),
    #Edit entry
    path("edit_entry/<int:pk>/", views.edit_entry, name='edit_entry'),
    #Delete entry
    path('topics/<int:pk>/delete-entry/', EntryDeleteView.as_view(), name='delete_entry'),
    #Delete topic
    path('topics/<int:pk>/delete-topic/', TopicDeleteView.as_view(), name='delete_topic'),
]