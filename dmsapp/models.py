from django.db import models

# Create your models here.
class Userip (models.Model):
    dia= models.DecimalField(max_digits = 5,decimal_places = 2,null=True,blank=True)
    rpm= models.DecimalField(max_digits = 8,decimal_places = 2,null=True,blank=True)
    rload= models.DecimalField(max_digits = 8,decimal_places = 2,null=True,blank=True)
    aload=models.DecimalField(max_digits = 8,decimal_places = 2,null=True,blank=True)
    lfactor=models.DecimalField(max_digits = 3,decimal_places = 2,null=True,blank=True)
    elife=models.DecimalField(max_digits = 8,decimal_places = 2,null=True,blank=True)

class series60(models.Model):
    skfNo=models.IntegerField(primary_key=True)
    dia=models.IntegerField()
    d1min=models.IntegerField()
    dcap=models.IntegerField()
    d2min=models.IntegerField()
    bB=models.IntegerField()
    rR=models.IntegerField()
    rR1=models.IntegerField()
    staticC=models.IntegerField()
    dynamicC=models.IntegerField()
    maxSpeed=models.IntegerField()

class series62(models.Model):
    skfNo=models.IntegerField(primary_key=True)
    dia=models.IntegerField()
    d1min=models.IntegerField()
    dcap=models.IntegerField()
    d2min=models.IntegerField()
    bB=models.IntegerField()
    rR=models.IntegerField()
    rR1=models.IntegerField()
    staticC=models.IntegerField()
    dynamicC=models.IntegerField()
    maxSpeed=models.IntegerField()

class series63(models.Model):
    skfNo=models.IntegerField(primary_key=True)
    dia=models.IntegerField()
    d1min=models.IntegerField()
    dcap=models.IntegerField()
    d2min=models.IntegerField()
    bB=models.IntegerField()
    rR=models.IntegerField()
    rR1=models.IntegerField()
    staticC=models.IntegerField()
    dynamicC=models.IntegerField()
    maxSpeed=models.IntegerField()

class series64(models.Model):
    skfNo=models.IntegerField(primary_key=True)
    dia=models.IntegerField()
    d1min=models.IntegerField()
    dcap=models.IntegerField()
    d2min=models.IntegerField()
    bB=models.IntegerField()
    rR=models.IntegerField()
    rR1=models.IntegerField()
    staticC=models.IntegerField()
    dynamicC=models.IntegerField()
    maxSpeed=models.IntegerField()

class Eqbload(models.Model):
    faco=models.DecimalField(max_digits = 5,decimal_places = 3, primary_key=True)
    e=models.DecimalField(max_digits = 5,decimal_places = 3)
    lx=models.DecimalField(max_digits = 5,decimal_places = 3)
    ly=models.DecimalField(max_digits = 5,decimal_places = 3)
    gx=models.DecimalField(max_digits = 5,decimal_places = 3)
    gy=models.DecimalField(max_digits = 5,decimal_places = 3)

############################
class series65(models.Model):
    skfNo=models.IntegerField(primary_key=True)
    dia=models.IntegerField()
    d1min=models.IntegerField()
    dcap=models.IntegerField()
    d2min=models.IntegerField()
    bB=models.IntegerField()
    rR=models.IntegerField()
    rR1=models.IntegerField()
    staticC=models.IntegerField()
    dynamicC=models.IntegerField()
    maxSpeed=models.IntegerField()
