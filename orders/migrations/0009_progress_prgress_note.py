# Generated by Django 3.1.6 on 2021-02-02 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20210202_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='progress',
            name='prgress_note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
