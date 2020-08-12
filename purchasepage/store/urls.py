from django.urls import path
from . import views



urlpatterns = [
    path('',views.pmainpage,name='pmainpage'),
    path ('ProductView/',views.ProductView.as_view()),
    path('Description/<int:id>/',views.Description,name='Description'),
    path('Landing/', views.Landingpage,name='Landingpage'),
]
