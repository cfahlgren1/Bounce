# Generated by Django 2.0 on 2020-05-17 05:03

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0010_auto_20200517_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='id',
            field=models.IntegerField(default=django.utils.timezone.now, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='court',
            name='id',
            field=models.CharField(default=uuid.UUID('8883f5f1-fc87-473a-92a8-74a35f01436d'), max_length=50, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
