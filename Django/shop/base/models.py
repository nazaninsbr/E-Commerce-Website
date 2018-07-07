from django.db import models
from django.contrib.auth.models import AbstractUser

class ProductType(models.Model):
	name = models.CharField(max_length=128)


class Product(models.Model):
	price = models.IntegerField(verbose_name="قیمت", default=0)
	pname = models.CharField(max_length=128)
	type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

	class Meta:
		unique_together = ('pname', 'type')

class Member(AbstractUser):
	pass







"""

product1 = Product.objects.filter(_type__name="لوازم خانگی")
product2 = Product.objects.get(_type__name="لوازم خانگی").product_set.all()
product3 = Product.objects.get(_type__name="لوازم خانگی").product_set.all().aggregate(price__sum=Sum('price'))
product4 = Product.objects.get(_type__name="لوازم خانگی").product_set.all().annotate(price__sum=Sum('price'))
_sum = 0
for product in product4:
	_sum += product.price

"""