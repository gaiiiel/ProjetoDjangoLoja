# Generated by Django 4.2.7 on 2024-07-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_categoria_produto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='msgPromocao',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]