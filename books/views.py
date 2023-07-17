import logging
import base64
import sys
import datetime, json
from datetime import datetime, timedelta , time
from json import JSONEncoder
import json
from decimal import Decimal
from django.utils.dateparse import parse_date

from decimal import Decimal
from django.db.models import Sum
from django.shortcuts import render , redirect
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import Group
from django.template import Context, Template
from django.utils.decorators import method_decorator
from django.forms.models import model_to_dict
from django.contrib import messages
from django.core.paginator import EmptyPage, InvalidPage, Paginator
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.translation import get_language
from django.contrib.auth.models import User


from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from .models import Library


class Home(View):
    template_name = "home.html"
    def get(self , request):
        print("HOMEEEE")

        lib_data = []

        lib = Library.objects.all()

        for ht in lib:
            data = {
                "id" : ht.id,
                "sno" : ht.sno,
                "name" : ht.name,
                "author" : ht.author,
                "title" : ht.title,
                "number" : ht.number,
            }

            lib_data.append(data)

        context = {
            'lib' : lib_data,
            'all_lib' : json.dumps(list(lib_data))
        }

        return render(request , self.template_name , context)
    
    def post(self , request):

        print("INNNNSIDE POST")

        lib_id = request.POST.get('lib_id')

        # db_param = {
        #     "sno" : request.POST.get('sno'),
        #     "name" : request.POST.get('name'),
        #     "author" : request.POST.get('author'),
        #     "title" : request.POST.get('title'),
        #     "number" : request.POST.get('number'),
        # }

        db_param = request.POST.dict()

        del db_param['csrfmiddlewaretoken']
        del db_param['lib_id']

        print("DB Param = ",db_param)        

        if(lib_id == '0'):
            print("New")
            db_param['created_time'] = datetime.now()
            Library.objects.create(**db_param)
            return redirect('home')
        else:
            print("Update")
            db_param['updated_time'] = datetime.now()
            Library.objects.filter(id = int(lib_id)).update(**db_param)

            return redirect('home')

