# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Visit'
        db.create_table(u'scaleID_visit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('age', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('nationality', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('handed', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('sing', self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'scaleID', ['Visit'])

        # Adding model 'Comparison'
        db.create_table(u'scaleID_comparison', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('visit', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scaleID.Visit'])),
            ('left_scale', self.gf('django.db.models.fields.IntegerField')()),
            ('center_sclae', self.gf('django.db.models.fields.IntegerField')()),
            ('right_scale', self.gf('django.db.models.fields.IntegerField')()),
            ('right_direction', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('answer_correct', self.gf('django.db.models.fields.BooleanField')()),
            ('time_spent', self.gf('django.db.models.fields.FloatField')()),
            ('speed_interval', self.gf('django.db.models.fields.FloatField')()),
            ('just_intonation', self.gf('django.db.models.fields.BooleanField')()),
            ('mode', self.gf('django.db.models.fields.IntegerField')()),
            ('clicksLeft', self.gf('django.db.models.fields.IntegerField')()),
            ('clicksCenter', self.gf('django.db.models.fields.IntegerField')()),
            ('clicksRight', self.gf('django.db.models.fields.IntegerField')()),
            ('questionTime', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'scaleID', ['Comparison'])


    def backwards(self, orm):
        # Deleting model 'Visit'
        db.delete_table(u'scaleID_visit')

        # Deleting model 'Comparison'
        db.delete_table(u'scaleID_comparison')


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
            'speed_interval': ('django.db.models.fields.FloatField', [], {}),
            'time_spent': ('django.db.models.fields.FloatField', [], {}),
            'visit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scaleID.Visit']"})
        },
        u'scaleID.visit': {
            'Meta': {'object_name': 'Visit'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'handed': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nationality': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sing': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['scaleID']