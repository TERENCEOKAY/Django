#!usr/bin/env python3
#-*- coding:utf-8 -*-
#author: Terence


from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from mysite.books.models import Book
from django.core.mail import send_mail
from mysite.contact.forms import ContactForm
# from django.views.decorators.csrf import csrf_exempt

# def search_form(request):
#     return render_to_response('search_form.html')

'''
def search(request):
    if 'q' in request.GET and request.GET['q']:
        # message = 'You search for: %r' % request.GET['q']
        q = request.GET['q']
        books = Book.objects.filter(title__icontains=q)
        return render_to_response('search_result.html', {'books': books, 'query': q})

    else:
        return render_to_response('search_form.html', {'error': True})

        # message = 'No books submit your search.'
    # return HttpResponse(message)
'''

'''
def search(request):
    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
'''


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Please enter a search term')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_result.html', {'books': books, 'query': q})

    return render_to_response('search_form.html', {'errors': errors})

'''
def contact(request):

    errors = []
    if request.method == 'POST':


        if not request.POST.get('subject', ''):
            errors.append('Please enter a subject')
        if not request.POST.get('message', ''):
            errors.append('Please enter a message')
        if request.POST.get('email') and '@' not in request.POST['email']:
            errors.append('Please enter a valid e-mail address')
        if not errors:
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                request.POST.get('email', 'zwhuang@tigresstech.com'),
                ['to@example.com'],
            )
            return HttpResponseRedirect('/contact/thanks/')



    return render(request, 'contact_form.html',
                  {'errors': errors,
                  'subject': request.POST.get('subject', ''),
                   'message': request.POST.get('message', ''),
                   'email': request.POST.get('email', '')})
'''

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'zwhuang@tigresstech.com'),
                ['781938094@qq.com']
            )
            return HttpResponseRedirect('/contact/thanks/')

    else:
        form = ContactForm(initial={'subject': '请输入您的主题'})

    return render_to_response('contact_form.html', {'form': form})
    # / Users / zwhuang / Documents / Python / Django / djcode / mysite / mysite / templates /

def thanks(request):
    return render_to_response('thanks.html')