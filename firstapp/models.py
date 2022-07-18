from django.db import models

class Curriculum(models.Model):
  name = models.CharField(max_length=255)
  # cnt = models.IntegerField(null=True)

class Owner(models.Model):
  name = models.CharField(max_length=50, null=True)
  class Meta:
    db_table = 'owner'

class Animal(models.Model):
  name = models.CharField(max_length=50, null=True)
  age = models.IntegerField(null=True)
  owner = models.ForeignKey(Owner, on_delete=models.SET_NULL, null=True)
  class Meta:
    db_table = 'animal'

class Warranty(models.Model):
  model_nm = models.CharField(max_length=50, null=True)
  period = models.IntegerField(null=True)
  class Meta:
    db_table = 'warranty'

class Product(models.Model):
  name = models.CharField(max_length=50, null=True)
  price = models.IntegerField(null=True)
  animal = models.ForeignKey(Animal, on_delete=models.SET_NULL, null=True)
  warranty = models.OneToOneField(Warranty, on_delete=models.SET_NULL, null=True)

  class Meta:
    db_table = 'product'

class Playground(models.Model):
  name = models.CharField(max_length=50, null=True)
  address = models.CharField(max_length=50, null=True)
  tel = models.CharField(max_length=20, null=True)
  animals = models.ManyToManyField(Animal, null=True)
  
  class Meta:
    db_table = 'playground'