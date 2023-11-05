from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'my_app'
router = DefaultRouter()
router.register('items', views.ItemViewSet, basename="item-viewset")

urlpatterns = [
    path('', views.index, name='index'),
    # path('items/', views.ItemAPIView.as_view(), name='item-view'),
]
urlpatterns += [path(r'api/', include(router.urls))]