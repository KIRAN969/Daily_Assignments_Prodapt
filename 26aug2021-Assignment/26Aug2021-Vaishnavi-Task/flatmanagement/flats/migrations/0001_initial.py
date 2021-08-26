# Generated by Django 3.0.3 on 2021-08-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flatsapp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buildingno', models.IntegerField()),
                ('ownername', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('adhar', models.BigIntegerField()),
                ('mobile', models.BigIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]