# Generated by Django 3.0.6 on 2020-07-24 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpls_monitor', '0005_auto_20200724_1107'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='management',
        ),
        migrations.RemoveField(
            model_name='interface',
            name='device_ref',
        ),
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.CharField(blank=True, choices=[('switch', 'Switch'), ('firewall', 'Firewall'), ('router', 'Router')], default='router', max_length=30),
        ),
    ]
