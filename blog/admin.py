from django.contrib import admin
from .models import User, Reyting, MockTest, Universitet, Sozlamalar, Yutuq

# Register your models here.

admin.site.register(User)
admin.site.register(Reyting)
admin.site.register(MockTest)
admin.site.register(Universitet)
admin.site.register(Sozlamalar)
admin.site.register(Yutuq)