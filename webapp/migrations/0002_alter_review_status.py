# Generated by Django 4.2.4 on 2023-08-09 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='status',
            field=models.CharField(choices=[('Принят', 'Принят'), ('Отклонен', 'Отклонен'), ('На модерации', 'На модерации')], default='На модерации', max_length=50, null=True, verbose_name='Статус'),
        ),
    ]
