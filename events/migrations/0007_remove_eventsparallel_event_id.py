# Generated by Django 4.1 on 2022-10-30 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_eventsparallel_event_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventsparallel',
            name='event_id',
        ),
    ]