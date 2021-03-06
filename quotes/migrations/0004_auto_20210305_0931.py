# Generated by Django 3.1.7 on 2021-03-05 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_auto_20210305_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highprice',
            name='highprice',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='lowprice',
            name='lowprice',
            field=models.DecimalField(decimal_places=5, default=0.0, max_digits=10),
        ),
    ]