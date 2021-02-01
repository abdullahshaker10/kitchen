# Generated by Django 3.1.6 on 2021-02-01 17:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('New', 'New'), ('Preparing', 'Preparing'), ('Waiting Review', 'Waiting Review'), ('Ready', 'Ready'), ('Canceled', 'Canceled')], max_length=50)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='clients.client')),
            ],
        ),
    ]
