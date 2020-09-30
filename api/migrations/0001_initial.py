# Generated by Django 3.1 on 2020-09-24 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_date', models.DateTimeField()),
                ('security', models.CharField(max_length=200)),
                ('currency', models.CharField(max_length=200)),
                ('carry_val', models.IntegerField()),
                ('safekeeping', models.CharField(max_length=200)),
                ('encumberance', models.CharField(choices=[('p', 'Pledged'), ('o', 'Onloan'), ('r', 'Restricted')], max_length=200)),
            ],
        ),
    ]