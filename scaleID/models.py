from django.db import models

# Create your models here.


class Visit(models.Model):
    email = models.CharField(max_length=200)
    age = models.IntegerField(null=True)
    nationality = models.CharField(max_length=200)
    handed = models.CharField(max_length=20)
    sing = models.NullBooleanField(null=True)

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
        return "Visit #" + str(self.id) + ", " + self.email


class Comparison(models.Model):
    visit = models.ForeignKey(Visit)
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
