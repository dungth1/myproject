# Generated by Django 2.1.7 on 2019-10-30 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0017_tutorial_approved_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='phuongan',
            field=models.CharField(choices=[('PA1_NECACT', 'Phương án 1:Import to NectAct'), ('PA2_TDM', 'Phương án 2:TDM'), ('PA3_AoIP_IP', 'Phương án 3:AoIP-IP'), ('PA4_AoIP_TDM', 'Phương án 4:AoIP-TDM'), ('PA4_Biendao', 'Phương án 5:Biển đảo')], default='PA2_TDM', max_length=100),
        ),
    ]
