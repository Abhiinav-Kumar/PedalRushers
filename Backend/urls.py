from django.urls import path
from Backend import views
urlpatterns = [
    path('Login_page/',views.Login_page,name="Login_page"),
    path('Admin_login/',views.Admin_login,name="Admin_login"),
    path('Admin_logout/',views.Admin_logout,name="Admin_logout"),

    path('Index_page/',views.Index_page,name="Index_page"),

    path('Add_Category/',views.Add_Category,name="Add_Category"),
    path('Save_Category/',views.Save_Category,name="Save_Category"),
    path('View_Categories/',views.View_Categories,name="View_Categories"),
    path('Edit_Categories/<int:PRID>/',views.Edit_Categories,name="Edit_Categories"),
    path('Update_categories/<int:PRID>/',views.Update_categories,name="Update_categories"),
    path('Delete_categories/<int:PRID>/',views.Delete_categories,name="Delete_categories"),

    path('Sub_category_page/',views.Sub_category_page,name="Sub_category_page"),
    path('Save_Sub_category/',views.Save_Sub_category,name="Save_Sub_category"),
    path('View_Sub_category/',views.View_Sub_category,name="View_Sub_category"),
    path('Edit_Sub_category/<int:subid>/',views.Edit_Sub_category,name="Edit_Sub_category"),
    path('Upadte_Sub_category/<int:subid>/',views.Upadte_Sub_category,name="Upadte_Sub_category"),
    path('Delete_Sub_category/<int:subid>/',views.Delete_Sub_category,name="Delete_Sub_category"),

    path('Product_page/',views.Product_page,name="Product_page"),
    path('Save_Product/',views.Save_Product,name="Save_Product"),
    path('View_Products/',views.View_Products,name="View_Products"),
    path('Edit_Product_page/<int:pid>/',views.Edit_Product_page,name="Edit_Product_page"),
    path('Update_Product/<int:pid>/',views.Update_Product,name="Update_Product"),
    path('Delete_products/<int:pid>/',views.Delete_products,name="Delete_products"),

    path('contact_page/',views.contact_page,name="contact_page"),
    path('Delete_contact/<int:cid>/',views.Delete_contact,name="Delete_contact"),

    path('Technical_page/',views.Technical_page,name="Technical_page"),
    path('Save_Technical_data/',views.Save_Technical_data,name="Save_Technical_data"),
    path('View_Technical/',views.View_Technical,name="View_Technical"),
    path('Technical_Edit_page/<int:techid>/',views.Technical_Edit_page,name="Technical_Edit_page"),
    path('Update_Technical/<int:techid>/',views.Update_Technical,name="Update_Technical"),
    path('Delete_technical/<int:tecid>/',views.Delete_technical,name="Delete_technical"),
]