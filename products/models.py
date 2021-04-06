from django.db.models.signals import post_save
from django.db import models
from django.db.models import Sum
from django.conf import settings
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Account(models.Model):
    accountid = models.CharField(db_column='AccountID', primary_key=True, max_length=20)  # Field name made lowercase.
    businesstype = models.CharField(db_column='BusinessType', max_length=15)  # Field name made lowercase.
    emailaddressid = models.ForeignKey('Accountaddress', models.DO_NOTHING, db_column='EmailAddressID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'account'

class Accountaddress(models.Model):
    emailaddressid = models.CharField(db_column='EmailAddressID', primary_key=True, max_length=10)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=25)  # Field name made lowercase.
    passwordid = models.ForeignKey('Password', models.DO_NOTHING, db_column='PasswordID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accountaddress'


class Accountpaymentinforel(models.Model):
    accountpaymentinforelid = models.CharField(db_column='AccountPaymentInfoRelID', primary_key=True, max_length=20)  # Field name made lowercase.
    accountid = models.ForeignKey(Account, models.DO_NOTHING, db_column='AccountID')  # Field name made lowercase.
    cardid = models.ForeignKey('Paymentinfo', models.DO_NOTHING, db_column='CardID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'accountpaymentinforel'



class Address(models.Model):
    addressid = models.CharField(db_column='AddressID', primary_key=True, max_length=10)  # Field name made lowercase.
    addressline1 = models.CharField(db_column='AddressLine1', max_length=25, blank=True, null=True)  # Field name made lowercase.
    addressline2 = models.CharField(db_column='AddressLine2', max_length=25, blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=25, blank=True, null=True)  # Field name made lowercase.
    postalcode = models.CharField(db_column='PostalCode', max_length=8, blank=True, null=True)  # Field name made lowercase.
    lastupdate = models.DateField(db_column='LastUpdate', blank=True, null=True)  # Field name made lowercase.
    provid = models.ForeignKey('Province', models.DO_NOTHING, db_column='ProvID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'address'



class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'



class Invoice(models.Model):
    invoiceid = models.CharField(db_column='InvoiceID', primary_key=True, max_length=10)  # Field name made lowercase.
    dategenerated = models.DateField(db_column='DateGenerated', blank=True, null=True)  # Field name made lowercase.
    paymentdue = models.DateField(db_column='PaymentDue')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'invoice'


class OrderProductrel(models.Model):
    order_productrelid = models.CharField(db_column='Order_ProductRelID', primary_key=True, max_length=10)  # Field name made lowercase.
    orderid = models.ForeignKey('Orders', models.DO_NOTHING, db_column='OrderID')  # Field name made lowercase.
    productserialnumber = models.ForeignKey('Productinventory', models.DO_NOTHING, db_column='ProductSerialNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order_productrel'



class Orderproduct(models.Model):
    user = models.ForeignKey('Userprofile', models.DO_NOTHING, db_column='user', blank=True, null=True)
    productid = models.ForeignKey('Product', models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    ordered = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(primary_key=True)
    totalitemcost = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orderproduct'
    
    def __str__(self):
        return f"{self.quantity} of {self.productid.name}"
        
    @property
    def cost(self, *args, **kwargs):
        self.totalitemcost = self.productid.rentalcost * self.quantity
        super(Orderproduct, self).save(*args, **kwargs)


class Orders(models.Model):
    orderid = models.CharField(db_column='OrderID', primary_key=True, max_length=15)  # Field name made lowercase.
    invoiceid = models.ForeignKey('Invoice', models.DO_NOTHING, db_column='InvoiceID', blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    orderrecieveddate = models.DateField(db_column='OrderRecievedDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, blank=True, null=True)  # Field name made lowercase.
    statusdatechanged = models.DateField(db_column='StatusDateChanged', blank=True, null=True)  # Field name made lowercase.
    accountid = models.ForeignKey('Account', models.DO_NOTHING, db_column='AccountID', blank=True, null=True)  # Field name made lowercase.
    referenceorderid = models.CharField(db_column='ReferenceOrderID', max_length=15, blank=True, null=True)  # Field name made lowercase.
    ordered = models.IntegerField(blank=True, null=True)
    id = models.ForeignKey('Orderproduct', models.DO_NOTHING, db_column='id', blank=True, null=True)
    DisplayFields = ['orderid', 'invoiceid', 'startdate', 'enddate', 'orderrecieveddate', 'status', 'statusdatechanged', 'accountid', 'days']

    class Meta:
        managed = False
        db_table = 'orders'

    def __str__(self):
        return self.orderid
    
    @property    
    def days(self):
        if(self.enddate != None):
            days = self.enddate.day - seld.startdate.day
            return days



class Password(models.Model):
    passwordid = models.CharField(db_column='PasswordID', primary_key=True, max_length=5)  # Field name made lowercase.
    currentpassword = models.CharField(db_column='CurrentPassword', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datechanged = models.DateField(db_column='DateChanged', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'password'




class Payment(models.Model):
    paymentid = models.CharField(db_column='PaymentID', primary_key=True, max_length=10)  # Field name made lowercase.
    invoiceid = models.ForeignKey(Invoice, models.DO_NOTHING, db_column='InvoiceID', blank=True, null=True)  # Field name made lowercase.
    paymentdate = models.DateField(db_column='PaymentDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'payment'


class Paymentinfo(models.Model):
    cardid = models.CharField(db_column='CardID', primary_key=True, max_length=20)  # Field name made lowercase.
    paymenttype = models.CharField(db_column='PaymentType', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'paymentinfo'


class Product(models.Model):
    productid = models.CharField(db_column='ProductID', primary_key=True, max_length=30)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subcategoryid = models.ForeignKey('Subproductcategory', models.DO_NOTHING, db_column='SubCategoryID', blank=True, null=True)  # Field name made lowercase.
    weight = models.CharField(db_column='Weight', max_length=30, blank=True, null=True)  # Field name made lowercase.
    weightmeasurecode = models.CharField(db_column='WeightMeasureCode', max_length=30, blank=True, null=True)  # Field name made lowercase.
    rentalcost = models.IntegerField(db_column='RentalCost', blank=True, null=True)  # Field name made lowercase.
    hexcolour = models.CharField(db_column='HexColour', max_length=30, blank=True, null=True)  # Field name made lowercase.
    dateadded = models.DateField(db_column='DateAdded', blank=True, null=True)  # Field name made lowercase.
    dateremoved = models.DateField(db_column='DateRemoved', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=15, blank=True, null=True)  # Field name made lowercase.
    product_img = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(default=1)

    class Meta:
        managed = False
        db_table = 'product'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products/product_list.html", kwargs={
            'productid': self.productid
        })

    def get_add_to_cart_url(self):
        return reverse("products:add_to_cart", kwargs={
            'product': self.product
        })

    def get_remove_from_cart_url(self):
        return reverse("products:remove-from-cart", kwargs={
            'productid': self.productid
        })

class Productcategory(models.Model):
    productcategoryid = models.CharField(db_column='ProductCategoryID', primary_key=True, max_length=5)  # Field name made lowercase.
    productcategoryname = models.CharField(db_column='ProductCategoryName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datemodified = models.DateField(db_column='DateModified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productcategory'


class Productinventory(models.Model):
    productserialnumber = models.CharField(db_column='ProductSerialNumber', primary_key=True, max_length=15)  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductID', blank=True, null=True)  # Field name made lowercase.
    shelf = models.CharField(db_column='Shelf', max_length=10, blank=True, null=True)  # Field name made lowercase.
    storeid = models.ForeignKey('Store', models.DO_NOTHING, db_column='StoreID', blank=True, null=True)  # Field name made lowercase.
    rentalstartdate = models.DateField(db_column='RentalStartDate', blank=True, null=True)  # Field name made lowercase.
    rentalenddate = models.DateField(db_column='RentalendDate', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'productinventory'



class Subproductcategory(models.Model):
    subproductcategoryid = models.CharField(db_column='SubProductCategoryID', primary_key=True, max_length=50)  # Field name made lowercase.
    productcategoryid = models.ForeignKey(Productcategory, models.DO_NOTHING, db_column='ProductCategoryID')  # Field name made lowercase.
    subproductcategoryname = models.CharField(db_column='SubProductCategoryName', max_length=20, blank=True, null=True)  # Field name made lowercase.
    datemodified = models.DateField(db_column='DateModified', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'subproductcategory'



class Userprofile(models.Model):
    user = models.CharField(primary_key=True, max_length=20)
    accountid = models.ForeignKey('Account', models.DO_NOTHING, db_column='AccountID', blank=True, null=True)  # Field name made lowercase.
    oneclickbuy = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'userprofile'


class Store(models.Model):
    storeid = models.CharField(db_column='StoreID', primary_key=True, max_length=2)  # Field name made lowercase.
    addressid = models.ForeignKey(Address, models.DO_NOTHING, db_column='AddressID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'store'


class Province(models.Model):
    provid = models.CharField(db_column='ProvID', primary_key=True, max_length=10)  # Field name made lowercase.
    provname = models.CharField(db_column='ProvName', max_length=25, blank=True, null=True)  # Field name made lowercase.
    abbreviation = models.CharField(db_column='Abbreviation', max_length=2, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'province'


