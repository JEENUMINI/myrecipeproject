# Generated by Django 3.1.3 on 2020-12-09 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='created_by',
            field=models.CharField(max_length=150),
        ),
    ]
