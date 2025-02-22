from django.db import models

class Login(models.Model):
    userid=models.CharField(max_length=50,primary_key=True)
    password=models.CharField(max_length=20)
    usertype=models.CharField(max_length=50)

class Team(models.Model):
    tmname=models.CharField(max_length=100)
    tmwork=models.TextField()
    tmaddress=models.TextField()
    tmcontactno=models.CharField(max_length=15)
    tmemailaddress=models.EmailField(max_length=50,primary_key=True)
    aadharno=models.CharField(max_length=12)
    panno=models.CharField(max_length=10)
    regdate=models.CharField(max_length=20)

class Normal(models.Model):
    name=models.CharField(max_length=100)
    cpname=models.CharField(max_length=50)
    cpcontactno=models.CharField(max_length=15)
    cpemailaddress=models.EmailField(max_length=50,primary_key=True)
    gstno=models.CharField(max_length=15)
    regdate=models.CharField(max_length=20)

class News(models.Model):
    newstext=models.TextField()
    newsdate=models.CharField(max_length=30)