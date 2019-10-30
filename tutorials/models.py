from django.db import models
from datetime import datetime


DEPT_CHOICES = [
    ('DHML_DEPT', 'PHÒNG ĐIỀU HÀNH MẠNG LƯỚI'),
    ('TKTU_DEPT', 'PHÒNG THIẾT KẾ TỐI ƯU'),
    ('DD_DEPT', 'PHÒNG DI ĐỘNG'),
]
KIND_CHOICES = [
    ('CDD', 'CDD'),
    ('PCM', 'PCM'),
    ('OTHER', 'Khác'),

]

APROVED_CHOICES = [
    ('Pass', 'Pass'),
    ('Deny', 'Deny'),
    ('Waiting','Waiting'),

]
PA_CHOICES = [
    ('All','Dùng chung cho tất cả phương án'),
    ('PA1_NECACT','Phương án 1:Import to NectAct'),
    ('PA2_TDM','Phương án 2:TDM'),
    ('PA3_AoIP_IP','Phương án 3:AoIP-IP'),
    ('PA4_AoIP_TDM','Phương án 4:AoIP-TDM'),
    ('PA4_Biendao','Phương án 5:Biển đảo'),
]
def linkto(instance,filename):
    _datetime = datetime.now()
    datetime_str = _datetime.strftime("%Y/%m")
    return '{0}/{1}/{2}/{3}/{4}'.format(datetime_str,instance.dept,instance.category,instance.phuongan,filename)

class Tutorial(models.Model):
    dept = models.CharField(max_length=100,default='TKTU_DEPT', choices = DEPT_CHOICES)
    category = models.CharField(max_length=100,default='CDD', choices=KIND_CHOICES)
    phuongan = models.CharField(max_length=100, default='All',choices=PA_CHOICES)
    #feature_image = models.ImageField(upload_to='tutorial/images/')
    #attachment = models.FileField(upload_to='tutorial/attachments/')
    attachment = models.FileField(upload_to=linkto)
    upload_user = models.CharField(max_length=100)
    approve_status = models.CharField(max_length=100,default='Waiting',choices=APROVED_CHOICES)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    approved_user = models.CharField(max_length=100,default='viewer')



    def __str__(self):
        return self.dept

    def delete(self, *args, **kwargs):
       # self.feature_image.delete()
        self.attachment.delete()
        super().delete(*args, **kwargs)







