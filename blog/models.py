from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey('User', related_name='blogs')
    content = models.TextField(max_length=2000)
    create_time = models.DateTimeField()

    def __unicode__(self):
        return self.title


class User(models.Model):
    nick = models.CharField(max_length=24, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=32)
    type = models.IntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()

    def __unicode__(self):
        return '%s<=>%s' %(self.nick, self.email)