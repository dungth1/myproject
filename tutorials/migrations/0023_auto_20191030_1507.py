# Generated by Django 2.1.7 on 2019-10-30 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0022_auto_20191030_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='approve_status',
            field=models.CharField(choices=[('Pass', 'Pass'), ('Deny', 'Deny'), ('Waiting', 'Waiting')], default='Waiting', max_length=100),
        ),
    ]
