# Generated by Django 2.2.5 on 2019-10-09 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acceuilimage',
            name='image',
            field=models.ImageField(upload_to='home'),
        ),
    ]
