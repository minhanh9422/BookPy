# Generated by Django 5.1.4 on 2024-12-18 07:44

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
                ('bid', models.CharField(max_length=10)),
                ('btittle', models.CharField(max_length=20)),
                ('bauthor', models.CharField(max_length=100)),
                ('bgenres', models.CharField(max_length=20)),
                ('bdescription', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
