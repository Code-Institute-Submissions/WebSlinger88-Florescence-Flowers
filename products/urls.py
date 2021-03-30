from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product,
         name='delete_product'),
    path('add_review/<int:product_id>/', views.add_review, name='add_review'),
    path('update_review/<int:review_id>/<int:rating_id>/', views.update_review,
         name='update_review'),
    path('delete_review/<int:review_id>/', views.delete_review,
         name='delete_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
