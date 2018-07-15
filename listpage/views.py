from django.http import HttpResponse
from django.shortcuts import render_to_response,render, redirect
import requests
##from .mdr import region_to_dict,Region
##from .dep import Depta
from joblist.mdr import region_to_dict,Region
from joblist.dep import Depta
import os
import time
from .models import JobList

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_joblist(request):

   body='''
    <title>Crawler</title>

    <form method="GET">
    <input id="user_in" name="url" style="border:1px solid #000000;" placeholder="Enter joblist url here "> 
    <button type="submit" style="height: 20px;" style="border:1px solid #000000;">Submit</button>
    <br>
    </form>'''

   
   _url=request.GET.get('url','')
   html=None
   if _url:
       d = Depta()
       print _url
       seeds = d.extract(url=_url)
       if seeds is not None:
           result=None
           for seed in seeds:
               table = seed.as_html_table()
               if table is not None:
                   result=table
           if result:
                html=result
                    
       #r = requests.get(url,timeout=60)
       #html=r.content
   if _url and html:
       obj=JobList()
       obj.url=_url
       obj.data=html
       obj.publish()

   return HttpResponse("<html>%s<br><div>%s</div></html>"%(body,html))
   #return render_to_response("search/htmlsearch.html",{'url':_url,'html':html})
