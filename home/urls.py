from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("homelogout", views.homelogout, name="homelogout"),
   
    path("mscsform", views.mscsform, name='mscsform'),
    path("formlogout", views.formlogout, name='formlogout'),

    path("formi", views.formi, name="form-i"),
     path("formilogout", views.formilogout, name='formilogout'),

    path("formii", views.formii, name="form-ii"),
    path("formiilogout", views.formiilogout, name="form-iilogout"),

    path("formiii", views.formiii, name="form-iii"),
    path("formiiilogout", views.formiiilogout, name="form-iiilogout"),

    path("formiv", views.formiv, name="form-iv"),
    path("formivlogout", views.formivlogout, name="form-ivlogout"),

    path("formv", views.formv, name="form-v"),
    path("formvlogout", views.formvlogout, name="form-vlogout"),


    path("mscslogin", views.mscslogin, name='mscslogin'),
    path("mscsloginlogout", views.mscsloginlogout, name='mscsloginlogout'),

    path("registration", views.registration, name='registration'),
    path("form", views.form, name='form'),

   

    path("adminlogin", views.adminlogin, name='adminlogin'),

    path("mscsact", views.mscsact, name='mscsact'),
    path("mscsactlogout", views.mscsactlogout, name='mscsactlogout'),

    path("checklist", views.checklist, name='checklist'),
    path("checklistlogout", views.checklistlogout, name='checklistlogout'),

    path("modelbye", views.modelbye, name='modelbye'),
    path("modelbyelogout", views.modelbyelogout, name='modelbyelogout'),

    path("logoutuser", views.logoutuser, name='logoutuser'),

    # path("login", views.loginuser, name="loginuser"),
    # path("loginuser", views.loginuser, name="loginuser"),

    path("regS", views.regS, name="regS"),
    path("regSlogout", views.regSlogout, name="regSlogout"),


    path("chartslogout", views.chartslogout, name="chartslogout"),
    path("chart1logout", views.chart1logout, name="chart1logout"),
    path("chart1", views.chart1, name="chart1"),
    path("chart2logout", views.chart2logout, name="chart2logout"),
    path("chart2", views.chart2, name="chart2"),
    path("chart3logout", views.chart3logout, name="chart3logout"),
    path("chart3", views.chart3, name="chart3"),

    path("contact", views.contact, name="contact"),
    path("contactlogout", views.contactlogout, name="contactlogout"),
    path("grievance", views.grievance, name="grievance"),
    path("grievance2", views.grievance2, name="grievance2"),
    path("grievanceform", views.grievanceform, name="grievanceform"),
    path("grievanceformlogout", views.grievanceformlogout, name="grievanceformlogout"),

    path("statewise", views.statewise, name="statewise"),
    path("statewiselogout", views.statewiselogout, name="statewiselogout"),
    path("registrars", views.registrars, name="registrars"),
    path("registrarslogout", views.registrarslogout, name="registrarslogout"),

    path("feedbackform", views.feedbackform, name="feedbackform"),
    path("feedbackformlogout", views.feedbackformlogout, name="feedbackformlogout"),
    path("feedback", views.feedback, name="feedback"),
    path("feedback2", views.feedback2, name="feedback2"),

    path("related", views.related, name="related"),
    path("relatedlogout", views.relatedlogout, name="relatedlogout"),

    path("societies", views.societies, name="societies"),
    path("societieslogout", views.societieslogout, name="societieslogout"),

    path("disclaimer", views.disclaimer, name="disclaimer"),
    path("disclaimerlogout", views.disclaimerlogout, name="disclaimerlogout"),



    





    

]
