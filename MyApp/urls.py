from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('employee', EmployeeViewSet)
router.register('manager', ManagerViewSet)
router.register('vecation', VecationViewSet)
router.register('brawing', BrawingViewSet)

urlpatterns = [
    path('', include(router.urls))
]