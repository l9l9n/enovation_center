from django.db import models


class Startup(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название проекта")
    description = models.TextField(verbose_name="Описание проекта", null=True, blank=True)
    industry = models.CharField(max_length=100, verbose_name="Отрасль", null=True, blank=True)
    prototype_status = models.CharField(max_length=90, verbose_name="Статус прототипа",
                                        choices=[('Yes', 'Есть'), ('No', 'Нет')],
                                        default='No',
                                        null=True,
                                        blank=True)
    allowed_status = models.CharField(max_length=90, verbose_name="Статус",
                                      choices=[('Yes', 'Принят'), ('No', 'Отказано')],
                                      default='No',
                                      null=True,
                                      blank=True)
    development_stage = models.CharField(max_length=50, verbose_name="Этап развития", null=True, blank=True)
    additional_files = models.FileField(upload_to='media/startup_files/',
                                        verbose_name="Дополнительные файлы",
                                        blank=True,
                                        null=True,)
    register_date = models.DateField(verbose_name="Дата регистрации", auto_now_add=True)


    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return f"{self.name}"
