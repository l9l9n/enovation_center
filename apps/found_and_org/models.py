from django.db import models


class SupportingOrganization(models.Model):
    name = models.CharField(max_length=255, verbose_name="(Фонд) Название организации поддержки")
    support_type = models.CharField(max_length=100, verbose_name="Тип поддержки", null=True, blank=True)
    support_conditions = models.TextField(verbose_name="Условия поддержки", null=True, blank=True)
    additional_files = models.FileField(upload_to='media/support_files/',
                                        verbose_name="Дополнительные файлы",
                                        blank=True,
                                        null=True,
                                        )
    contacts = models.CharField(max_length=150, verbose_name="Контакты", null=True, blank=True)
    register_date = models.DateField(verbose_name="Дата регистрации", auto_now_add=True)

    class Meta:
        verbose_name = "Фонд | Организация"
        verbose_name_plural = "Фонды | Организации"

    def __str__(self):
        return f"{self.name}"
