from django.db import models

# Create your models here.
class Line(models.Model):
    """ЛЭП"""

    dispatch_name = models.CharField(
        verbose_name="Диспетчерское наименование",
        max_length=100,
        unique = True,
        null = False,
        blank = False
    )
    pf_name = models.CharField(
        verbose_name="Наименование в PowerFactory",
        max_length=100,
        unique = True
    )
    current_capacity = models.FloatField(
        verbose_name="ДДТН, А",
        default=2000 # Я бы на этом подумал
    )
    length = models.FloatField(
        verbose_name="Длина ЛЭП, км"
#       blank=True, не может не быть
#       null=True
    )
#    voltage_transformer_ratio = models.FloatField( Переделал этот момент в своем проекте
#       verbose_name='Коэффициент трансформации ТН',
#        default=5000,
#        blank=True,
#        null=True
#    )
    manual_ct_ratio = models.FloatField(
        verbose_name="Номинальный ток ТТ",
        default = 2000
    )
    manual_vt_ratio = models.FloatField(
        verbose_name="Номинальное напряжение ТН",
        default = 2200
    )
    branch_count = models.IntegerField(
        verbose_name="Количество ответвлений",
        default=0,
        null=True,
        blank=True
    )
    is_offset_applied = models.BooleanField(
        verbose_name="Применение смещения в защищаемую зону",
        default=False
    )
    zero_sequence_voltage = models.FloatField(
        verbose_name="Составляющая напряжения нулевой последовательности",
        default=0,
        null=True,
        blank=True
    )
    offset_coefficient = models.FloatField(
        verbose_name="Коэффициент смещения для ЛЭП",
        default=0,
        null=True,
        blank=True
    )

#    class Meta:
#        """Мета-данные модели Line."""
#
#        db_table = 'line'
#        verbose_name = 'ЛЭП'
#        verbose_name_plural = 'ЛЭП'
#
#    def __str__(self):
#         """
#         :return: Диспетчерское наименование ЛЭП.
#         """
#        return f"{self.dispatch_name} ({self.pf_name})" or self.dispatch_name
#
#    def save(self, *args, **kwargs):
#        """Автоматический расчет количества ответвлений при сохранении"""
#        if not self.branch_count:
#            self.branch_count = self.line_taps.filter(is_active=True).count()
#        super().save(*args, **kwargs)

class Substation(models.Model):
    """Подстанция"""

    dispatch_name = models.CharField(
        verbose_name="Диспетчерское наименование",
        max_length=100,
        unique=True,

    )
    pf_name = models.CharField(
        verbose_name="Наименование в PowerFactory",
        max_length=100,
        null=True,
        blank=True
    )
    voltage_level = models.FloatField(verbose_name="Уровень напряжения, кВ")

#    class Meta:
#        """Мета-данные модели Substation."""
#
#        db_table = 'substation'
#        verbose_name = 'Подстанция'
#        verbose_name_plural = 'Подстанции'
#
#    def __str__(self):
#        """
#        :return: Диспетчерское наименование подстанции.
#        """
#        return self.dispatch_name

class LineTap(models.Model):
    """Ответвления ЛЭП"""

    dispatch_name = models.CharField(
        verbose_name="Диспетчерское наименование ответвления",
        max_length=100,
        null=True, # Надо подумать
        blank=True,
        unique=True
    )
    pf_name = models.CharField(
        verbose_name="Наименование в PowerFactory",
        max_length=100,
        null=True, # Надо подумать
        blank=True
    )
    length = models.FloatField(
        verbose_name="Длина ответвления"
    )
    is_active = models.BooleanField(
        verbose_name="Активно ли ответвление",
        default=True
    )

class LineType(models.Model):
    """Тип ЛЭП"""

    type_code = models.CharField(
        verbose_name="Наименование типа ЛЭП",
        max_length=100,
        unique=True,
    )

#    class Meta:
#        db_table = 'line_type'
#        verbose_name = 'Тип ЛЭП'
#        verbose_name_plural = 'Типы ЛЭП'
#
#    def __str__(self):
#        return self.type_code