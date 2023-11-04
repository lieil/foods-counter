from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, default="default")
    description = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return self.name


class ProductGroup(models.Model):
    name = models.CharField(max_length=50, default="default")
    description = models.TextField(null=False, blank=True, default="default food group description")
    created_by = models.ForeignKey(User, models.CASCADE)
    # tags

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    group = models.ForeignKey(
        ProductGroup,
        on_delete=models.PROTECT,
    )

    class Unit(models.TextChoices):
        PIECE = "PC", _("Штука")
        KILOGRAM = "KG", _("Килограмм")
        LITER = "L", _("Литр")

    unit = models.CharField(
        max_length=2,
        choices=Unit.choices,
        default=Unit.PIECE,
    )

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=50, default="default")
    description = models.TextField(null=False, blank=True, default="default shop description")
    created_by = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    date = models.DateField()
    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
    )
    quantity = models.FloatField(default=1)
    #
    total = models.FloatField(default=0)
    shop = models.ForeignKey(
        Shop,
        on_delete=models.PROTECT,
    )
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return f"{self.date}, {self.shop}, {self.product}, {self.user.username}"
