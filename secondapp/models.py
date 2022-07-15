from django.db import models

#   secondapp_army_shop
class ArmyShop(models.Model):
  year = models.IntegerField()
  month = models.IntegerField()
  type = models.CharField(max_length=10)
  name = models.CharField(max_length=30)

  class Meta:
    db_table = 'army_shop'
    managed = False

class Course(models.Model):
  name = models.CharField(max_length=30)
  cnt = models.IntegerField()

  # Override
  def __str__(self):
    return '%s - %s (%s)' % (self.id, self.name, self.cnt)