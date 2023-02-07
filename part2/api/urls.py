from django.urls import include, path
from . import views


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('images/', views.images),
    path('image_meta/<int:pk>/', views.image_meta),
    path('download/<int:pk>/', views.download_image),
]