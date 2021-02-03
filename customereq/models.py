from django.db import models
from datetime import datetime
import string
import random
# Create your models here.

def set_request_id():
    str_length = 10
    string_pool = string.ascii_letters
    result = ""
    for index in range(str_length):
        result = result + random.choice(string_pool)
    result = datetime.today().strftime("%Y%m%d%H%M%S") + result
    return result

class Customereq(models.Model):
    sender_name = models.CharField(max_length=64, verbose_name="보내는사람")
    sender_address = models.CharField(max_length=256, verbose_name="보내는사람 주소")
    sender_detailAddress = models.CharField(max_length=64, verbose_name="보내는 사람 상세 주소")
    sender_extraAddress = models.CharField(max_length=64,verbose_name="보내는 사람 주소 참고", blank=True)
    sender_postcode = models.CharField(max_length=64, verbose_name="보내는 사람 우편번호")
    receiver_name = models.CharField(max_length=64, verbose_name="받는 사람")
    receiver_address = models.CharField(max_length=256, verbose_name="받는 사람 주소")
    receiver_detailAddress = models.CharField(max_length=64, verbose_name="받는 사람 상세 주소")
    receiver_extraAddress = models.CharField(max_length=64, verbose_name="받는 사람 주소 참고", blank=True)
    receiver_postcode = models.CharField(max_length=64, verbose_name="받는 사람 우편번호")
    items = models.CharField(max_length=256, verbose_name="보내는 물건 상세")
    pickup_date = models.DateTimeField(auto_now_add=True,verbose_name="기사가 수거해 간 날짜 및 시간")
    request_message = models.CharField(max_length=256, verbose_name="보내는 요청자가 기사에게 요청사항")
    dam_request_id = models.CharField(max_length=64,default=set_request_id(), verbose_name="요청id")


    def __str__(self):
        return '%s %s %s'%(self.dam_request_id, self.sender_name, self.receiver_name)