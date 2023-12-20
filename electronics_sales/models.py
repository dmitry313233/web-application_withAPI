from django.db import models
# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Factory(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    email = models.EmailField(**NULLABLE, verbose_name='Email')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=70, **NULLABLE, verbose_name='Улица')
    number_home = models.IntegerField(**NULLABLE, verbose_name='Номер дома')
    title_product = models.CharField(max_length=70, verbose_name='Название продукта')
    model_product = models.CharField(**NULLABLE, max_length=30, verbose_name='Модель продукта')
    product_launch_date = models.DateField(auto_now=True, verbose_name='Дата выхода продукта на рынок')
    debt = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Задолженность')  # раздуплить что это
    time_create = models.DateTimeField(auto_now=True, verbose_name='Время создания')

    #provider = models.ForeignKey('Factory', on_delete=models.CASCADE, verbose_name='Поставщик')  # раздуплить что это

    def __str__(self):
        return (f'{self.name}, {self.country}, {self.city}, {self.title_product}, {self.product_launch_date}, '
                f'{self.debt}, {self.time_create}')

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'


class RetailNetwork(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    email = models.EmailField(**NULLABLE, verbose_name='Email')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, **NULLABLE, verbose_name='Город')
    street = models.CharField(max_length=70, **NULLABLE, verbose_name='Улица')
    number_home = models.IntegerField(**NULLABLE, verbose_name='Номер дома')
    title_product = models.CharField(max_length=70, verbose_name='Название продукта')
    model_product = models.CharField(max_length=30, **NULLABLE, verbose_name='Модель продукта')
    product_launch_date = models.DateField(auto_now=True, verbose_name='Дата выхода продукта на рынок')
    debt = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Задолженность')  # раздуплить что это   +
    time_create = models.DateTimeField(auto_now=True, verbose_name='Время создания')

    provider = models.ForeignKey('Factory', on_delete=models.CASCADE, verbose_name='Поставщик')  # раздуплить что это

    def __str__(self):
        return (f'{self.name}, {self.country}, {self.number_home}, {self.title_product}, {self.product_launch_date}, '
                f'{self.debt}, {self.time_create}, {self.provider}')

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Рознечные сети'


class IndividualEntrepreneur(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    email = models.EmailField(verbose_name='Email')
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=70, verbose_name='Улица')
    number_home = models.IntegerField(**NULLABLE, verbose_name='Номер дома')
    title_product = models.CharField(max_length=70, verbose_name='Название продукта')
    model_product = models.CharField(max_length=30, **NULLABLE, verbose_name='Модель продукта')
    product_launch_date = models.DateField(auto_now=True, verbose_name='Дата выхода продукта на рынок')
    debt = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Задолженность')  # раздуплить что это   +
    time_create = models.DateTimeField(auto_now=True, verbose_name='Время создания')

    provider = models.ForeignKey('RetailNetwork', on_delete=models.CASCADE, verbose_name='Поставщик')  # раздуплить что это

    def __str__(self):
        return (f'{self.name}, {self.email}, {self.country}, {self.city}, {self.street}, {self.title_product},'
                f' {self.product_launch_date}, {self.debt}, {self.time_create}, {self.provider}')

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'

