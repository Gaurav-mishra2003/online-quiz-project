# Generated by Django 4.2.2 on 2024-04-10 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addquiz_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ques', models.CharField(max_length=200)),
                ('A', models.CharField(max_length=200)),
                ('B', models.CharField(max_length=200)),
                ('C', models.CharField(max_length=200)),
                ('D', models.CharField(max_length=200)),
                ('Ans', models.CharField(max_length=200)),
            ],
        ),
    ]
