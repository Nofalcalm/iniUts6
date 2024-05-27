from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'Merekmotor', views.MerekmotorViewSet)
router.register(r'Order', views.OrderViewSet)
router.register(r'Produk', views.ProdukViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]