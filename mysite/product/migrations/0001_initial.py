# Generated by Django 3.2.1 on 2021-05-05 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12)),
                ('description', models.CharField(max_length=255)),
                ('quantity', models.IntegerField(default=0)),
            ],
        ),
    ]
