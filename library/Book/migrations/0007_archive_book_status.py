# Generated by Django 5.0.4 on 2024-04-17 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0006_book_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=200)),
                ('last_name', models.CharField(default='', max_length=200)),
                ('birth_date', models.DateField(default='')),
                ('birth_place', models.CharField(default='', max_length=50)),
                ('class_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('rented', 'Rented'), ('available', 'Available'), ('lost', 'Lost')], default='', max_length=200),
        ),
    ]