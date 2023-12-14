from django.urls import path

from .import views


app_name = "Polls"
urlpatterns = [
    # ex: /Polls/
    path("",views.IndexView.as_view(),name="index"),
    # ex: /Polls/5/
    path("<int:pk>/",views.DetailView.as_view(),name='detail'),
    # ex /Polls/5/results/
    path("<int:pk>/results/",views.ResultsView.as_view(),name="results"),
    # ex: /Polls/5/vote/
    path("<int:question_id>/vote/",views.vote,name="vote"),
]