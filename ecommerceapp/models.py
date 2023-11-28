from django.db import models

# Create your models here.
# name
# phone number
# email
# profile picture upload
# company name
# company details
class sellerreg(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField()
    pic=models.FileField(upload_to='ecommerceapp/static')
    cname=models.CharField(max_length=30)
    cdetail=models.CharField(max_length=250)
    password=models.CharField(max_length=15)

    def __str__(self):
        return self.name

class seller_file(models.Model):
    brand=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    photo=models.FileField(upload_to='ecommerceapp/static')
    price=models.IntegerField()
    available=[
        ('Silver','Silver'),
        ('Gold',"Gold"),
        ('RoseGold',"RoseGold"),
        ('Black',"Black")
    ]
    colors=models.CharField(max_length=15,choices=available)
    quantity=models.IntegerField()
    choice=[
        ('Men',"Men"),
        ('Women',"Women"),
        ('Kids',"Kids")
    ]
    category=models.CharField(max_length=30,choices=choice)
    description=models.CharField(max_length=250)
    def __str__(self):
         return self.brand
class buyerreg(models.Model):
    pic=models.FileField(upload_to='ecommerceapp/static')
    name=models.CharField(max_length=50)
    phone=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=200)
    loc=models.CharField(max_length=50)
    password=models.CharField(max_length=15)
    def __str__(self):
        return self.name

class buyer_wishlist(models.Model):
    userid=models.IntegerField()
    prod_id=models.IntegerField()
    brand=models.CharField(max_length=50)
    product_name=models.CharField(max_length=30)
    picture=models.FileField()
    price=models.IntegerField()
    category=models.CharField(max_length=30)
    desc=models.CharField(max_length=200)
    def __str__(self):
        return self.product_name

class add_cart(models.Model):
    userid=models.IntegerField()
    prod_id=models.IntegerField()
    pic=models.FileField()
    brand=models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    quantity=models.IntegerField()
    price=models.IntegerField()
    category=models.CharField(max_length=20)


    def __str__(self):
        return self.name

class address_change(models.Model):
    userid=models.IntegerField()
    name=models.CharField(max_length=20)
    daddress=models.CharField(max_length=100)
    choice=[
        ('Kerala',"Kerala"),
        ('Tamilnadu',"Tamilnadu"),
        ('Karnataka',"Karnataka")
    ]
    state=models.CharField(max_length=20,choices=choice)
    city=models.CharField(max_length=20)
    houseno=models.CharField(max_length=20)
    landmark=models.CharField(max_length=30)
    pincode=models.IntegerField()
    phn=models.IntegerField()
    alt_phn=models.IntegerField()

    # def __str__(self):
    #     return self.name


class order_confirm(models.Model):
    userid=models.IntegerField()
    address=models.CharField(max_length=500)
    imgg=models.FileField()
    prod_details=models.CharField(max_length=500)
    total=models.IntegerField()
    order_date=models.DateField(auto_now_add=True)
    esimated_date=models.DateField()