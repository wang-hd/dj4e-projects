# Generated by Django 3.2.5 on 2022-02-25 17:57

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Type must be greater than 1 character')])),
            ],
        ),
        migrations.CreateModel(
            name='Boat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, validators=[django.core.validators.MinLengthValidator(2, 'Nickname must be greater than 1 character')])),
                ('length', models.PositiveIntegerField()),
                ('knots', models.PositiveIntegerField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boats.type')),
            ],
        ),
    ]
