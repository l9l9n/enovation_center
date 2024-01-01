from django.db import models


class Investor(models.Model):
    name = models.CharField(max_length=255, verbose_name="Имя инвестора")
    investment_area = models.CharField(max_length=100, verbose_name="Область инвестирования")
    investment_size = models.DecimalField(max_digits=100, decimal_places=2, verbose_name="Размер инвестиций")
    additional_files = models.FileField(upload_to='media/investor_files/',
                                        verbose_name="Дополнительные файлы",
                                        blank=True,
                                        null=True,
                                        )

    class Meta:
        verbose_name = "Инвестор"
        verbose_name_plural = "Инвесторы"

    def __str__(self):
        return f"{self.name}"
