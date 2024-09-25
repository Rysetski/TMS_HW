from django.urls import path
from .views import category, edit_category, delete_category, CreateCategory

urlpatterns = [
    path('category/', category, name="category"),
    path('category/edit/<int:c_id>', edit_category, name="edit_category"),
    path('category/delete/<int:c_id>', delete_category, name="delete_category"),
    path('category/create', CreateCategory.as_view(), name="create_category"),
]