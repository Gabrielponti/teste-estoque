from django.urls import path
from color.views import ColorListView, ColorUpdateView, ColorDeleteView

urlpatterns = [
    path("color/", ColorListView.as_view(), name="color_list_view"),
    path("color/update/<int:pk>/", ColorUpdateView.as_view(), name="color_update_view"),
    path("color/delete/<int:pk>/", ColorDeleteView.as_view(), name="color_delete_view"),
]