from . import views
from django.urls import path

urlpatterns = [
    path('trans',views.transaction,name='trans'),
    path('payment',views.payment,name='payment'),
]