from django.urls import path, include
from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('category', views.CategoryViewSet)


urlpatterns = [
    path("category/", views.CategoryListCreateAPIView.as_view()),
    path("items/", views.ItemListCreateAPIView.as_view()),
    path("views/items/", views.ItemListCreateView.as_view()),
    path("views/item/<int:pk>/", views.ItemListCreateView.as_view()),

    # path('viewset/category/', views.CategoryViewSet.as_view(
    #     {'get': 'list', 'post': 'create'}
    # )),
    # path('viewset/category/<int:pk>/', views.CategoryViewSet.as_view(
    #     {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    # )),

    path('viewset/', include(router.urls)),
]
