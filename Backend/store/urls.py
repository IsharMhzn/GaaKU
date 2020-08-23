from django.urls import path
from . import views



urlpatterns = [
    path('',views.pmainpage.as_view(),name='pmainpage'),
<<<<<<< HEAD
    path('Description/<int:pk>/',views.Description.as_view(),name='Description'),
    path('Landing/', views.Landingpage,name='Landingpage'),
    path('<category>',views.category,name='category'),
    path('search/',views.search,name='search'),
    path('add_to_whishlist/<int:pk>/',views.add_to_whishlist,name='add_to_whishlist'),
=======
    path('Description/<int:pk>/',views.Description,name='Description'),
    path('Landing/', views.Landingpage,name='Landingpage'),
    path('<category>',views.category,name='category'),
    path('search/',views.search,name='search'),
    path('comment/show', views.commentview, name='comment')
>>>>>>> 30a2ec9e1ea3663a0841d91595d1edda7cfaeee6
]
