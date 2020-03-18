# Generated by Django 2.2.10 on 2020-03-02 12:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comercio', '0002_auto_20200226_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carrito',
            old_name='precioUnidad',
            new_name='subTotal',
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(upload_to='static/imgPro'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=models.CharField(max_length=1, null=True),
        ),
    ]
