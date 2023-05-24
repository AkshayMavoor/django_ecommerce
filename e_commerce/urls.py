from django.urls import path
from .views import E_product,Checkout
from .views import AddProduct
from .views import cart_update
from .views import ProductTable
from .views import DeleteProductView
from .views import UpdateProductView


urlpatterns = [
    
    path('e_product/', E_product.as_view(), name="e_product"),
    path('checkout/', Checkout.as_view(), name="check_out"),
    path('addProducts/',AddProduct.as_view(), name="addProducts"),
    path('cart_update/', cart_update, name="cart_update"),
    path('productTable/',ProductTable.as_view(), name="ProductTable"),
    path('delete/<int:id>/',DeleteProductView.as_view(), name="delete"),
    path('updateProduct/<int:id>/', UpdateProductView.as_view(), name="updateProduct"),
    
]