from django.urls import path
from .views import FoodDetailView, FoodListView, FoodCreateView, FoodUpdateView, FoodDeleteView

app_name = 'foods'

urlpatterns = [
    path('', FoodListView.as_view(), name='food-list'),
    path('<int:pk>/', FoodDetailView.as_view(), name='food-detail'),
    path('create/', FoodCreateView.as_view(), name='food-create'),
    path('<int:pk>/update/', FoodUpdateView.as_view(), name='food-update'),
    path('<int:pk>/delete/', FoodDeleteView.as_view(), name='food-delete')
]