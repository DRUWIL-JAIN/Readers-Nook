# Generated by Django 2.0 on 2021-10-07 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readersnook', '0006_auto_20211007_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_book',
            name='bimage',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]
