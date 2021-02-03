from django.db import models
# Create your models here.

# 배송관련된 APP

class ShippingManager(models.Manager):
    # dadamda에서 배송요청을 할때 이 create_shipping함수가 실행되어 객체 생성 배송요청할때, id, status, departure, destination이 결정됨 나머지는 기사가 값 변경
    def create_shipping(self, dam_request_id, departure, destination):
        shinfo = self.create(dam_request_id=dam_request_id, delivery_status="접수완료", departure=departure, destination=destination)
        return shinfo

class Shipping_info(models.Model):
    dam_request_id = models.CharField(max_length=256)
    delivery_status = models.CharField(max_length=256)
    delivery_man = models.CharField(max_length=256, blank=True)
    pickup_man = models.CharField(max_length=256, blank=True)
    memo = models.CharField(max_length=256, blank=True)
    departure = models.CharField(max_length=256)
    destination = models.CharField(max_length=256)

    objects = ShippingManager()


    def __str__(self):
        return str(self.pk) + ". " + self.dam_request_id + " - " + self.delivery_status + " - " + self.departure