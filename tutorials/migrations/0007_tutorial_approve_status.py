# Generated by Django 2.1.7 on 2019-10-29 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0006_approve'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='approve_status',
            field=models.CharField(default='Waiting', max_length=100),
        ),
    ]
