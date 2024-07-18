from django.urls import path
from calculator.views import recipes_views, DATA

urlpatterns = [
    path('<dish_name>/', recipes_views, {'data': DATA}),
]