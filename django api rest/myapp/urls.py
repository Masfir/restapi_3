from django.urls import path
from myapp import views

urlpatterns =[
    
    path('BlogList/', views.BlogList.as_view()),
    path('ApiDetail/<int:pk>/', views.ApiDetail.as_view()),
]