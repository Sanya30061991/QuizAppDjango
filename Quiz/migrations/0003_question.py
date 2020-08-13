# Generated by Django 3.0.8 on 2020-08-13 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_auto_20200812_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_id', models.IntegerField(verbose_name='ID of related quiz')),
                ('title', models.TextField(verbose_name='Title of exact question')),
                ('ans1', models.CharField(max_length=100, verbose_name='1 possible answer')),
                ('ans2', models.CharField(max_length=100, verbose_name='2 possible answer')),
                ('ans3', models.CharField(max_length=100, verbose_name='3 possible answer')),
                ('correct_ans', models.CharField(max_length=100, verbose_name='Correct answer to this question')),
            ],
        ),
    ]