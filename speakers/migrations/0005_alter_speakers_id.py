# Generated by Django 4.1 on 2022-11-02 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speakers', '0004_alter_speakers_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='speakers',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
