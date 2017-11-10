from django.shortcuts import render_to_response
# from mysite.books.models import Book
from django.http import HttpResponse
import datetime

'''
def book_list(request):
    books = Book.objects.order_by('name')
    return render_to_response('book_list.html', {'books': books})
'''


def current_datatime(request):
    time_now = datetime.datetime.now()
    return render_to_response('mypage.html', {'current_date': time_now})

'''
def display_meta(request):
    values = request.META.items()
    values = sorted(values)
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
'''

def display_meta(request):
    values = sorted(request.META.items())
    return render_to_response('display_meta.html', {'values': values, 'request': request})