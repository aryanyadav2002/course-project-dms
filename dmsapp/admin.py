from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Userip)
class UseripAdmin(admin.ModelAdmin):
    list_display= ('id', 'dia','rpm','rload','aload', 'lfactor', 'elife')


@admin.register(series60)
class series60Admin(admin.ModelAdmin):
    list_display= ('skfNo', 'dia','d1min','dcap','d2min', 'bB', 'rR','rR1', 'staticC','dynamicC','maxSpeed')
@admin.register(series62)
class series62Admin(admin.ModelAdmin):
    list_display= ('skfNo', 'dia','d1min','dcap','d2min', 'bB', 'rR','rR1', 'staticC','dynamicC','maxSpeed')
@admin.register(series63)
class series63Admin(admin.ModelAdmin):
    list_display= ('skfNo', 'dia','d1min','dcap','d2min', 'bB', 'rR','rR1', 'staticC','dynamicC','maxSpeed')
@admin.register(series64)
class series64Admin(admin.ModelAdmin):
    list_display= ('skfNo', 'dia','d1min','dcap','d2min', 'bB', 'rR','rR1', 'staticC','dynamicC','maxSpeed')
@admin.register(Eqbload)
class EqbloadAdmin(admin.ModelAdmin):
    list_display= ('faco','e','lx','ly', 'gx', 'gy')

##########################
@admin.register(series65)
class series65Admin(admin.ModelAdmin):
    list_display= ('skfNo', 'dia','d1min','dcap','d2min', 'bB', 'rR','rR1', 'staticC','dynamicC','maxSpeed')