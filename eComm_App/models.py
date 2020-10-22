from django.db import models
from phone_field import PhoneField
from django.contrib import messages
import re

# Validators below.

class UserManager(models.Manager):
    def regValid(self, post):
        # Errors dictionary:
        errors = {}
        # Username lookup:
        userMatch = User.objects.filter(username= post['uName'])
        # Email regex:
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # Start of validation:
        # **************************
        # first name
        if len(post['fname']) == 0:
            errors['fnameREQ'] = 'First name is required.'
        if len(post['fname']) < 3:
            errors['fnameChar'] = 'First name requires atleast 3 characters.'
        # Last name
        if len(post['lname']) == 0:
            errors['lnameREQ'] = 'Last name is required.'
        if len(post['lname']) < 3:
            errors['lnameChar'] = 'Last name requires atleast 3 characters.'
        # username
        if len(post['uName']) == 0:
            errors['uNameREQ'] = "Username is required."
        elif len(post['uName']) < 3:
            errors['uNameChar'] = "Username must be atleast 3 characters."
        elif len(userMatch) > 0:
            errors['matchUser'] = 'This username is already taken.'
        # password
        if len(post['pw']) == 0:
            errors['pwreq'] = "Password is required."
        elif len(post['pw']) < 3:
            errors['pwLenreq'] = "Password must be atleast 3 characters."
        elif post['pw'] != post['cpw']:
            errors['confirmpw'] = "Password does not match !"
        # email
        if len(post['email']) == 0:
            errors['emailREQ'] = 'Email is required.'
        elif not EMAIL_REGEX.match(postData['rEmail']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        # phone
        return errors

    def logValid(self, post):
        # Errors Dictionary:
        errors = {}
        # Username lookup:
        userMatch = User.objects.filter(username= post['uName'])
        # Start of validation:
        # ****************************
        # Username
        if len(post['uName']) == 0:
            errors['userReq'] = "Username is required."
        elif len(userMatch) == 0:
            errors['userNo'] = 'No matching username !!'
        else:
            if userMatch[0].password != post['pwd']:
                errors['badPw'] = "Invalid password !!"
        return errors



# Models below.
class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager

class Product(models.Model):
    itemName = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    cart = models.ManyToManyField(User, related_name="addCart")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

