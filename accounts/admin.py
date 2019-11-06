from django.contrib import admin
from .models import User

admin.site.register(User) #管理画面でUserモデルを操作
