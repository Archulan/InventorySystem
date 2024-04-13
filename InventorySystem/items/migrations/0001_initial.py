# Generated by Django 5.0.4 on 2024-04-13 04:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('itemtypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('item_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='itemtypes.itemtype')),
            ],
        ),
    ]