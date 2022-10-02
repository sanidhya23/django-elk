from django.urls import path
from base_app import views

app_name = 'base_app'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('health/', views.HealthStatusView.as_view(), name='health-status'),
    path('add_city', views.CityAddView.as_view(), name='add-city'),
    path('list_city', views.CityListView.as_view(), name='list-city'),
]
