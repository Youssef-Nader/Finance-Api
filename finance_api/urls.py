# finance_api.urls/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('api/transactions', TransactionList.as_view(), name='transaction-list'),
    path('api/transactions/<int:pk>/', TransactionDetail.as_view(), name='transaction-detail'),
    path('api/users', UserList.as_view(), name='user-list'),
    path('api/users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    # path('api/users/<int:user_id>/transactions/', UserTransactionsView.as_view(), name='user-detail'),
    # path('api/reports/', UserandTransactionView.as_view(), name='user-reports-transactions'),
]