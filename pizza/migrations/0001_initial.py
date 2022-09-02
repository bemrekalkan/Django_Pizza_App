# Generated by Django 4.1 on 2022-09-02 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('1', 'small'), ('2', 'medium'), ('3', 'large')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping1', models.CharField(max_length=50, verbose_name='Topping_1')),
                ('topping2', models.CharField(max_length=50, verbose_name='Topping_2')),
                ('size', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pizza.size')),
            ],
        ),
    ]