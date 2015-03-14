# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Attendance(models.Model):
    date = models.DateTimeField(primary_key=True)
    session_schedule_id = models.IntegerField(primary_key=True)
    attendance_status = models.CharField(max_length=1)
    student_id = models.IntegerField(primary_key=True)
    attendance_comment = models.CharField(max_length=255)
    partner_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Attendance'


class Enhancementpartner(models.Model):
    partner_id = models.IntegerField(primary_key=True)
    partner_name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'EnhancementPartner'


class Enhancementpartnerschedule(models.Model):
    partner_id = models.IntegerField(primary_key=True)
    session_schedule_id = models.IntegerField(primary_key=True)
    date = models.DateField(primary_key=True)
    comment = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'EnhancementPartnerSchedule'


class Program(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    zone_id = models.IntegerField()
    program_description = models.CharField(max_length=200)
    interval_code = models.IntegerField(db_column='Interval_code')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Program'


class School(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    district_id = models.IntegerField()
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'School'


class Session(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    program_id = models.IntegerField()
    session_description = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Session'


class Sessioncanceldate(models.Model):
    session_schedule_id = models.IntegerField(primary_key=True)
    date = models.DateTimeField(primary_key=True)
    comment = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'SessionCancelDate'


class Sessionforstudent(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    session_schedule_id = models.IntegerField()
    student_id = models.IntegerField(db_column='Student_id')  # Field name made lowercase.
    effective_date = models.DateField()
    ending_date = models.IntegerField()
    date_stamp = models.DateField()

    class Meta:
        managed = False
        db_table = 'SessionForStudent'


class Sessionschedule(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    session_id = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    school_year = models.IntegerField()
    comments = models.CharField(max_length=255)
    teacher_id = models.IntegerField()
    location = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'SessionSchedule'


class Student(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    local_student_id = models.IntegerField()
    school_id = models.IntegerField()
    last_name = models.CharField(max_length=35)
    first_name = models.CharField(max_length=35)
    middle_name = models.CharField(max_length=35)
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    gender = models.CharField(max_length=1)
    grade_level = models.CharField(max_length=2)
    location_type_id = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    date_stamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Student'


class Teacher(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    last_name = models.CharField(max_length=35)
    first_name = models.CharField(max_length=35)
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'Teacher'


class Zone(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    zone_description = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'Zone'

''' maybe used later for auth groups
class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
'''