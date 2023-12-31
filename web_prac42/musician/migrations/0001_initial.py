# Generated by Django 5.0 on 2023-12-09 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30, verbose_name='First Name')),
                ('lastName', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone Number')),
                ('instrument', models.CharField(choices=[('Guiter', 'Guiter'), ('Violin', 'Violin'), ('Piano', 'Piano')], max_length=30, verbose_name='Instrument Type')),
            ],
        ),
    ]
