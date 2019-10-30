# Generated by Django 2.1.7 on 2019-10-29 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0009_delete_approve'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='approve_status',
            field=models.CharField(choices=[('Y', 'OK'), ('N', 'NOK'), ('W', 'Waiting')], default='N', max_length=100),
        ),
    ]