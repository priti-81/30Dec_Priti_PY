# Generated by Django 3.0 on 2023-07-04 08:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Addpolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('policynames', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userType', models.CharField(blank=True, default='U', max_length=20)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, default=None, max_length=254)),
                ('city', models.CharField(default=None, max_length=20)),
                ('mobile', models.BigIntegerField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='policyTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('Name', models.CharField(max_length=30)),
                ('policyTenure', models.SmallIntegerField(default=None)),
                ('totalAmount', models.IntegerField(default=123456)),
                ('premiumAmount', models.BigIntegerField(default=None)),
                ('premiumPay', models.TextField(default=None)),
                ('expectedReturn', models.BigIntegerField(default=None)),
                ('policyName', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Lifesure.Addpolicy')),
            ],
        ),
    ]
