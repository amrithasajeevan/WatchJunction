import datetime

from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth import logout
from django.core.mail import send_mail
from ecommercepro.settings import EMAIL_HOST_USER
import ast

# Create your views here.
def index(request):
    return render(request,'index.html')
def sellerlog(request):
    if request.method=='POST':
        email=request.POST.get('eid')
        password=request.POST.get('passw')
        c=sellerreg.objects.all()
        for i in c:
            if(i.email==email and i.password==password):
                request.session['id']=i.id#global
                return redirect(seller_profile)
        else:
                return HttpResponse('login failed')

    return render(request,"seller_login.html")
def seller_reg(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phn')
        image=request.FILES.get('img')
        company=request.POST.get('cname')
        details=request.POST.get('cdetails')
        password=request.POST.get('passw')
        cpassword=request.POST.get('cpass')
        if password==cpassword:
            a=sellerreg(name=name,email=email,phone=phone,pic=image,cname=company,cdetail=details,password=password)
            a.save()
            return HttpResponse('register success')
        else:
            return HttpResponse('failed')

    return render(request,'seller_reg.html')

def seller_fileupload(request):
    if request.method=='POST':
        brand=request.POST.get('brand')
        mname=request.POST.get('mname')
        pic=request.FILES.get('pic')
        price=request.POST.get('price')
        colour=request.POST.get('colours')
        quantity=request.POST.get('qty')
        category=request.POST.get('category')
        desc=request.POST.get('desc')

        s=seller_file(brand=brand,name=mname,photo=pic,price=price,colors=colour,quantity=quantity,category=category,description=desc)
        s.save()
        return HttpResponse('product uploaded')

    return render(request,"seller_fileupload.html")
def edit_file(request):

    return render(request,'seller_edit.html')
def seller_profile(request):
    id1=request.session['id']

    a=sellerreg.objects.get(id=id1)
    img = str(a.pic).split('/')[-1]
    return render(request,'seller_profile.html',{'data':a,'img':img})


def seller_profileedit(request,id):

        w=sellerreg.objects.get(id=id)
        image = str(w.pic).split('/')[-1]
        if request.method == 'POST':
            w.name=request.POST.get('name')
            w.email=request.POST.get('email')
            w.phone=request.POST.get('phone')
            if request.FILES.get('image') == None:
                w.save()
            else:
                w.pic = request.FILES['image']
                w.save()
            w.cname=request.POST.get('cname')
            w.cdetail=request.POST.get('cdetail')
            w.save()
            return redirect(seller_profile)
        return render(request,"seller_editprofile.html",{'data':w,'img':image})

def seller_productview(request):
    id=[]
    brand=[]
    mname=[]
    photo=[]
    price=[]
    colour=[]
    quty=[]
    category=[]
    desc=[]
    a=seller_file.objects.all()
    for i in a:
        id1=i.id
        id.append(id1)
        brand1=i.brand
        brand.append(brand1)
        mname1=i.name
        mname.append(mname1)
        pic=str(i.photo).split('/')[-1]
        photo.append(pic)
        price1=i.price
        price.append(price1)
        colour1=i.colors
        colour.append(colour1)
        qty1=i.quantity
        quty.append(qty1)
        cat=i.category
        category.append(cat)
        descr=i.description
        desc.append(descr)

    mylist=zip(id,brand,mname,photo,price,colour,quty,category,desc)
    return render(request,'seller_productdisplay.html',{'data':mylist})

def edit_sellerproduct(request,id):
    e=seller_file.objects.get(id=id)
    image1=str(e.photo).split('/')[-1]
    if request.method=='POST':
        e.brand=request.POST.get('bname')
        e.name=request.POST.get('mname')
        if request.FILES.get('pic') == None:
            e.save()
        else:
            e.photo= request.FILES['pic']
            e.save()
        e.price=request.POST.get('price')
        e.colors=request.POST.get('colors')
        e.quantity=request.POST.get('qty')
        e.category=request.POST.get('cat')
        e.description=request.POST.get('des')
        e.save()
        return redirect(seller_productview)
    return render(request,"edit_products_seller.html",{'data':e,'img':image1})

def buyer_register(request):
    if request.method=='POST':
        img=request.FILES.get('image')
        name=request.POST.get('uname')
        phone=request.POST.get('phn')
        email=request.POST.get('eid')
        address=request.POST.get('add')
        loc=request.POST.get('loc')
        password=request.POST.get('passw')
        cpassword=request.POST.get('cpassw')
        a = buyerreg(pic=img, name=name, phone=phone, email=email, address=address, loc=loc, password=password)
        b=buyerreg.objects.all()
        for i in b:
            if(i.name==name or i.email==email):
                return HttpResponse('this name or emailid already exist use another')
        else:

                if password==cpassword:
                    a.save()
                    subject=f"YOU have created with account {email}"
                    message=f'Hi {name}'
                    email_from = EMAIL_HOST_USER
                    send_mail(subject,message,email_from,[email])
                    return HttpResponse('registration success')
                else:
                    return HttpResponse('failed')

    return render(request,'buyer_register.html')



def buyerlogin(request):
    if request.method=='POST':
        email=request.POST.get('eid')
        password=request.POST.get('passw')
        g=buyerreg.objects.all()
        for i in g:

            if(i.email==email and i.password==password):
                request.session['u_id'] = i.id
                print(request.session['u_id'])
                return redirect('http://127.0.0.1:8000/ecommerceapp/buyerprofile/')
                # return redirect(buyer_profile)
        else:
            return HttpResponse('login failed')

    return render(request,'buyer_login.html')



def buyer_profile(request):
    try:
        id2 = request.session['u_id']
        d = buyerreg.objects.get(id=id2)
        img = str(d.pic).split('/')[-1]
        return render(request, 'buyerprofile.html', {'data': d, 'img': img})
    # print(id2)

    except:
        request.session['u_id']=None
        return redirect(buyerlogin)

def logout_view(request):
    logout(request)

    return redirect(buyerlogin)



def men_product(request):
    id = []
    brand = []
    mname = []
    photo = []
    price = []
    colour = []
    quty = []
    category = []
    desc = []
    a = seller_file.objects.all()
    for i in a:
        id1 = i.id
        id.append(id1)
        brand1 = i.brand
        brand.append(brand1)
        mname1 = i.name
        mname.append(mname1)
        pic = str(i.photo).split('/')[-1]
        photo.append(pic)
        price1 = i.price
        price.append(price1)
        colour1 = i.colors
        colour.append(colour1)
        qty1 = i.quantity
        quty.append(qty1)
        cat = i.category
        category.append(cat)
        descr = i.description
        desc.append(descr)

    mylist = zip(id, brand, mname, photo, price, colour, quty, category, desc)
    return render(request, 'men_product_display.html', {'a': mylist})

def women_product(request):
    id = []
    brand = []
    mname = []
    photo = []
    price = []
    colour = []
    quty = []
    category = []
    desc = []
    a = seller_file.objects.all()
    for i in a:
        id1 = i.id
        id.append(id1)
        brand1 = i.brand
        brand.append(brand1)
        mname1 = i.name
        mname.append(mname1)
        pic = str(i.photo).split('/')[-1]
        photo.append(pic)
        price1 = i.price
        price.append(price1)
        colour1 = i.colors
        colour.append(colour1)
        qty1 = i.quantity
        quty.append(qty1)
        cat = i.category
        category.append(cat)
        descr = i.description
        desc.append(descr)

    womenlist = zip(id, brand, mname, photo, price, colour, quty, category, desc)
    return render(request, 'women_product_display.html', {'b': womenlist})

def kids_product(request):
    id = []
    brand = []
    mname = []
    photo = []
    price = []
    colour = []
    quty = []
    category = []
    desc = []
    a = seller_file.objects.all()
    for i in a:
        id1 = i.id
        id.append(id1)
        brand1 = i.brand
        brand.append(brand1)
        mname1 = i.name
        mname.append(mname1)
        pic = str(i.photo).split('/')[-1]
        photo.append(pic)
        price1 = i.price
        price.append(price1)
        colour1 = i.colors
        colour.append(colour1)
        qty1 = i.quantity
        quty.append(qty1)
        cat = i.category
        category.append(cat)
        descr = i.description
        desc.append(descr)

    kidlist = zip(id, brand, mname, photo, price, colour, quty, category, desc)
    return render(request, 'kids_product_display.html', {'c': kidlist})

def whishlist(request,id):
    a=seller_file.objects.get(id=id)
    print(id)
    id3=request.session['u_id']
    c=buyer_wishlist.objects.all()
    for i in c:
        if id == i.prod_id and id3==i.userid:
            return HttpResponse('item already exist')
    else:
        b=buyer_wishlist(userid=id3,prod_id=a.id,brand=a.brand,product_name=a.name,picture=a.photo,price=a.price,category=a.category,desc=a.description)
        b.save()
        return HttpResponse("item added to wishlist")

def display_whishlist(request):
    id5=request.session['u_id']#login user id
    idd=[]
    userid=[]
    pro_id = []
    brand1 = []
    pname=[]
    pic=[]
    price=[]
    cat=[]
    desc=[]
    s=buyer_wishlist.objects.all()
    for i in s:
        id4=i.id
        idd.append(id4)
        uid=i.userid
        userid.append(uid)
        pro_id1=i.prod_id
        pro_id.append(pro_id1)
        brandd=i.brand
        brand1.append(brandd)
        name=i.product_name
        pname.append(name)
        picc=str(i.picture).split('/')[-1]
        pic.append(picc)
        pri=i.price
        price.append(pri)
        categ=i.category
        cat.append(categ)
        descr=i.desc
        desc.append(descr)
    wish=zip(idd,userid,pro_id,brand1,pname,pic,price,cat,desc)
    return render(request,'wishlist_disp.html',{'data':wish,'userid':id5})

def whishlist_delete(request,id):
    h=buyer_wishlist.objects.get(id=id)
    h.delete()
    return redirect(display_whishlist)

def add_to_cart(request,id):
    cc=seller_file.objects.get(id=id)
    id4=request.session['u_id']
    dd=add_cart.objects.all()
    for i in dd:
        if id==i.prod_id and id4==i.userid:
            i.quantity+=1
            i.price = cc.price * i.quantity
            i.save()
            return redirect('http://127.0.0.1:8000/ecommerceapp/addtocart_display/')
    else:
        count=1
        v=add_cart(userid=id4,prod_id=cc.id,pic=cc.photo,brand=cc.brand,name=cc.name,quantity=count,price=cc.price,category=cc.category)
        v.save()
        return redirect('http://127.0.0.1:8000/ecommerceapp/addtocart_display/')

def  addtocart_display(request):
        id7=request.session['u_id']
        idd=[]
        userid=[]
        pro_id=[]
        pic=[]
        brand=[]
        name=[]
        qty=[]
        price=[]
        cat=[]
        j=add_cart.objects.filter(userid=id7)
        for i in j:
            id3=i.id
            idd.append(id3)
            uid=i.userid
            userid.append(uid)
            proid=i.prod_id
            pro_id.append(proid)
            pic1=str(i.pic).split('/')[-1]
            pic.append(pic1)
            brand1=i.brand
            brand.append(brand1)
            name1=i.name
            name.append(name1)
            qty1=i.quantity
            qty.append(qty1)
            p=i.price
            price.append(p)
            category1=i.category
            cat.append(category1)
        total1=sum(price)
        # Before setting the session variable
        print("Total1 before setting in session:", total1)

        # Set the session variable
        request.session['tprice'] = total1
        print(request.session['tprice'])

        # After setting the session variable
        print("Total1 after setting in session:", request.session.get('tprice'))

        # Later in your code when you access the session variable
        try:
            total_price = request.session['tprice']
            print("Total price from session:", total_price)
        except KeyError:
            print("tprice session variable not found")

        cart=zip(idd,userid,pro_id,pic,brand,name,qty,price,cat)

        return render(request,'addtocart_disp.html',{'data':cart,'userid':id7,'total':total1})

def cart_delete(request,id):
    d=add_cart.objects.get(id=id)
    d.delete()
    return redirect(addtocart_display)

def cart_increment(request,id):

    a=add_cart.objects.get(id=id)
    b=seller_file.objects.get(id=a.prod_id)
    price=b.price

    a.quantity+=1
    a.price=price*a.quantity
    a.save()
    print(price)
    return redirect(addtocart_display)

def cart_decrement(request,id):
    a = add_cart.objects.get(id=id)
    b = seller_file.objects.get(id=a.prod_id)
    price = b.price
    if a.quantity > 0:
        a.quantity -= 1
        a.price = price * a.quantity
        a.save()

    return redirect(addtocart_display)


def delivery_address(request):
    try:
        id8 = request.session['u_id']
        a=address_change.objects.all()
        for i in a:
            if i.userid == id8:
                return redirect('http://127.0.0.1:8000/ecommerceapp/viewaddress/')
        else:
            raise Exception
    except:

        if request.method == 'POST':
                    name = request.POST.get('name')
                    addr = request.POST.get('addr')
                    state = request.POST.get('state')
                    city = request.POST.get('city')
                    houseno = request.POST.get('houseno')
                    landmark = request.POST.get('landmark')
                    pincode = request.POST.get('pincode')
                    phn = request.POST.get('phn')
                    altphn = request.POST.get('altphn')
                    s = address_change(userid=id8, name=name, daddress=addr, state=state, city=city, houseno=houseno,
                                       landmark=landmark, pincode=pincode, phn=phn, alt_phn=altphn)
                    s.save()
                    return redirect(address_display)
    return render(request, 'add_address.html')

def add_another_address(request):
        id8 = request.session['u_id']
        if request.method == 'POST':
                    name = request.POST.get('name')
                    addr = request.POST.get('addr')
                    state = request.POST.get('state')
                    city = request.POST.get('city')
                    houseno = request.POST.get('houseno')
                    landmark = request.POST.get('landmark')
                    pincode = request.POST.get('pincode')
                    phn = request.POST.get('phn')
                    altphn = request.POST.get('altphn')
                    s = address_change(userid=id8, name=name, daddress=addr, state=state, city=city, houseno=houseno,
                                       landmark=landmark, pincode=pincode, phn=phn, alt_phn=altphn)
                    s.save()
                    return redirect(address_display)
        return render(request, 'add_address.html')



# def address_display(request):
#
#     try:
#         id5=request.session['u_id']
#         uid=[]
#         idd=[]
#         name=[]
#         addr=[]
#         st=[]
#         c=[]
#         hno=[]
#         lmark=[]
#         pinc=[]
#         phn=[]
#         aphn=[]
#         a=address_change.objects.all()
#         for i in a:
#             uid1=i.userid
#             uid.append(uid1)
#             id1=i.id
#             idd.append(id1)
#             name1=i.name
#             name.append(name1)
#             addr1=i.daddress
#             addr.append(addr1)
#             st1=i.state
#             st.append(st1)
#             c1=i.city
#             c.append(c1)
#             hno1=i.houseno
#             hno.append(hno1)
#             land=i.landmark
#             lmark.append(land)
#             pinc1=i.pincode
#             pinc.append(pinc1)
#             phn1=i.phn
#             phn.append(phn1)
#             aphn1=i.alt_phn
#             aphn.append(aphn1)
#         address=zip(uid,idd,name,addr,st,c,hno,lmark,pinc,phn,aphn)
#         if request.method == 'POST':
#             a = address_change.objects.get('delivery_addr')
#             request.session['del'] = a
#
#             return redirect(preview_display)
#
#
#         return render(request,'address_display_radio.html',{'data':address,'userid':id5})
#     except:
#         request.session['u_id'] = None
#         return redirect(delivery_address)


def address_display(request):
    try:
        id5 = request.session['u_id']
        uid = []
        idd = []
        name = []
        addr = []
        st = []
        c = []
        hno = []
        lmark = []
        pinc = []
        phn = []
        aphn = []
        a = address_change.objects.all()

        for i in a:
            uid1 = i.userid
            uid.append(uid1)
            id1 = i.id
            idd.append(id1)
            name1 = i.name
            name.append(name1)
            addr1 = i.daddress
            addr.append(addr1)
            st1 = i.state
            st.append(st1)
            c1 = i.city
            c.append(c1)
            hno1 = i.houseno
            hno.append(hno1)
            land = i.landmark
            lmark.append(land)
            pinc1 = i.pincode
            pinc.append(pinc1)
            phn1 = i.phn
            phn.append(phn1)
            aphn1 = i.alt_phn
            aphn.append(aphn1)

        address = zip(uid, idd, name, addr, st, c, hno, lmark, pinc, phn, aphn)

        return render(request, 'address_disp.html', {'data': address, 'userid': id5})
    except:
        request.session['u_id'] = None
        return redirect(delivery_address)



# def select_address(request):
#     id4=request.session['u_id']
#     addresses = address_change.objects.all()
#
#     selected_address = None
#
#     if request.method == 'POST':
#         selected_address_id = request.POST.get('selected_address')
#         print(selected_address_id)

        # if selected_address_id:
        #     selected_address = address_change.objects.get(pk=selected_address_id)
        #     request.session['selected_address']=selected_address
        #     print(request.session['selected_address'])



    # context = {
    #     'addresses': addresses,
    #     'selected_address': selected_address,
    #     'userid':id4
    # }
    #
    # return render(request,"preview_display.html",context)

def address_edit(request,id):
    e = address_change.objects.get(id=id)
    if request.method=='POST':
        e.name=request.POST.get('name')

        e.daddress = request.POST.get('address')
        e.state = request.POST.get('state')
        e.city = request.POST.get('city')
        e.houseno = request.POST.get('bno')
        e.landmark = request.POST.get('lmark')
        e.pincode = request.POST.get('pinc')
        e.phn=request.POST.get('phone')
        e.alt_phn=request.POST.get('alt_phn')
        e.save()
        return redirect(address_display)
    return render(request,'address_editing.html',{'data':e})

def address_delete(request,id):
    d=address_change.objects.get(id=id)
    d.delete()
    return redirect(address_display)

def proceed_to_payment(request):

    return render(request,'procced_to_pay.html')

def confirm_payemnt(request):
    id5=request.session['u_id']
    addr=address_change.objects.filter(userid=id5)
    addr1=[]
    for i in addr:
        addr1.append(i.daddress)
        addr1.append(i.state)
        addr1.append(i.city)
        addr1.append(i.houseno)
        addr1.append(i.landmark)
        addr1.append(i.pincode)
        addr1.append(i.phn)
        addr1.append(i.alt_phn)
    print(addr1)
    ord_date = datetime.date.today()
    est_date = ord_date + datetime.timedelta(days=7)

    total_amt1 = request.session['tprice']
    print(total_amt1)

    cart_items = []
    cc = add_cart.objects.all()
    for j in cc:
        if id5 == j.userid:
            pic1=str(j.pic).split('/')[-1]
            cart_items.append(pic1)
            cart_items.append(j.brand)
            # cart_items.append(j.brand)
            cart_items.append(j.name)
            cart_items.append(j.quantity)
            cart_items.append(j.price)
            cart_items.append(j.category)

    print(cart_items)

    confirm=order_confirm(userid=id5,address=addr1,prod_details=cart_items,total=total_amt1,order_date=ord_date,esimated_date=est_date)
    confirm.save()
    return redirect(preview_display)






def preview_display(request):
    id9 = request.session.get('u_id')
    cc = order_confirm.objects.filter(userid=id9)



    product_data = []
    addr=[]
    total1=[]
    for i in cc:
        addr.append(i.address)

        data_string = i.address.replace("[", "").replace("]", "")
        # Split the 'prod_details' string into individual elements
        prod_details_str = i.prod_details.strip("[]").replace("'", "").split(', ')
        data_list = [elem.strip().strip("'") for elem in data_string.split(',')]
        result_string = ' , '.join(data_list)

        total1.append(i.total)
        tot=str(i.total).strip("[]")
        # Check if there are at least 5 elements (details for one product)
        min_elements_per_product = 6
        num_products = len(prod_details_str) // min_elements_per_product

        if num_products >= 1:
            # Split and store the details for each product
            product_details = []

            for j in range(num_products):
                start_idx = j * min_elements_per_product
                end_idx = start_idx + min_elements_per_product
                product_details.append(prod_details_str[start_idx:end_idx])

            # Append the product details to the product_data list
            product_data.append({
                'product_details': product_details,
            })


    return render(request, 'preview_display.html', {'data': product_data,'addrr':result_string,'total':tot})












