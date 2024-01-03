from django.db import models


class Investor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя инвестора")
    investment_area = models.CharField(max_length=100, verbose_name="Область инвестирования", null=True, blank=True)
    investment_size = models.DecimalField(max_digits=100, decimal_places=2, verbose_name="Размер инвестиций", null=True, blank=True)
    additional_files = models.FileField(upload_to='media/investor_files/',
                                        verbose_name="Дополнительные файлы",
                                        blank=True,
                                        null=True,
                                        )
    contacts = models.CharField(max_length=150, verbose_name="Контакты", null=True, blank=True)
    register_date = models.DateField(verbose_name="Дата регистрации", auto_now_add=True)

    class Meta:
        verbose_name = "Инвестор"
        verbose_name_plural = "Инвесторы"

    def __str__(self):
        return f"{self.name}"
