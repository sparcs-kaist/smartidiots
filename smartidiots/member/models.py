from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

class Member(models.Model):
    # SPARCS Info
    sparcsid = models.CharField(max_length=255,primary_key=True,db_index=True) # SPARCS ID

    # Personal Info
    name_kr = models.CharField(max_length=255,db_index=True) # Korean name
    name_en = models.CharField(max_length=255,db_index=True) # English name
    birthday = models.CharField(max_length=40) # Birthday : 1993.01.01
    gender = models.SmallIntegerField() # 0 for male, 1 for female

    # Contact Info
    phone = models.CharField(max_length=40) # Phone Number +821012345678
    email = models.CharField(max_length=255,db_index=True) # External Email Address : example@gmail.com
    address = models.CharField(max_length=255) # Address
    blog = models.CharField(max_length=255) # Blog URL
    company = models.CharField(max_length=255) # Company Name
    kaist_admission_year = models.IntegerField(db_index=True,validators=[MinValueValidator(1900)]) # KAIST Admission Year : 2011
    sparcs_admission_year = models.IntegerField(db_index=True) # SPARCS Admission Year : 2012
    major = models.CharField(max_length=255,db_index=True) # Major : Computer Science, Industrial Design

    # Social Services Info
    twitter = models.CharField(max_length=255) # Twitter ID
    facebook = models.CharField(max_length=255) # Facebook ID
    googleplus = models.CharField(max_length=255) # Google+ ID
    github = models.CharField(max_length=255) # Github ID

    # Extra Info
    description = models.CharField(max_length=255) # Short Description
    introduction = models.TextField() # Self Introduction
    extra = models.CharField(max_length=255) # Extra Field

    # Categories
    categories = models.ManyToManyField('Category') # N:N Relationship with Category


class Skill(models.Model):
    member = models.ForeignKey(Member) # Owner of skill
    name = models.CharField(max_length=255) # Name of skill : Django, Python, Javascript, etc..
    value = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)]) # percentage value of skill

class Category(models.Model):
    name = models.CharField(max_length=255,db_index=True) # Name of Category : Web Developer, iOS Developer
    description = models.CharField(max_length=255) # Short Description of category
