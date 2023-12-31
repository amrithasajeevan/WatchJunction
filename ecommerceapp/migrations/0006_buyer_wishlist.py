# Generated by Django 4.2.5 on 2023-09-19 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0005_buyerreg_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='buyer_wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.IntegerField()),
                ('product_name', models.CharField(max_length=30)),
                ('picture', models.FileField(upload_to='')),
                ('price', models.IntegerField()),
                ('category', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=200)),
            ],
        ),
    ]
