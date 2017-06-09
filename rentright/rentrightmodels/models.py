# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
Default_serializer = 1
# Create your models here.
class identifier(models.Model):
    user = models.OneToOneField(User, unique = True,related_name = "pk5i+")
    age = models.IntegerField(blank = True, null= True)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True) 
    gender = models.CharField(max_length=10, blank=True, null=True) 
    email= models.CharField(max_length=100,blank=True, null=True)
    phone_number= models.CharField(max_length=50,blank=True, null=True)
    address = models.CharField(max_length=2000,blank=True, null=True)     
    profile_picture = models.ImageField(upload_to = 'rentrightusers/%Y/%m/%d',blank = True, null = True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(User,related_name = "pki6+")
    user_logs = models.ForeignKey('user_logs',blank = True, null= True)
    def __unicode__(self):
        return '%s ' %(self.first_name)
    class Meta:   
        verbose_name = 'Identifier'
class locations(models.Model):
    identifier = models.ForeignKey(identifier,blank = True, null= True)
    user = models.ForeignKey(User,related_name = "pki6+" , blank = True, null = True)
    longitude = models.DecimalField(max_digits=100,decimal_places=20, blank=True, null=True )
    latitude = models.DecimalField(max_digits=100,decimal_places=20, blank=True, null=True )
    created_at = models.DateTimeField(auto_now_add = True)
    state = models.CharField(max_length=2000,blank=True, null=True)
    community = models.CharField(max_length=2000,blank=True, null=True)
    address = models.CharField(max_length=2000,blank=True, null=True)
    def __unicode__(self):
        return '%s ' %(self.locations)
    class Meta:   
        verbose_name = 'Locations'
class reviews(models.Model):
    identifier = models.ForeignKey(identifier,blank = True, null= True)
    user = models.ForeignKey(User,related_name = "pki7+", blank = True, null = True)
    rating = models.IntegerField(blank=True, null=True )
    comment = models.CharField(max_length=2000,blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(blank = True,null = True)
    def __unicode__(self):
        return '%s ' %(self.comment)
    class Meta:   
        verbose_name = 'Reviews'
class user_logs(models.Model):
    activity = models.CharField(max_length=2000,blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(blank = True,null = True)
    def __unicode__(self):
        return '%s ' %(self.user.first_name)
    class Meta:   
        verbose_name = 'User Logs'
class occupants(models.Model):
    identifier = models.ForeignKey(identifier,blank = True, null= True)
    user = models.ForeignKey(User,related_name = "pki9+", blank = True, null = True)
    status = models.CharField(max_length =20, default = "active", blank=True, null=True) 
    properties= models.ForeignKey('properties',blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add = True)
    tenancy_start = models.DateTimeField(blank = True,null = True)
    tenancy_end  = models.DateTimeField(blank = True,null = True)
    def __unicode__(self):
        return '%s ' %(self.user.first_name)
    class Meta:   
        verbose_name = 'Occupants'
class properties(models.Model):
    identifier = models.ForeignKey(identifier,blank = True, null= True)
    manager = models.ForeignKey(User,related_name = "pki1q2+", blank = True, null = True)
    status = models.CharField(max_length =20, default = "active", blank=True, null=True) 
    availability= models.CharField(max_length=20,blank=True, null=True)
    description= models.CharField(max_length=2000,blank=True, null=True)
    cost = models.IntegerField(blank = True, null= True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(blank = True,null = True)
    address = models.CharField(max_length=2000,blank=True, null=True)
    state = models.CharField(max_length=2000,blank=True, null=True)
    community = models.CharField(max_length=2000,blank=True, null=True)
    properties_log= models.ForeignKey('properties_log',blank=True, null=True)
    def __unicode__(self):
        return '%s ' %(self.manager.first_name)
    class Meta:   
        verbose_name = 'Properties'
class properties_log(models.Model):
    identifier = models.ForeignKey(identifier,blank = True, null= True)
    user = models.ForeignKey(User,related_name = "pkihj2+", blank = True, null = True)
    cost = models.IntegerField(blank = True, null= True)
    activity = models.CharField(max_length=2000,blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add = True)
    event_date = models.DateTimeField(blank = True, null = True)
    def __unicode__(self):
        return '%s ' %(self.activities)
    class Meta:   
        verbose_name = 'Properties Log'
        
    



