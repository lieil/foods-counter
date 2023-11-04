from django.db import models


# Create your models here.
class ProductGroup(models.Model):
    name = models.CharField(max_length=50, default="default")
    description = models.TextField(null=False, blank=True, default="default food group description")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(null=True)
    group = models.ForeignKey(
        ProductGroup,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return self.name