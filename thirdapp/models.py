from django.db import models
from django.db.models.fields import CharField, IntegerField

class Shop(models.Model):
  shop_id = IntegerField(primary_key=True)
  shop_name = CharField(max_length=100, null=True)
  shop_desc = CharField(max_length=100, null=True)
  rest_date = CharField(max_length=100, null=True)
  parking_info = CharField(max_length=100, null=True)
  img_path = CharField(max_length=255, null=True)
  
  class Meta:
    db_table = 'shop'
    app_label = 'thirdapp'
    managed = False
