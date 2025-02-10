# Generated by Django 5.1.5 on 2025-02-10 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_toolbox_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='toolbox',
            name='position_x',
        ),
        migrations.RemoveField(
            model_name='toolbox',
            name='position_y',
        ),
        migrations.AddField(
            model_name='toolbox',
            name='height',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='toolbox',
            name='width',
            field=models.IntegerField(default=50),
        ),
    ]
