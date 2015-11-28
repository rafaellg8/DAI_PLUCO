from django.contrib import admin
from plucoApp.models import Comment,Forum,User
#importamos de plucoApp los modelos
# Register your models here.

admin.site.register(Comment)
admin.site.register(Forum)
admin.site.register(User)
