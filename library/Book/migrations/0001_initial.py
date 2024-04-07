# Generated by Django 5.0.4 on 2024-04-05 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, null=True)),
                ('category', models.CharField(choices=[('math', 'Math'), ('science', 'Science'), ('physics', 'Physics'), ('arab', 'Arabic'), ('islamic', 'Islamic'), ('frensh', 'Frensh'), ('geography', 'Geography'), ('hestory', 'Hestory')], max_length=100)),
                ('class_number', models.CharField(blank=True, max_length=100)),
                ('entry_date', models.DateField(auto_now=True)),
                ('published_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('adress', models.CharField(blank=True, default='', max_length=200)),
                ('phone_number', models.CharField(blank=True, default=0, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('adress', models.CharField(default='', max_length=200)),
                ('class_name', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='RentBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent_date', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField()),
                ('prof_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Book.prof')),
                ('student_name', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Book.student')),
            ],
        ),
    ]
