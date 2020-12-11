from django.urls import path
from announce.views import AnnounceListView,AnnounceDetailView

urlpatterns = [
    path('',AnnounceListView.as_view()),
    path('<int:pk>', AnnounceDetailView.as_view()),
]