# Generated by Django 3.2.15 on 2022-09-23 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contentshub', '0003_alter_master_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='klass',
            options={'ordering': ('-id',)},
        ),
        migrations.AlterModelOptions(
            name='master',
            options={'ordering': ('-id',)},
        ),
    ]
