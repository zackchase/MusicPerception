# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Session.listen_rb'
        db.delete_column(u'scaleID_session', 'listen_rb')

        # Deleting field 'Session.listen_rap'
        db.delete_column(u'scaleID_session', 'listen_rap')

        # Deleting field 'Session.listen_rock'
        db.delete_column(u'scaleID_session', 'listen_rock')

        # Deleting field 'Session.listen_jazz'
        db.delete_column(u'scaleID_session', 'listen_jazz')

        # Deleting field 'Session.listen_gospel'
        db.delete_column(u'scaleID_session', 'listen_gospel')

        # Deleting field 'Session.listen_indian_classical'
        db.delete_column(u'scaleID_session', 'listen_indian_classical')

        # Deleting field 'Session.listen__european_classical'
        db.delete_column(u'scaleID_session', 'listen__european_classical')

        # Deleting field 'Session.listen_bollywood'
        db.delete_column(u'scaleID_session', 'listen_bollywood')

        # Deleting field 'Session.listen_pop'
        db.delete_column(u'scaleID_session', 'listen_pop')


    def backwards(self, orm):
        # Adding field 'Session.listen_rb'
        db.add_column(u'scaleID_session', 'listen_rb',
                      self.gf('django.db.models.fields.BooleanField')(default=0),
                      keep_default=False)

        # Adding field 'Session.listen_rap'
        db.add_column(u'scaleID_session', 'listen_rap',
                      self.gf('django.db.models.fields.BooleanField')(default=0),
                      keep_default=False)

        # Adding field 'Session.listen_rock'
        db.add_column(u'scaleID_session', 'listen_rock',
                      self.gf('django.db.models.fields.BooleanField')(default=0),
                      keep_default=False)

        # Adding field 'Session.listen_jazz'
        db.add_column(u'scaleID_session', 'listen_jazz',
                      self.gf('django.db.models.fields.BooleanField')(default=0),
                      keep_default=False)

        # Adding field 'Session.listen_gospel'
        db.add_column(u'scaleID_session', 'listen_gospel',
                      self.gf('django.db.models.fields.BooleanField')(default=0),
                      keep_default=False)

        # Adding field 'Session.listen_indian_classical'
        db.add_column(u'scaleID_session', 'listen_indian_classical',
                      self.gf('django.db.models.fields.BooleanField')(default=0),
                      keep_default=False)

        # Adding field 'Session.listen__european_classical'
        db.add_column(u'scaleID_session', 'listen__european_classical',
                      self.gf('django.db.models.fields.BooleanField')(default=0),
                      keep_default=False)

        # Adding field 'Session.listen_bollywood'
        db.add_column(u'scaleID_session', 'listen_bollywood',
                      self.gf('django.db.models.fields.BooleanField')(default=0),
                      keep_default=False)

        # Adding field 'Session.listen_pop'
        db.add_column(u'scaleID_session', 'listen_pop',
                      self.gf('django.db.models.fields.BooleanField')(default=0),
                      keep_default=False)


    models = {
        u'scaleID.comparison': {
            'Meta': {'object_name': 'Comparison'},
            'answer_correct': ('django.db.models.fields.BooleanField', [], {}),
            'center_sclae': ('django.db.models.fields.IntegerField', [], {}),
            'clicksCenter': ('django.db.models.fields.IntegerField', [], {}),
            'clicksLeft': ('django.db.models.fields.IntegerField', [], {}),
            'clicksRight': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'just_intonation': ('django.db.models.fields.BooleanField', [], {}),
            'left_scale': ('django.db.models.fields.IntegerField', [], {}),
            'mode': ('django.db.models.fields.IntegerField', [], {}),
            'questionTime': ('django.db.models.fields.IntegerField', [], {}),
            'right_direction': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'right_scale': ('django.db.models.fields.IntegerField', [], {}),
            'session': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scaleID.Session']"}),
            'speed_interval': ('django.db.models.fields.FloatField', [], {}),
            'time_spent': ('django.db.models.fields.FloatField', [], {})
        },
        u'scaleID.session': {
            'Meta': {'object_name': 'Session'},
            'age': ('django.db.models.fields.IntegerField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'handed': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sing': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['scaleID']