from django.db import models


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
