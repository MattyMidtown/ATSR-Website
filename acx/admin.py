from django.contrib import admin

# Register your models here.
from .models import Account
from .models import Accountaddress
from .models import Address
from .models import Accountpaymentinforel
from .models import Companyentity
from .models import Companyentityaddressrel
from .models import Person
from .models import Password
from .models import Paymentinfo
from .models import Province
from .models import Roletype

admin.site.register(Account)
admin.site.register(Accountaddress)
admin.site.register(Address)
admin.site.register(Accountpaymentinforel)
admin.site.register(Companyentity)
admin.site.register(Companyentityaddressrel)
admin.site.register(Person)
admin.site.register(Password)
admin.site.register(Paymentinfo)
admin.site.register(Province)
admin.site.register(Roletype)

