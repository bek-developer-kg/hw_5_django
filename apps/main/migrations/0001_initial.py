# Generated by Django 5.1.4 on 2025-01-04 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('logo', models.ImageField(upload_to='logo/', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Настройка главной стр-ы',
                'verbose_name_plural': 'Настройки главной стр-ы',
            },
        ),
    ]
