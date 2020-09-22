from django.urls import path
from . import views



urlpatterns = [
    path('',views.pmainpage.as_view(),name='pmainpage'),
    path('pdescription/<int:pk>/',views.pdescription,name='pdescription'),
    path('Landing/', views.Landingpage,name='Landingpage'),
    path('<category>',views.category,name='category'),
    path('search/',views.search,name='search'),
    path('add_to_whishlist/<int:pk>/',views.add_to_whishlist,name='add_to_whishlist'),
    path('comment/show', views.commentview, name='comment'),
    path('notify/me', views.lookingfor, name='lookingfor')
]
