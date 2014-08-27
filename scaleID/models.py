from django.db import models

# Create your models here.


class Session(models.Model):
    email = models.CharField(max_length=200)
    age = models.IntegerField()
    nationality = models.CharField()
    handed = models.CharField(max_length=20)
    sing = models.BooleanField()

    listen_classical = models.BooleanField()
    listen_pop  = models.BooleanField()
    listen_rock  = models.BooleanField()
    listen_rap  = models.BooleanField()
    listen_jazz  = models.BooleanField()
    listen_rb = models.BooleanField()
    listen_indian_classical = models.BooleanField()
    listen_singer_songwriter = models.BooleanField()
    listen_gospel = models.BooleanField()

    def __unicode__(self):
        return str(self.id) + " " + self.email


class Comparison(models.Model):
    session = models.ForeignKey(Session)
    left_ID = models.IntegerField()
    center_ID = models.IntegerField()
    right_ID = models.IntegerField()
    guess = models.CharField(max_length=20)
    time_spent = models.FloatField()
    just_intonation = models.BooleanField()
    mode = models.IntegerField()
    speed_interval = models.FloatField()


    # num clicks left
    # num clicks center
    # num clicks right
    # time left
    # time center
    # time right
    # total time on question



    def __unicode__(self):
        return str(self.session) + str(self.left_ID)  + str(self.center_ID) + str(self.right_ID)
