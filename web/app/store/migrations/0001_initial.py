# Generated by Django 2.2.3 on 2019-07-16 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species', models.CharField(default='', max_length=128)),
                ('item', models.CharField(default='', max_length=128)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
