from django.shortcuts import render,redirect
from Backend.models import PedalRushersDB,PR_Product_DB,PR_Sub_category_DB,PR_Technical_DB
from WebApp.models import UserDB,CartDB,UserBillingDB
from django.contrib import messages
import razorpay

# from WebApp.models import ContactDb,UserDB


# Create your views here.
def Home_page(req):
    cat = PedalRushersDB.objects.all()
    return render(req,"Home.html",{'cat':cat})

def Product_page(req):
    pro = PR_Product_DB.objects.all()
    cat = PedalRushersDB.objects.all()
    return render(req,"Products_web.html",{'pro':pro,'cat':cat})

def Contact_page(req):
    cat = PedalRushersDB.objects.all()
    return render(req,"Contact.html",{'cat':cat})

def Save_contact_web(req):
    if req.method=="POST":
        NAME = req.POST.get('name')
        EMAIL = req.POST.get('email')
        MESSAGES = req.POST.get('message')

        obj = ContactDb(Name=NAME,Email=EMAIL,Messages=MESSAGES)
        obj.save()
        return redirect(Contact_page)


def Sub_Filtered_product(req,sub_name):
    data = PR_Sub_category_DB.objects.filter(Sub_Category=sub_name)
    cat = PedalRushersDB.objects.all()
    return render(req,"Sub_category_Filtered.html",{'data':data,'cat':cat})

def Products_Filtered(req,pro_name):
    data = PR_Product_DB.objects.filter(Pro_Type=pro_name)
    cat = PedalRushersDB.objects.all()
    return render(req,"Products_Filtered.html",{'data':data,'cat':cat})

def Single_Product_Page(req,pro_id,productname):
    data = PR_Product_DB.objects.get(id = pro_id)
    cat = PedalRushersDB.objects.all()

    # productname_stripped = productname.strip()
    #
    # # Remove all whitespace between words
    # productname_no_spaces = productname_stripped.replace(" ", "")
    # print("Product name without spaces:", productname_no_spaces)
    # # x = data.Pro_Model
    # print("Product name getting :",productname.strip())
    tec = PR_Technical_DB.objects.get(Tec_Product=productname)

    return render(req,"Single_Product.html",{'data':data,'cat':cat,'tec':tec})

def About_page(req):
    cat = PedalRushersDB.objects.all()
    return render(req,"About.html",{'cat':cat})


def User_login_page(request):
    return render(request,"user_Login.html")

def Save_User(request):
    if request.method == "POST":
        USER = request.POST.get('user')
        EMAIL = request.POST.get('email')
        PASS = request.POST.get('pass')

        obj = UserDB(Username=USER,Email=EMAIL,Password=PASS)
        obj.save()
        return redirect(User_login_page)

def User_login(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('pass')

        if UserDB.objects.filter(Username=un,Password=pwd).exists():
            request.session['Username']=un
            request.session['Password']=pwd
            messages.success(request, "Welcome")
            return redirect(Home_page)
        else:
            messages.error(request,"Inavlid Password")
            return redirect(User_login_page)
    else:
        messages.error(request, "User Not Found")
        return redirect(User_login_page)

def user_logout(request):

    del request.session['Username']
    del request.session['Password']
    messages.success(request, "Successfully Logout")
    return redirect(Home_page)


def Cart_page(req):
    cat = PedalRushersDB.objects.all()
    try:
        data = CartDB.objects.filter(Username=req.session['Username'])
        sub_total = 0
        shipping_charge = 0
        total = 0
        for x in data:
            sub_total += x.Total_Price
            if sub_total >= 10000:
                shipping_charge = 50
            elif sub_total>= 5000:
                shipping_charge = 100
            elif sub_total >= 1000:
                shipping_charge = 130
            else:
                shipping_charge = 150

            total =sub_total+shipping_charge
        return render(req,"Cart.html",{'cat':cat,'data':data,'sub_total':sub_total,'total':total,'shipping_charge':shipping_charge})
    except KeyError:
        messages.error(req,"Please Login into your Account")
        return redirect(Home_page)

def Save_Cart(req):
    if req.method == "POST":

        UN = req.POST.get('USERNAME')
        PRON = req.POST.get('PRODUCT_NAME')
        TP = req.POST.get('TOTAL_PRICE')
        QT = req.POST.get('QUANTITY')

        obj = CartDB(Username=UN,Product=PRON,Quantity=QT,Total_Price=TP)
        obj.save()
        messages.success(req,"ADDED TO CART")
        return redirect(Cart_page)

def Delete_cart_item(req,cartid):
    x = CartDB.objects.filter(id=cartid)
    x.delete()
    messages.warning(req,"Removed From Cart")
    return redirect(Cart_page)

def Checkout_page(req):
    cat = PedalRushersDB.objects.all()
    data = CartDB.objects.filter(Username=req.session['Username'])
    sub_total = 0
    shipping_charge = 0
    total = 0
    for x in data:
        sub_total += x.Total_Price
    if sub_total >= 10000:
        shipping_charge = 50
    elif sub_total>= 5000:
        shipping_charge = 100
    elif sub_total >= 1000:
        shipping_charge = 130
    else:
        shipping_charge = 150

    total =sub_total+shipping_charge
    return render(req,'Checkout.html',{'cat':cat,'total':total})

def Save_Billing(req):
    if req.method=="POST":
        un = req.POST.get('username')
        em = req.POST.get('email')
        ph = req.POST.get('phonenumber')
        add = req.POST.get('address')
        state = req.POST.get('state')
        city = req.POST.get('city')
        postal = req.POST.get('postal')
        mes = req.POST.get('message')
        tp = req.POST.get('totalprice')

        obj = UserBillingDB(Username=un,Email=em,Phone=ph,Address=add,State=state,City=city,Postalcode=postal,Messages=mes,Totalprice=tp)
        obj.save()
        x = CartDB.objects.filter(Username=req.session['Username'])
        x.delete()
        return redirect(Payment_page)


def Payment_page(req):
    customer = UserBillingDB.objects.order_by('-id').first()
    pay = customer.Totalprice
    amount = int(pay*100)
    pay_str = str(amount)
    if req.method=="POST":
        order_currecy='INR'
        client = razorpay.Client(auth=('rzp_test_3lMy3dVuXe8hqk','fXEFJv7RHxqbXGaIF2Xij3B5'))
        payment = client.order.create({'amount':amount,'currency':order_currecy,'payment_capture':'1'})
    return render(req,"Payment.html",{'customer':customer,'pay_str':pay_str})
    
