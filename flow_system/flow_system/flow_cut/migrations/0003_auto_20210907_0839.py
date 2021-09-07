# Generated by Django 2.1.8 on 2021-09-07 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow_cut', '0002_auto_20210831_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pcaps_cut',
            name='label',
        ),
        migrations.RemoveField(
            model_name='pcaps_cut',
            name='nth',
        ),
        migrations.AddField(
            model_name='pcaps_cut',
            name='original',
            field=models.CharField(default='wrong', max_length=100),
        ),
        migrations.AlterField(
            model_name='pcaps_cut',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
