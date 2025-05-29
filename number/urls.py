from django.urls import path
from number.views import NumberListView, NumberUpdateView ,NumberDeleteView


urlpatterns = [
    path('number/', NumberListView.as_view(), name='number_list_view'),
    path('number/update/<int:pk>/', NumberUpdateView.as_view(), name='number_update_view'),
    path('number/delete/<int:pk>/', NumberDeleteView.as_view(), name='number_delete_view'),
]
