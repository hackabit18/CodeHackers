# Generated by Django 2.1.1 on 2018-10-26 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('haxtor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AlterField(
            model_name='user',
            name='userCat',
            field=models.CharField(choices=[('1', 'kids'), ('2', 'coder')], max_length=254),
        ),
    ]
