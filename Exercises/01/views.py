#!usr/bin/env python3
#-*- coding:utf-8 -*-
#author:Terence

from django.shortcuts import render_to_response
from models import Books

def latest_books(request):
    book_list = Book.objects.order_by('-pub_data')[:10]
    return render_to_response('latest_books.html', {'book_list': book_list})
