# Generated by Django 3.2.5 on 2021-09-02 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_alter_user_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=11, unique=True, verbose_name='mobile'),
        ),
    ]