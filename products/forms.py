from .models import Orders, Orderproduct, Product, Userprofile
from django import forms

class OrderItemForm(forms.ModelForm):
 
    class Meta:
        model = Orderproduct
        fields = [
            'productid',
            'quantity',
            'id',
            

        ]


class OrderForm(forms.ModelForm):
    startdate    = forms.DateField(label='What date will you need these items by?', widget=forms.DateInput)
    enddate      = forms.DateField(label="Last day that you'll need these items" ,widget=forms.DateInput)
    orderreceiveddate = forms.DateField(label="Please enter today's date:", widget=forms.DateInput)
    
    class Meta:
        model = Orders
        fields = [
            'orderid',
            'startdate',
            'enddate',
            'orderreceiveddate',
            'accountid', 
            'id'
        ]

#class RawOrderForm(forms.Form):
#    orderid      = forms.CharField(label='Please enter 4-5 digit combination of number (random is fine). This will be your Order ID')
#    startdate    = forms.DateField(label='What date will you need these items by?', widget=forms.DateInput)
#    enddate      = forms.DateField(label="Last day that you'll need these items" ,widget=forms.DateInput)
#    orderreceiveddate = forms.DateField(label="Please enter today's date:")
#    accountid    = forms.CharField(label='Please renter your username/account id: ')
#    id           = forms.CharField()





