from django.urls import path
from . import views
from rest_framework.documentation import include_docs_urls


urlpatterns = [
    path('vendors/', views.VendorListCreate.as_view()),
    path('vendors/<int:pk>/', views.VendorRetrieveUpdateDestroy.as_view()),
    path('purchase_orders/', views.PurchaseOrderListCreate.as_view()),
    path('purchase_orders/<int:pk>/', views.PurchaseOrderRetrieveUpdateDestroy.as_view()),
    path('vendors/<int:pk>/performance/', views.VendorPerformance.as_view()),
    path('purchase_orders/<int:pk>/acknowledge/', views.AcknowledgePurchaseOrder.as_view()),
    path('docs/', include_docs_urls(title='Vendor Management System API')),

]
