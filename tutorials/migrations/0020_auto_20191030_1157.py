# Generated by Django 2.1.7 on 2019-10-30 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0019_auto_20191030_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='approved_user',
            field=models.CharField(default='viewer', max_length=100),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='category',
            field=models.CharField(choices=[('CDD', 'CDD'), ('PCM', 'PCM'), ('OTHER', 'Khác')], default='CDD', max_length=100),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='dept',
            field=models.CharField(choices=[('DHML_DEPT', 'PHÒNG ĐIỀU HÀNH MẠNG LƯỚI'), ('TKTU_DEPT', 'PHÒNG THIẾT KẾ TỐI ƯU'), ('DD_DEPT', 'PHÒNG DI ĐỘNG')], default='DHML_DEPT', max_length=100),
        ),
    ]
