from django.urls import path
from WebApp import views
urlpatterns = [
    path('',views.Home_page,name="Home"),
    path('User_login_page',views.User_login_page,name="User_login_page"),
    path('Save_User',views.Save_User,name="Save_User"),
    path('User_login',views.User_login,name="User_login"),
    path('user_logout',views.user_logout,name="user_logout"),

    path('About_page',views.About_page,name="About_page"),

    path('Contact_page/',views.Contact_page,name="Contact_page"),
    path('Save_contact_web/',views.Save_contact_web,name="Save_contact_web"),

    path('Products_Web/',views.Product_page,name="Products_Web"),
    path('Sub_Filtered_product/<sub_name>/',views.Sub_Filtered_product,name="Sub_Filtered_product"),
    path('Products_Filtered/<pro_name>/',views.Products_Filtered,name="Products_Filtered"),
    path('Single_Product_Page/<int:pro_id>/<productname>/',views.Single_Product_Page,name="Single_Product_Page"),

    path('Cart_page',views.Cart_page,name="Cart_page"),
    path('Save_Cart',views.Save_Cart,name="Save_Cart"),
    path('Delete_cart_item/<int:cartid>/',views.Delete_cart_item,name="Delete_cart_item"),

    path('Checkout_page/',views.Checkout_page,name="Checkout_page"),
    path('Save_Billing/',views.Save_Billing,name="Save_Billing"),

     path('Payment_page/',views.Payment_page,name="Payment_page"),


]