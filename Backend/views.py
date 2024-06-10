from django.shortcuts import render,redirect
from Backend.models import PedalRushersDB,PR_Sub_category_DB,PR_Product_DB,PR_Technical_DB
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import ContactDb
from django.contrib import messages
# Create your views here.

def Index_page(req):
    return render(req,"Index.html")

def Add_Category(req):
    return render(req,"Category.html")

def Save_Category(req):
    if req.method == "POST":
        CTYPE = req.POST.get('CATEGORY')
        CDES = req.POST.get('DESCRIPTION')
        CIMG = req.FILES['IMAGE']

        obj = PedalRushersDB(Category_PD=CTYPE,Description_PD=CDES,Image_PD=CIMG)
        obj.save()
        messages.success(req,"Category Saved")
        return redirect(Add_Category)

def View_Categories(req):
    data = PedalRushersDB.objects.all()
    return render(req,"View_Categories.html",{"data":data})

def Edit_Categories(req,PRID):
    data = PedalRushersDB.objects.get(id=PRID)
    return render(req,"Edit_category.html",{"data":data})

def Update_categories(req,PRID):
    if req.method == "POST":
        CTYPE = req.POST.get('CATEGORY')
        CDES = req.POST.get('DESCRIPTION')

        try:
            img = req.FILES['IMAGE']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file =PedalRushersDB.objects.get(id=PRID).Image_PD

        PedalRushersDB.objects.filter(id=PRID).update(Category_PD=CTYPE,Description_PD=CDES,Image_PD=file)
        messages.success(req,"Updated")
        return redirect(View_Categories)

def Delete_categories(req,PRID):
    x = PedalRushersDB.objects.filter(id=PRID)
    x.delete()
    messages.error(req,"Deleted.")
    return redirect(View_Categories)

def Login_page(request):
    return render(request,"Login.html")

def Admin_login(request):
    if request.method=="POST":
        UN = request.POST.get('username')
        PWD = request.POST.get('pass')
        if User.objects.filter(username__contains=UN).exists():
            x = authenticate(username=UN,password=PWD)
            if x is not None:
                login(request,x)
                request.session['username']=UN
                request.session['password']=PWD
                messages.success(request,"Welcome")
                return redirect(Index_page)
            else:
                messages.error(request,"Inavlid Password")
                return redirect(Login_page)
        else:
            messages.warning(request,"User Not Found")
            return redirect(Login_page)

def Admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.error(request,"Successfully Logout")
    return redirect(Login_page)

def Sub_category_page(req):
    CATG =PedalRushersDB.objects.all()
    return render(req,"Sub_category.html",{"CATG":CATG})

def Save_Sub_category(req):
    if req.method=="POST":
        MCAT=req.POST.get('CATEGORY')
        Sub_name=req.POST.get('SUB')
        Sub_des=req.POST.get('DESCRIPTION')
        Sub_IMG=req.FILES['SUBIMAGE']

        obj=PR_Sub_category_DB(Sub_Category=MCAT,Sub_Models=Sub_name,Sub_Description_PD=Sub_des,Sub_Image_PD=Sub_IMG)
        obj.save()
        messages.success(req,"Successfully Added")
        return redirect(Sub_category_page)

def View_Sub_category(req):
    data = PR_Sub_category_DB.objects.all()
    return render(req,"View_sub_category.html",{"data":data})

def Edit_Sub_category(req,subid):
    cat = PedalRushersDB.objects.all()
    data=PR_Sub_category_DB.objects.get(id=subid)
    return render(req,"Edit_Sub_category.html",{"data":data,'cat':cat})

def Upadte_Sub_category(req,subid):
    if req.method=="POST":
        MCAT=req.POST.get('CATEGORY')
        Sub_name=req.POST.get('SUB')
        Sub_des=req.POST.get('DESCRIPTION')

        try:
            img = req.FILES['SUBIMAGE']
            fs= FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = PR_Sub_category_DB.objects.get(id=subid).Sub_Image_PD

        PR_Sub_category_DB.objects.filter(id=subid).update(Sub_Category=MCAT,Sub_Models=Sub_name,Sub_Description_PD=Sub_des,Sub_Image_PD=file)
        messages.success(req,"Updated")
        return redirect(View_Sub_category)
def Delete_Sub_category(req,subid):
    x =PR_Sub_category_DB.objects.filter(id=subid)
    x.delete()
    messages.error(req,"Deleted")
    return redirect(View_Sub_category)

def Product_page(req):
    sub = PR_Sub_category_DB.objects.all()
    return render(req,"Productsbacked.html",{'sub':sub})

def Save_Product(req):
    if req.method=="POST":
        Type = req.POST.get('TYPE')
        Model = req.POST.get('MODEL')
        Price = req.POST.get('PRICE')
        Brand = req.POST.get('BRAND')
        Descri = req.POST.get('DESCRIPTION')
        Img = req.FILES['PIMAGE']

        obj = PR_Product_DB(Pro_Type=Type,Pro_Model=Model,Pro_Price=Price,Pro_Brand=Brand,Pro_Description=Descri,Pro_Img=Img)
        obj.save()
        messages.success(req,"Saved")
        return redirect(Technical_page)

