from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>/", views.details ,name='details'),
    # ex: / polls/5/results/
    #path("<int:inorte_id>/", views.results, name='results'),
    # ex: /polls/5/vote/
    #path ("<int:inoarte_id>/vote/", views.vote, name="vote"),
    path("<int:id>/", views.usuários ,name='usuários'),
    # ex: / polls/5/results/
    #path("<int:inorte_id>/", views.results, name='results'),
    # ex: /polls/5/vote/
    #path ("<int:inoarte_id>/vote/", views.vote, name="vote"),
]