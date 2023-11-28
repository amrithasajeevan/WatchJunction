from django.contrib import admin

# Register your models here.
from  .models import *
admin.site.register(sellerreg)
admin.site.register(seller_file)
admin.site.register(buyerreg)
admin.site.register(buyer_wishlist)
admin.site.register(add_cart)
admin.site.register(address_change)
admin.site.register(order_confirm)