def View_Products(req):
    data = PR_Product_DB.objects.all()
    return render(req,"View_Product.html",{"data":data})

def Edit_Product_page(req,pid):
    sub = PR_Sub_category_DB.objects.all()
    data = PR_Product_DB.objects.get(id=pid)
    return render(req,"Edit_Products.html",{'data':data,'sub':sub})

def Update_Product(req,pid):
    if req.method=="POST":
        Type = req.POST.get('TYPE')
        Model = req.POST.get('MODEL')
        Price = req.POST.get('PRICE')
        Brand = req.POST.get('BRAND')
        Descri = req.POST.get('DESCRIPTION')

        try:
            img = req.FILES['PIMAGE']
            fs =FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = PR_Product_DB.objects.get(id=pid).Pro_Img
        PR_Product_DB.objects.filter(id=pid).update(Pro_Type=Type,Pro_Model=Model,Pro_Price=Price,Pro_Brand=Brand,Pro_Description=Descri,Pro_Img=file)
        messages.success(req,"Updated")
        return redirect(View_Products)

def Delete_products(req,pid):
    x = PR_Product_DB.objects.filter(id=pid)
    x.delete()
    messages.error(req,"Deleted")
    return redirect(View_Products)

def contact_page(req):
    data= ContactDb.objects.all()
    return render(req,"View_Contact.html",{'data':data})

def Delete_contact(req,cid):
    x = ContactDb.objects.filter(id=cid)
    x.delete()
    messages.error(req,"Deleted")
    return redirect(contact_page)


def Technical_page(req):
    pro = PR_Product_DB.objects.all()
    return render(req,"Technical.html",{"pro":pro})

def Save_Technical_data(req):
    if req.method == "POST":
        PR = req.POST.get('PRODUCTNAME')
        DES = req.POST.get('DESCRIPTION')
        AGE = req.POST.get('AGE')
        CLR = req.POST.get('COLOR')
        MAT = req.POST.get('MATERIAL')
        SIZE = req.POST.get('SIZE')
        FET = req.POST.get('FEATURES')
        STY = req.POST.get('STYLE')
        COM = req.POST.get('COMPONENTS')
        WEI = req.POST.get('WEIGHT')
        MODN = req.POST.get('MODELNUM')
        MANU = req.POST.get('MANUFACTURE')
        ORG = req.POST.get('ORIGIN')
        PRSIN = req.POST.get('PRSIN')

        obj = PR_Technical_DB(Tec_Product=PR,Tec_Description=DES,Tec_Age=AGE,Tec_Color=CLR,Tec_Material=MAT,Tec_Size=SIZE,Tec_Features=FET,Tec_Style=STY,Tec_Components=COM,Tec_Weight=WEI,Tec_ModelNo=MODN,Tec_Manufacture=MANU,Tec_Orgin=ORG,Tec_Prsin=PRSIN)
        obj.save()
        messages.success(req,"Added Sucessfully")
        return redirect(Technical_page)

def View_Technical(req):
    data = PR_Technical_DB.objects.all()
    return render(req,"View_Technical.html",{'data':data})

def Technical_Edit_page(req,techid):
    pro = PR_Product_DB.objects.all()
    data =PR_Technical_DB.objects.get(id=techid)
    return render(req,"Edit_Technical.html",{'pro':pro,'data':data})

def Update_Technical(req,techid):
    if req.method == "POST":
        PR = req.POST.get('PRODUCTNAME')
        DES = req.POST.get('DESCRIPTION')
        AGE = req.POST.get('AGE')
        CLR = req.POST.get('COLOR')
        MAT = req.POST.get('MATERIAL')
        SIZE = req.POST.get('SIZE')
        FET = req.POST.get('FEATURES')
        STY = req.POST.get('STYLE')
        COM = req.POST.get('COMPONENTS')
        WEI = req.POST.get('WEIGHT')
        MODN = req.POST.get('MODELNUM')
        MANU = req.POST.get('MANUFACTURE')
        ORG = req.POST.get('ORIGIN')
        PRSIN = req.POST.get('PRSIN')

        PR_Technical_DB.objects.filter(id=techid).update(Tec_Product=PR,Tec_Description=DES,Tec_Age=AGE,Tec_Color=CLR,Tec_Material=MAT,Tec_Size=SIZE,Tec_Features=FET,Tec_Style=STY,Tec_Components=COM,Tec_Weight=WEI,Tec_ModelNo=MODN,Tec_Manufacture=MANU,Tec_Orgin=ORG,Tec_Prsin=PRSIN)
        messages.success(req,"Successfully Updated")
        return redirect(View_Technical)

def Delete_technical(req,tecid):
    x = PR_Technical_DB.objects.filter(id=tecid)
    x.delete()
    messages.error(req,"Deleted")
    return redirect(View_Technical)

