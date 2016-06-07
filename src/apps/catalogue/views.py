from django.template import RequestContext
from datetime import datetime
from django.template import loader
from .models import Product, Category, Option
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.core.paginator import Paginator

from django.http import HttpResponse, Http404, HttpRequest
from django.views.decorators.http import require_GET
from django.shortcuts import render, get_object_or_404


@require_GET
def goods_for_sale(request):
    good_list = Product.objects.sale()
    page = request.GET.get('page',
                           1)

    goods = Product.objects.pagination(good_list,
                                       page)

    context = {
        'page': goods,
        'goods': goods.object_list,
    }

    return render(request,
                  'catalogue/sales.html',
                  context
                  )


def ProductView(request):
    products = ProductItem.objects.filter(product_type__name="Группа №1").filter(status="p").distinct()
    template = loader.get_template('catalogue/catalogue.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))


def product_group(request):
    products = ProductItem.objects.filter(product_type__name="Группа №1").filter(status="p").distinct()
    print('Тест', products)
    template = loader.get_template('catalogue/catalogue.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))

def index(request):
    products = ProductItem.objects.filter(product_type__name="Группа №1").filter(status="p").distinct()
    print('Тест', products)
    template = loader.get_template('catalogue/product.html')
    context = {
        'products': products,
    }
    return HttpResponse(template.render(context, request))


def Product1View(request):
    list = ProductItem.objects.filter(product_type__name="test1").filter(status="p").distinct()
    template = loader.get_template('catalogue/list1.html')
    context = {
        'list': list,
    }
    return HttpResponse(template.render(context, request))


def Product2View(request):
    type = ProductType.objects.filter(name="krovati")
    #list = ProductItem.objects.filter(product_type=type)
    template = loader.get_template('catalogue/list2.html')
    context = {
        'list': list,
    }
    return HttpResponse(template.render(context, request))


def AkciiView(request):
    list = ProductItem.objects.all()
    paginator = Paginator(list, 2, 2)

    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    template = loader.get_template('catalogue/akcii.html')
    #print(products.page_range_data)

    context = {
        'products': list,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'catalogue/sales.html',
        context_instance = RequestContext(request,
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        })
    )


def product_detail(request, product_id):
    product = ProductItem.objects.get(id=product_id)
    product_options = OptionGroup.objects.filter(producttype__id=(ProductType.objects.filter(type__in=product_id)))
    template = loader.get_template('catalogue/detail_old.html')
    context = {
        'product': product,
        'product_options': product_options,
    }
    return HttpResponse(template.render(context, request))