# Generated by Django 4.2.3 on 2024-01-08 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appadmin', '0003_alter_detail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='filepath/'),
        ),
    ]
