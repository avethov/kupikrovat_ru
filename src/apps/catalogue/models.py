from django.db import models
from django.core.paginator import Page, Paginator, EmptyPage, PageNotAnInteger
from os.path import join


class ProductManager(models.Manager):
    def sale(self):
        good_list = Product.objects.filter(is_saled=True)

        return good_list

    def pagination(self,
                   list,
                   page,
                   limit=16):

        paginator = Paginator(list,
                              limit)

        try:
            goods = paginator.page(page)
        except PageNotAnInteger:
            goods = paginator.page(1)
        except EmptyPage:
            goods = paginator.page(paginator.num_pages)

        return goods


class Option(models.Model):
    name = models.CharField(u"Опция",
                            max_length=255)
    description = models.TextField(u'Описание',
                                   blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = u'Опция'
        verbose_name_plural = u'Опции'


class OptionAttribute(models.Model):
    name = models.CharField(u"Параметр",
                            max_length=255)
    option = models.ForeignKey(Option,
                               on_delete=models.CASCADE,
                               related_name="options",
                               related_query_name="option"
                               )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = u'Аттрибут'
        verbose_name_plural = u'Аттрибуты'


class Product(models.Model):
    name = models.CharField(u'Название товара',
                            max_length=255)
    description = models.TextField(u"Описание товара",
                                   blank=True)
    attribute = models.ManyToManyField(OptionAttribute,
                                       verbose_name=u'Параметры',
                                       blank=True)
    option = models.ManyToManyField(Option,
                                    verbose_name=u'Опция',
                                    blank=True)
    price = models.IntegerField(u'Цена',
                                default=0)

    preview = models.OneToOneField(ProductImagePreview,
                                   on_delete=models.CASCADE)

    is_saled = models.BooleanField(default=False)

    date_created = models.DateTimeField(
        u"Создан",
        auto_now_add=True,
        null=True
        )
    date_updated = models.DateTimeField(
        u"Обновлен",
        auto_now=True,
        null=True
        )

    objects = ProductManager()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'


def content_file_name(instance,
                      filename):
    return join(['product', instance.Product.name, filename])


class Category(models.Model):
    name = models.CharField(u'Название категории',
                            max_length=255
                            )
    product = models.ManyToManyField(Product,
                                     verbose_name=u'Товар',
                                     blank=True)
    option = models.ManyToManyField(Option,
                                    verbose_name=u'Характеристика',
                                    blank=True)

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'


class ProductImagePreview(models.Model):
    preview = models.ImageField(upload_to=content_file_name)

    class Meta:
        verbose_name = "Preview image"


class ProductImageExtra(models.Model):
    image = models.ImageField(upload_to='product')

    class Meta:
        verbose_name = "Extra image"
        verbose_name_plural = "Extra images"



'''
class ProductType(models.Model):
    name = models.CharField("Name", max_length=256)
    options = models.ManyToManyField('catalogue.OptionGroup', blank=True, verbose_name="Options", default="")

    class Meta:
        app_label = "catalogue"
        ordering = ["name"]
        verbose_name = "Product type"
        verbose_name_plural = "Product types"

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField("Name", max_length=256)

    class Meta:
        app_label = "catalogue"
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

STATUS_CHOICES = (
    ('d', u'Добавлен'),
    ('p', u'Опубликован'),
    ('w', u'Изъят'),
)


class ProductItem(models.Model):
    name = models.CharField(u"Название", max_length=256)
    description = models.TextField(u"Описание", blank=True)
    price = models.DecimalField(u"Цена", max_digits=6, decimal_places=0)
    product_type = models.ForeignKey(
        'catalogue.ProductType',
        on_delete=models.CASCADE,
        related_name="types",
        related_query_name="type",
        verbose_name=u"Тип",
        null=True,
        blank=True
        )
    product_options = models.ManyToManyField(
        'catalogue.OptionGroup',
        verbose_name=u"Доступные опции"
        )
    product_image = models.ImageField(
        upload_to='product'
        )
    rating = models.FloatField(u"Рейтинг", default=0)
    date_created = models.DateTimeField(
        u"Создан",
        auto_now_add=True,
        null=True
        )
    date_updated = models.DateTimeField(
        u"Обновлен",
        auto_now=True,
        null=True
        )
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
        default="d",
        verbose_name=u"Текущий статус"
        )

    class Meta:
        app_label = "catalogue"
        ordering = ["name"]
        verbose_name = u"Товар"
        verbose_name_plural = u"Товары"


class ProductRecommendation(models.Model):
    pass


class ProductSpecial(models.Model):
    pass


class OptionGroup(models.Model):
    name = models.CharField("Name", max_length=256)
    description = models.TextField("Description", blank=True)

    class Meta:
        app_label = "catalogue"
        ordering = ["name"]
        verbose_name = "Option group"
        verbose_name_plural = "Option groups"

    def __str__(self):
        return self.name


class OptionItem(models.Model):
    option_group = models.ForeignKey(
        'catalogue.OptionGroup',
        on_delete=models.CASCADE,
        related_name="groups",
        related_query_name="group",
        null=True,
        blank=True
        )
    name = models.CharField(u"Параметр", max_length=256)

    class Meta:
        app_label = "catalogue"
        ordering = ["name"]
        verbose_name = "Option"
        verbose_name_plural = "Options"
'''