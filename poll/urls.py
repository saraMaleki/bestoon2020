from django.urls import path
from . import views

urlpatterns = [
    path('submit/expense/', views.Submit_Expense, name='Submit_Expense'),
    path('submit/income/', views.Submit_Income, name='Submit_Income'),
]