from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Transaction
from rest_framework import generics 
from .serializers import *
from django.contrib.auth.models import User
# Create your views here.

# All transactions
class TransactionList(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# Single transaction with ID
class TransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

# Return all users with their information
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

#Return each user with information
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Return transactions to each user through user_id
# class UserDetail(generics.RetrieveAPIView):            
#     if User.objects.all().filter(username='AliOsman'):
#         queryset = Transaction.objects.all().filter(user_id=1)
#         serializer_class = UserSerializer
#     elif User.objects.all().filter(username='MohamedAbdo'):    
#         queryset = Transaction.objects.all().filter(user_id=2)
#         serializer_class = UserSerializer
#     elif User.objects.all().filter(username='MohamedYasser'):
#         queryset = Transaction.objects.all().filter(user_id=3)
#         serializer_class = UserSerializer



    


#All users with the transactions in reports
# class UserandTransactionView(generics.ListAPIView):
#     def get(self, request):
#         transactions = Transaction.objects.all()
#         total=[]
#         data1= []
#         for transaction in transactions:
#             data1.append({
#                 'transaction_date': transaction.transaction_date,
#                 'transaction_description': transaction.transaction_description,
#                 'transaction_amount': transaction.transaction_amount,
#                 'user_id': transaction.user_id
#             })
#         users = User.objects.all()
#         data2 = []
#         for user in users:
#             data2.append({
#                 'id': user.id,
#                 'username': user.username,
#                 'email': user.email
#             })
#         total.append(data1 + data2)
#         return Response(total)