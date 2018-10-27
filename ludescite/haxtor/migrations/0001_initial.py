# Generated by Django 2.1.1 on 2018-10-26 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('ansID', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('ansText', models.CharField(max_length=254)),
                ('ansCorrect', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('quesID', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('quesLevel', models.CharField(choices=[(1, 'easy'), (2, 'medium'), (3, 'hard')], max_length=1)),
                ('quesText', models.CharField(max_length=256)),
                ('quesImg', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topicID', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=256, unique=True)),
                ('diffLevel', models.CharField(choices=[(1, 'easy'), (2, 'medium'), (3, 'hard')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uID', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('userCat', models.CharField(choices=[(1, 'kids'), (2, 'coder')], max_length=1)),
                ('point', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progScore', models.IntegerField()),
                ('currEvolution', models.CharField(choices=[(1, 'CupCake'), (2, 'Pasterie'), (3, 'FudgeCake')], max_length=50)),
                ('uID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='haxtor.User')),
            ],
        ),
        migrations.AddField(
            model_name='questions',
            name='topicID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='haxtor.Topic'),
        ),
        migrations.AddField(
            model_name='answers',
            name='quesID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='haxtor.Questions'),
        ),
    ]