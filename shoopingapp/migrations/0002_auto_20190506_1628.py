# Generated by Django 2.1.7 on 2019-05-06 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoopingapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='cover',
            field=models.FileField(default=1, upload_to=''),
        ),
    ]
