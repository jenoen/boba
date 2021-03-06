# Generated by Django 2.2 on 2019-05-22 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(choices=[('BOBA', 'boba'), ('JELLY', 'jelly'), ('LYCHEE', 'lychee'), ('REDBEAN', 'redbean'), ('AGAR', 'agar')], max_length=100)),
                ('ice', models.BooleanField(null=True)),
                ('drinkBase', models.CharField(choices=[('GREEN', 'green'), ('BLACK', 'black'), ('MILK', 'milk'), ('TARO', 'taro'), ('THAI', 'thai')], max_length=100)),
                ('sugarLevel', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customerName', models.CharField(max_length=64)),
                ('totalPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('time', models.DateTimeField()),
                ('drinks', models.ManyToManyField(to='bobaDrinks.Drink')),
            ],
        ),
    ]
