from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_view),
    path('products/<int:id>/', views.review_view),
    path('products/', views.product_view),



]
