"""
apppppppppppppppppppppppps urls
"""
from django.contrib import admin
from django.urls import path
from base import views
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path('', views.index),
    path('books/', views.Books),
    path('books/<int:id>',views.Books),
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair')

]
