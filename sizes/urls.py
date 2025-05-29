from django.urls import path
from sizes.views import SizeListCreateView, SizeUpdateView, SizeDeleteView


urlpatterns = [
    path('size/', SizeListCreateView.as_view(), name='size_list_view'),
    path('size/update/<int:pk>/', SizeUpdateView.as_view(), name='size_update_view'),
    path('size/delete/<int:pk>/', SizeDeleteView.as_view(), name='size_delete_view'),
]
