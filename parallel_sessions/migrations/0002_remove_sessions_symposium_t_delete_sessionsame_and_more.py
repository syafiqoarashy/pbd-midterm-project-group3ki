# Generated by Django 4.1 on 2022-11-03 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parallel_sessions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessions',
            name='symposium_T',
        ),
        migrations.DeleteModel(
            name='SessionsAME',
        ),
        migrations.DeleteModel(
            name='SessionsBBE',
        ),
        migrations.DeleteModel(
            name='SessionsCPE',
        ),
        migrations.DeleteModel(
            name='SessionsECE',
        ),
        migrations.DeleteModel(
            name='SessionsIE',
        ),
        migrations.DeleteModel(
            name='SessionsISBE',
        ),
        migrations.DeleteModel(
            name='SessionsIT',
        ),
        migrations.DeleteModel(
            name='SessionsMME',
        ),
        migrations.DeleteModel(
            name='SessionsSBCC',
        ),
        migrations.DeleteModel(
            name='SessionsSCE',
        ),
        migrations.DeleteModel(
            name='Sessions',
        ),
    ]