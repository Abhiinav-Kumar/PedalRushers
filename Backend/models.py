from django.db import models

# Create your models here.

class PedalRushersDB(models.Model):
    Category_PD = models.CharField(max_length=100,null=True,blank=True)
    Description_PD = models.CharField(max_length=200,null=True,blank=True)
    Image_PD = models.ImageField(upload_to="PedalRushers_Images",null=True,blank=True)


class PR_Sub_category_DB(models.Model):
    Sub_Category= models.CharField(max_length=100, null=True, blank=True)
    Sub_Models= models.CharField(max_length=100, null=True, blank=True)
    Sub_Description_PD = models.CharField(max_length=300,null=True,blank=True)
    Sub_Image_PD = models.ImageField(upload_to="Sub_category_images",null=True,blank=True)

class PR_Product_DB(models.Model):
    Pro_Type = models.CharField(max_length=200,null=True,blank=True)
    Pro_Model = models.CharField(max_length=200,null=True,blank=True)
    Pro_Price = models.IntegerField(null=True,blank=True)
    Pro_Brand =models.CharField(max_length=200,null=True,blank=True)
    Pro_Description =models.CharField(max_length=200,null=True,blank=True)
    Pro_Img = models.ImageField(upload_to="Product_images",null=True,blank=True)


class PR_Technical_DB(models.Model):
    Tec_Product = models.CharField(max_length=200,null=True,blank=True)
    Tec_Description = models.CharField(max_length=600,null=True,blank=True)
    Tec_Age = models.CharField(max_length=50,null=True,blank=True)
    Tec_Color = models.CharField(max_length=50,null=True,blank=True)
    Tec_Material = models.CharField(max_length=100,null=True,blank=True)
    Tec_Size = models.CharField(max_length=50,null=True,blank=True)
    Tec_Features = models.CharField(max_length=300,null=True,blank=True)
    Tec_Style = models.CharField(max_length=100,null=True,blank=True)
    Tec_Components = models.CharField(max_length=200,null=True,blank=True)
    Tec_Weight = models.CharField(max_length=100,null=True,blank=True)
    Tec_ModelNo = models.CharField(max_length=100,null=True,blank=True)
    Tec_Manufacture = models.CharField(max_length=100,null=True,blank=True)
    Tec_Orgin = models.CharField(max_length=100,null=True,blank=True)
    Tec_Prsin = models.CharField(max_length=100,null=True,blank=True)





