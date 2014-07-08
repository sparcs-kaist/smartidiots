from django.db import models
from apps.member.models import Member

# Create your models here.

class Seminar(models.Model):
    # Presentor
    presentor = models.ForeignKey(Member, related_name="seminars_done") # Presentor of a seminar
    referers = models.ManyToManyField(Member, related_name="seminars_refered") # People refered to a seminar

    # Seminar Information
    title = models.CharField(max_length=255, db_index=True) # Title of a seminar
    date = models.DateField(auto_now=True) # Date performed of a seminar
    resource = models.FileField(upload_to='/seminars/') # Seminar file
    sequel = models.ForeignKey('Sequel', related_name="series", null=True, blank=True) # Sequel to a seminar

    # Seminar Track & Category
    track = models.ForeignKey('Track', related_name="seminars") # Broad category
    category = models.ForeignKey('Category', related_name="seminars") # Detailed category


class Sequel(models.Model):
    presentor = models.ForeignKey(Member, related_name="seminar_sequals") # Presentor of a sequel
    title = models.CharField(max_length=255, db_index=True) # title of a sequel


'''
Example of Tracks: Newbie, Wheel, Informative, Development, Design, etc.
'''
class Track(models.Model):
    name = models.CharField(max_length=255, db_index=True) # Name of broad category
    description = models.CharField(max_length=255) # Brief description


'''
Example of Categories: Framework, VCS, Android, iOS, Hardware, Server, etc.
'''
class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True) # Name of detailed category
    description = models.CharField(max_length=255) # Brief description
