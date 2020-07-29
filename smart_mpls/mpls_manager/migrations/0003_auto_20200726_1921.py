# Generated by Django 3.0.6 on 2020-07-26 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpls_manager', '0002_auto_20200726_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='vrf',
            name='routing',
            field=models.CharField(blank=True, choices=[('ospf', 'OSPF'), ('rip', 'RIP version 2'), ('static', 'STATIC ROUTAGE'), ('eigrp', 'EIGRP')], default='static', max_length=30),
        ),
        migrations.AlterField(
            model_name='device',
            name='device_type',
            field=models.CharField(blank=True, choices=[('router', 'Router'), ('firewall', 'Firewall'), ('switch', 'Switch')], default='router', max_length=30),
        ),
    ]
