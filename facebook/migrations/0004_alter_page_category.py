# Generated by Django 3.2.6 on 2021-09-02 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0003_page_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='category',
            field=models.CharField(default='', max_length=120),
        ),
    ]
