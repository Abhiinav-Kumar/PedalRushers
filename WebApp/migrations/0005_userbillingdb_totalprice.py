# Generated by Django 5.0.4 on 2024-06-10 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0004_userbillingdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbillingdb',
            name='Totalprice',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
