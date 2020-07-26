# Generated by Django 3.0.6 on 2020-07-25 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mpls_monitor', '0009_auto_20200724_1833'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='management',
        ),
        migrations.RemoveField(
            model_name='device',
            name='topology_ref',
        ),
        migrations.DeleteModel(
            name='Interface',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='artists',
        ),
        migrations.RemoveField(
            model_name='role',
            name='artist',
        ),
        migrations.RemoveField(
            model_name='role',
            name='movie',
        ),
        migrations.DeleteModel(
            name='Vrf',
        ),
        migrations.DeleteModel(
            name='Access',
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
        migrations.DeleteModel(
            name='Device',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='Topologies',
        ),
    ]
