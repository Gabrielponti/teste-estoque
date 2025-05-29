from django.urls import path
from stocks.views import StockBaseView, StockCreateView, StockListView, StockUpdateView,StockDetailView, StockDeleteView


urlpatterns = [
    path('', StockBaseView.as_view(), name='StockBaseView'),
    path('stock/', StockListView.as_view(), name='stock_list_view'),
    path('stock/new/', StockCreateView.as_view(), name='stock_create_view'),
    path('stock/update/<int:pk>/', StockUpdateView.as_view(), name='stock_update_view'),
    path('stock/detail/<int:pk>/', StockDetailView.as_view(), name='stock_detail_view'),
    path('stock/delete/<int:pk>/', StockDeleteView.as_view(), name='stock_delete_view'),
]
