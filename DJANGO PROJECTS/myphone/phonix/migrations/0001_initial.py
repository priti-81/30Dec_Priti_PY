# Generated by Django 3.0 on 2023-06-07 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='productdetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productprice', models.FloatField()),
                ('productimage', models.ImageField(blank=True, upload_to='media')),
                ('productmodel', models.CharField(max_length=30)),
                ('productRAM', models.CharField(max_length=20)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='phonix.product')),
            ],
        ),
    ]