from django.urls import path
from . import views
appname = "mimeapp"
urlpatterns = [
    path('csv',views.csvviews),
    path('pdf',views.pdfviews),
    path('html',views.htmlviews),
    path('xml',views.xmlviews),
]