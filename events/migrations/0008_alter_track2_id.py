# Generated by Django 4.1 on 2022-10-30 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_remove_eventsparallel_event_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track2',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]