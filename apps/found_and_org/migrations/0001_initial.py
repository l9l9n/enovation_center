# Generated by Django 4.2 on 2024-01-01 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SupportingOrganization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='(Фонд) Название организации поддержки')),
                ('support_type', models.CharField(max_length=100, verbose_name='Тип поддержки')),
                ('support_conditions', models.TextField(verbose_name='Условия поддержки')),
                ('additional_files', models.FileField(blank=True, null=True, upload_to='media/support_files/', verbose_name='Дополнительные файлы')),
            ],
            options={
                'verbose_name': 'Фонд | Организация',
                'verbose_name_plural': 'Фонды | Организации',
            },
        ),
    ]
