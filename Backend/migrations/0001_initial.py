# Generated by Django 5.0.4 on 2024-05-05 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PedalRushersDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_PD', models.CharField(blank=True, max_length=100, null=True)),
                ('Description_PD', models.CharField(blank=True, max_length=200, null=True)),
                ('Image_PD', models.ImageField(blank=True, null=True, upload_to='PedalRushers_Images')),
            ],
        ),
    ]
