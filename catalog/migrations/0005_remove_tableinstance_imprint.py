# Generated by Django 3.1.2 on 2020-12-11 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20201211_1533'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tableinstance',
            name='imprint',
        ),
    ]