from django.urls import path
from rest_framework import routers
from . import views

router = routers.SimpleRouter()
router.register('emails', views.EmailViewSet)

urlpatterns = [
    path('analytics/', views.RetrieveDayAnalytics.as_view()),
]

urlpatterns+=router.urls