# Generated by Django 3.2.5 on 2021-07-10 17:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Polls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll_title', models.CharField(max_length=50)),
                ('option1', models.IntegerField(default=0)),
                ('option2', models.IntegerField(default=0)),
                ('option3', models.IntegerField(default=0)),
                ('option4', models.IntegerField(default=0)),
                ('option5', models.IntegerField(default=0)),
                ('is_valid', models.DurationField(default=datetime.timedelta(days=7))),
            ],
        ),
    ]
