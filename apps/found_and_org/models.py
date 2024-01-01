from django.db import models


class SupportingOrganization(models.Model):
    name = models.CharField(max_length=255, verbose_name="(Фонд) Название организации поддержки")
    support_type = models.CharField(max_length=100, verbose_name="Тип поддержки")
    support_conditions = models.TextField(verbose_name="Условия поддержки")
    additional_files = models.FileField(upload_to='media/support_files/',
                                        verbose_name="Дополнительные файлы",
                                        blank=True,
                                        null=True,
                                        )

    class Meta:
        verbose_name = "Фонд | Организация"
        verbose_name_plural = "Фонды | Организации"

    def __str__(self):
        return f"{self.name}"
