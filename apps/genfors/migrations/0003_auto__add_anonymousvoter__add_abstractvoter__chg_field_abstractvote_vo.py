# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AnonymousVoter'
        db.create_table(u'genfors_anonymousvoter', (
            (u'abstractvoter_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['genfors.AbstractVoter'], unique=True, primary_key=True)),
            ('user_hash', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'genfors', ['AnonymousVoter'])

        # Adding model 'AbstractVoter'
        db.create_table(u'genfors_abstractvoter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meeting', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['genfors.Meeting'])),
        ))
        db.send_create_signal(u'genfors', ['AbstractVoter'])


        # Changing field 'AbstractVote.voter'
        db.alter_column(u'genfors_abstractvote', 'voter_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['genfors.AbstractVoter']))
        # Deleting field 'RegisteredVoter.meeting'
        db.delete_column(u'genfors_registeredvoter', 'meeting_id')

        # Deleting field 'RegisteredVoter.id'
        db.delete_column(u'genfors_registeredvoter', u'id')

        # Adding field 'RegisteredVoter.abstractvoter_ptr'
        db.add_column(u'genfors_registeredvoter', u'abstractvoter_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['genfors.AbstractVoter'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'AnonymousVoter'
        db.delete_table(u'genfors_anonymousvoter')

        # Deleting model 'AbstractVoter'
        db.delete_table(u'genfors_abstractvoter')


        # Changing field 'AbstractVote.voter'
        db.alter_column(u'genfors_abstractvote', 'voter_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['genfors.RegisteredVoter']))
        # Adding field 'RegisteredVoter.meeting'
        db.add_column(u'genfors_registeredvoter', 'meeting',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['genfors.Meeting']),
                      keep_default=False)

        # Adding field 'RegisteredVoter.id'
        db.add_column(u'genfors_registeredvoter', u'id',
                      self.gf('django.db.models.fields.AutoField')(default=1, primary_key=True),
                      keep_default=False)

        # Deleting field 'RegisteredVoter.abstractvoter_ptr'
        db.delete_column(u'genfors_registeredvoter', u'abstractvoter_ptr_id')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'authentication.onlineuser': {
            'Meta': {'ordering': "['first_name', 'last_name']", 'object_name': 'OnlineUser'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'allergies': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'compiled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'field_of_study': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'default': "'male'", 'max_length': '10'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'infomail': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'mark_rules': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'ntnu_username': ('django.db.models.fields.CharField', [], {'max_length': '10', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'rfid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'started_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2014, 3, 18, 0, 0)'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '4', 'null': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'genfors.abstractvote': {
            'Meta': {'object_name': 'AbstractVote'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['genfors.Question']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'voter': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['genfors.AbstractVoter']"})
        },
        u'genfors.abstractvoter': {
            'Meta': {'object_name': 'AbstractVoter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meeting': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['genfors.Meeting']"})
        },
        u'genfors.alternative': {
            'Meta': {'object_name': 'Alternative'},
            'alt_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['genfors.Question']"})
        },
        u'genfors.anonymousvoter': {
            'Meta': {'object_name': 'AnonymousVoter', '_ormbases': [u'genfors.AbstractVoter']},
            u'abstractvoter_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['genfors.AbstractVoter']", 'unique': 'True', 'primary_key': 'True'}),
            'user_hash': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        },
        u'genfors.booleanvote': {
            'Meta': {'object_name': 'BooleanVote', '_ormbases': [u'genfors.AbstractVote']},
            u'abstractvote_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['genfors.AbstractVote']", 'unique': 'True', 'primary_key': 'True'}),
            'answer': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'})
        },
        u'genfors.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'ended': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_locked': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'genfors.multiplechoice': {
            'Meta': {'object_name': 'MultipleChoice', '_ormbases': [u'genfors.AbstractVote']},
            u'abstractvote_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['genfors.AbstractVote']", 'unique': 'True', 'primary_key': 'True'}),
            'answer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['genfors.Alternative']", 'null': 'True', 'blank': 'True'})
        },
        u'genfors.question': {
            'Meta': {'object_name': 'Question'},
            'anonymous': ('django.db.models.fields.BooleanField', [], {}),
            'created_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'locked': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'meeting': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['genfors.Meeting']"}),
            'only_show_winner': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'question_type': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'result': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'genfors.registeredvoter': {
            'Meta': {'object_name': 'RegisteredVoter', '_ormbases': [u'genfors.AbstractVoter']},
            u'abstractvoter_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['genfors.AbstractVoter']", 'unique': 'True', 'primary_key': 'True'}),
            'can_vote': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['authentication.OnlineUser']"})
        }
    }

    complete_apps = ['genfors']