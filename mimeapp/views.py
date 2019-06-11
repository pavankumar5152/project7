from django.shortcuts import render
from django.http import HttpResponse
from reportlab.pdfgen import canvas
import csv
data = """<table><tr><th>eid</th><ename</th><th>esal</th></tr><tr><td>1001</td><td>pavan</td><td>30000</td></tr>
  <tr><td>1001</td><td>pavan</td><td>30000</td></tr><tr><td>1001</td><td>pavan</td><td>30000</td></tr></table>"""
def csvviews(request):
    response = HttpResponse(content_type="text/csv")
    response['content_Disposition'] = 'attachment:filename="myfile"'
    write=csv.writer(response)
    write.writerrow(['firstrow','foo','br','baz'])
    write.writerrow(['secondrow','A','B','C','Testing'])
def pdfviews(request):
    responce=HttpResponse(content_type='application/pdf')
    responce['content_disposition']='attachment:filename ="myfile"'
    p=canvas.canvas(responce)
    p.drawsrting(100,100,"hello word")
    p.save()
    return responce
def htmlviews(request):
    return HttpResponse(data,content_type="text/html")
def xmlviews(request):
    return HttpResponse(data,content_type="application/xml")


