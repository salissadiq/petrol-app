# Generated by Django 4.1 on 2022-08-05 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_product_category_alter_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales',
            name='status',
        ),
        migrations.AddField(
            model_name='sales',
            name='amount',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
