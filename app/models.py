from django.db import models
from django.contrib.auth.models import User

# Models of drScratch

class File(models.Model):
    filename = models.CharField(max_length=100)
    method = models.CharField(max_length=100)
    time = models.TextField()
    language = models.TextField(default="en")
    score = models.IntegerField()
    abstraction = models.IntegerField()
    parallelization = models.IntegerField()
    logic = models.IntegerField()
    synchronization = models.IntegerField()
    flowControl = models.IntegerField()
    userInteractivity = models.IntegerField()
    dataRepresentation = models.IntegerField()
    spriteNaming = models.IntegerField()
    initialization = models.IntegerField()
    deadCode = models.IntegerField()
    duplicateScript = models.IntegerField()

class Student(models.Model):
    student = models.ForeignKey(User, unique=True)  

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    #student = models.ManyToManyField(Student)


class Teacher(models.Model):
    teacher = models.ForeignKey(User, unique=True)
    username = models.TextField()
    password = models.TextField()
    email = models.TextField()
    hashkey = models.TextField()
    #classroom = models.ManyToManyField(Classroom)


class Organization(models.Model):
    name = models.TextField()
    email = models.TextField()
    password = models.TextField()
    hashkey = models.TextField()

    def __str__(self):
        return self.name + " " + self.email + " " + self.password + " " + self.hashkey

class Dashboard(models.Model):
	user = models.TextField()
	frelease = models.DateField()

class Project(models.Model):
	name = models.TextField()
	version = models.IntegerField()
	score = models.IntegerField()
	level = models.TextField()
	path = models.TextField()
	fupdate = models.TextField()
	dashboard = models.ForeignKey(Dashboard)
	
class Attribute(models.Model):
	myproject = models.ForeignKey(Project)
	character = models.TextField()
	orientation = models.IntegerField()
	position = models.IntegerField()
	costume = models.IntegerField()
	visibility = models.IntegerField()
	size = models.IntegerField()

class Dead(models.Model):
	myproject = models.ForeignKey(Project)
	character = models.TextField()
	blocks = models.IntegerField()

class Duplicate(models.Model):
	myproject = models.ForeignKey(Project)
	numduplicates = models.IntegerField()

class Sprite(models.Model):
	myproject = models.ForeignKey(Project)
	character = models.TextField()

class Mastery(models.Model):
	myproject = models.ForeignKey(Project)
	abstraction = models.IntegerField()
	paralel = models.IntegerField()
	logic = models.IntegerField()
	synchronization = models.IntegerField()
	flowcontrol = models.IntegerField()
	interactivity = models.IntegerField()
	representation = models.IntegerField()
	scoring = models.IntegerField()	

class Comment(models.Model):
	user = models.TextField()
	text = models.TextField()
	date = models.DateField()

class Activity(models.Model):
	text = models.TextField()
	date = models.DateField()
class Hashkey(models.Model):
    hashkey = models.TextField()
    def __str__(self):
        return self.hashkey

