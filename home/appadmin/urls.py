from django.urls import path
from .views import details_view

urlpatterns = [
    # Your other URL patterns
    path('details/', details_view, name='details_view'),
]
