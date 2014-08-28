from django.db import models

# Create your models here.


class Session(models.Model):
    email = models.CharField(max_length=200)
    age = models.IntegerField()
    nationality = models.CharField(max_length=200)
    handed = models.CharField(max_length=20)
    sing = models.BooleanField()

    # listen_indian_classical = models.BooleanField()
    # listen_bollywood = models.BooleanField()
    # listen__european_classical = models.BooleanField()
    # listen_pop = models.BooleanField()
    # listen_rock  = models.BooleanField()
    # listen_rap  = models.BooleanField()
    # listen_jazz  = models.BooleanField()
    # listen_rb = models.BooleanField()
    # listen_gospel = models.BooleanField()

    def __unicode__(self):
        return str(self.id) + " " + self.email


class Comparison(models.Model):
    session = models.ForeignKey(Session)
    left_scale = models.IntegerField()
    center_sclae = models.IntegerField()
    right_scale = models.IntegerField()
    right_direction = models.CharField(max_length=20)
    answer_correct = models.BooleanField()
    time_spent = models.FloatField()
    speed_interval = models.FloatField()
    just_intonation = models.BooleanField()
    mode = models.IntegerField()
    clicksLeft = models.IntegerField()
    clicksCenter = models.IntegerField()
    clicksRight = models.IntegerField()
    questionTime = models.IntegerField()



    def __unicode__(self):
        return str(self.session) + str(self.left_ID)  + str(self.center_ID) + str(self.right_ID)
