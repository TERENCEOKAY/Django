#!usr/bin/env python3
#-*- coding:utf-8 -*-
#author:Terence

from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=50)
    pub_data = models.DateField()