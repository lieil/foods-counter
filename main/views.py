from django.shortcuts import render


# Create your views here.
from django.http import HttpRequest, HttpResponse

from .models import Purchase, Product, ProductGroup, Tag, Shop


def index(request):
    return render(request, 'main/index.html')


def purchase_list(request: HttpRequest) -> HttpResponse:
    purchases = (
        Purchase
        .objects
        .order_by("pk")
        .select_related("product")
        .select_related("shop")
        .all()
    )
    return render(
        request=request,
        template_name="main/purchases.html",
        context={"purchases": purchases},
    )


def group_list(request: HttpRequest) -> HttpResponse:
    groups = (
        ProductGroup
        .objects
        .order_by("pk")
        .prefetch_related("tags")
        .all()
    )
    return render(
        request=request,
        template_name="main/groups.html",
        context={"groups": groups},
    )