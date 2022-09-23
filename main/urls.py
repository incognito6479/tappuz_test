from django.urls import include, path
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register(r'department', views.DepartmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.AuthApiView.as_view())
]
