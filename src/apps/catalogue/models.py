from django.db import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse


class ProductManager(models.Manager):
    def published(self):
        good_list = Product.objects.filter(status='p')

        return good_list

    def added(self):
        good_list = Product.objects.filter(status='d')

        return good_list

    def withdrawn(self):
        good_list = Product.objects.filter(status='w')

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
    name = models.CharField(verbose_name=u"Опция",
                            max_length=255)
    description = models.TextField(verbose_name=u'Описание',
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
    ADDED, PUBLISHED, WITHDRAWN = 'added', 'published', 'withdrawn'
    STATUS_CHOICES = ((ADDED, u'Добавлен'),
                      (PUBLISHED, u'Опубликован'),
                      (WITHDRAWN, u'Изъят'),
                      )
    name = models.CharField(u'Название товара',
                            max_length=255)
    description = models.TextField(verbose_name=u"Описание товара",
                                   blank=True,
                                   null=True)
    attribute = models.ManyToManyField(OptionAttribute,
                                       verbose_name=u'Параметры',
                                       blank=True)
    option = models.ManyToManyField(Option,
                                    verbose_name=u'Опция',
                                    blank=True)
    price = models.IntegerField(verbose_name=u'Цена',
                                default=0)

    preview = models.ImageField(verbose_name=u'Фотография',
                                upload_to='product')

    raiting = models.IntegerField(verbose_name=u'Рейтинг',
                                  default=0,
                                  )

    status = models.CharField(verbose_name=u"Статус",
                              max_length=9,
                              choices=STATUS_CHOICES,
                              default=ADDED,
                              )

    date_created = models.DateTimeField(verbose_name=u"Создан",
                                        auto_now_add=True,
                                        null=True
                                        )
    date_updated = models.DateTimeField(verbose_name=u"Обновлен",
                                        auto_now=True,
                                        null=True
                                        )

    objects = ProductManager()

    def __str__(self):
        return self.name

    def get_url(self):
        return reverse('details',
                       kwargs={'id': str(self.id)})

    class Meta:
        ordering = ["name"]
        verbose_name = u'Товар'
        verbose_name_plural = u'Товары'


class Category(models.Model):
    STANDALONE, PARENT, CHILD = 'standalone', 'parent', 'child'
    STRUCTURE_CHOICES = ((STANDALONE, u'Независимая'),
                         (PARENT, u'Родительская'),
                         (CHILD, u'Подкатегория'),
                         )
    structure = models.CharField(verbose_name=u'Тип категории',
                                 max_length=10,
                                 choices=STRUCTURE_CHOICES,
                                 default=PARENT,
                                 )
    parent = models.ForeignKey('self',
                               verbose_name=u'Родительская категория',
                               blank=True,
                               related_name='children',
                               null=True
                               )
    name = models.CharField(u'Название категории',
                            max_length=255
                            )
    slug = models.SlugField(verbose_name=u'Метка',
                            max_length=255,
                            unique=True,
                            null=True)
    description = models.TextField(verbose_name=u'Описание',
                                   blank=True)
    product = models.ManyToManyField(Product,
                                     verbose_name=u'Товар',
                                     blank=True)
    option = models.ManyToManyField(Option,
                                    verbose_name=u'Характеристика',
                                    blank=True)

    class Meta:
        verbose_name = u'Категория'
        verbose_name_plural = u'Категории'

