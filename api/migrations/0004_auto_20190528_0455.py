# Generated by Django 2.2.1 on 2019-05-27 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20190528_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamesession',
            name='gameData',
        ),
        migrations.AddField(
            model_name='gamesession',
            name='location',
            field=models.CharField(default='stadium', max_length=200),
        ),
    ]