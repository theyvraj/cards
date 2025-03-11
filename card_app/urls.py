from django.urls import path
from .views import CardListView, CardDetailView

urlpatterns = [
    path('', CardListView.as_view(), name='card_list'),
    path('card/<int:pk>/', CardDetailView.as_view(), name='card_detail'),
]