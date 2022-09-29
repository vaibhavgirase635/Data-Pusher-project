
from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Account import views

router=DefaultRouter()

router.register('accountapi',views.MyaccountView,basename='account')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/',include('rest_framework.urls',namespace='rest_framework')),
]
