# Generated by Django 5.1.4 on 2025-03-26 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0002_alter_marca_table_alter_pedido_table_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='img'),
        ),
    ]
