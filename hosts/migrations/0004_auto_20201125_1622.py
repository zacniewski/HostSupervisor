# Generated by Django 3.1.3 on 2020-11-25 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hosts', '0003_auto_20201125_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vlan',
            name='uwagi',
            field=models.TextField(blank=True, default='Brak'),
        ),
    ]
