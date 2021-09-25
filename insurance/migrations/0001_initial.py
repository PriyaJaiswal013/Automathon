# Generated by Django 3.0.5 on 2021-09-20 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20)),
                ('creation_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_name', models.CharField(max_length=200)),
                ('sum_assurance', models.PositiveIntegerField(default=500000)),
                ('Pateint_name', models.CharField(max_length=500)),
                ('contact_no', models.IntegerField(default='')),
                ('gender', models.CharField(max_length=200)),
                ('insured_card_id_number', models.CharField(max_length=500)),
                ('total_cost_hospitalization', models.PositiveIntegerField()),
                ('creation_date', models.DateField(auto_now=True)),
                ('status', models.CharField(default='Pending', max_length=100)),
                ('category', models.ForeignKey(default='Health Insurance', on_delete=django.db.models.deletion.CASCADE, to='insurance.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('admin_comment', models.CharField(default='Nothing', max_length=200)),
                ('asked_date', models.DateField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='PolicyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Pending', max_length=100)),
                ('creation_date', models.DateField(auto_now=True)),
                ('Policy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance.Policy')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer')),
            ],
        ),
    ]