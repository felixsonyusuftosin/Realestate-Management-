# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
Default_serializer = 1
# Create your models here.
