# Generated by Django 2.1.8 on 2021-09-07 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature_extract', '0010_auto_20210907_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tls_feature',
            name='name',
            field=models.CharField(default='null', max_length=100),
        ),
    ]
