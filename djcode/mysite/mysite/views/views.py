# from django.http import HttpResponse, Http404
  datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
import psycopg2


def hello(request):
    return HttpResponse("Hello World!")

def my_home_page_view(request):
    return HttpResponse("Here is Terence's Zone!")

def current_datatime(request):
    time_now = datetime.datetime.now()

    '''
    # fp = open('mysite/templates/current_datetime.html')
    # rn = fp.read()
    # t = Template(rn)
    t = get_template('current_datetime.html')
    # c = Context({'current_time': time_now})
    html = t.render({'current_time': time_now})

    # html = "<html><body>It is %s.<body><html>" % time_now
    return HttpResponse(html)
    '''

    return render_to_response('current_datetime.html', {'current_time': time_now})


def hours_ahead(request, offset):
    offset = int(offset)
    time_later = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # assert False

    '''
    t = get_template('hours_ahead.html')
    # c = Context({'hours': offset, 'later_time': time_later})
    html = t.render({'hours': offset, 'later_time': time_later})

    # html = "<html><body>In %s hour(s),it will be %s.<body><html>" % (offset, time_later)
    return HttpResponse(html)
    '''

    return render_to_response('hours_ahead.html', {'hours':offset, 'time_later':time_later})


def book_list(request):
    db = psycopg2.connect(user='Terence',database='mydb', password='weigehaoshuai', host='192.168.199.204')
    cursor = db.cursor()
    cursor.execute('SELECT name FROM books ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render_to_response('book_list.html', {'names': names})
