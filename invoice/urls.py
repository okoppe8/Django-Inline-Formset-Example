from django.urls import path

from invoice import views

urlpatterns = [
    path('', views.InvoiceFilterView.as_view(), name='index'),
    path('detail/<int:pk>/', views.InvoiceDetailView.as_view(), name='detail'),
    path('create/', views.InvoiceCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.InvoiceUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.InvoiceDeleteView.as_view(), name='delete'),
]
