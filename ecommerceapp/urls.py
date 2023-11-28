from django.urls import path
from .views import *
urlpatterns=[
    path('indexpage/',index),
    path('sellerlogin/',sellerlog),
    path('sellerregister/',seller_reg),
    path('sellerfileupload/',seller_fileupload),
    path('editseller/',edit_file),
    path('sellerprofile/',seller_profile),
    path('editsellerprofile/<int:id>',seller_profileedit),
    path('seller_products/',seller_productview),
    path('selleredit_product/<int:id>',edit_sellerproduct),
    path('buyerregister/',buyer_register),
    path('buyerlogin/',buyerlogin),
    path('buyerprofile/',buyer_profile),
    path('menproducts/',men_product),
    path('womenproducts/',women_product),
    path('kidsproducts/',kids_product),
    path('wishlist/<int:id>',whishlist),
    path('wishlistdisplay/',display_whishlist),
    path('deletewishlist/<int:id>',whishlist_delete),
    path('addtocart/<int:id>',add_to_cart),
    path('addtocart_display/',addtocart_display),
    path('deletecarts/<int:id>',cart_delete),
    path('buyerlogout/', logout_view),
    path('cartinc/<int:id>',cart_increment),
    path('cartdec/<int:id>',cart_decrement),
    path('orderedaddress/',delivery_address),
    path('viewaddress/',address_display),
    path('edit_address/<int:id>',address_edit),
    path('delete_address/<int:id>',address_delete),
    path('add_another_add/',add_another_address),
    path('proceedtopay/',proceed_to_payment),
    path('confirmation/',confirm_payemnt),
    path('previewdisplay/',preview_display),
    # path('select_address/', select_address)


]