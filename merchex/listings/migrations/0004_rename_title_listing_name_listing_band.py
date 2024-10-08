# Generated by Django 5.1.1 on 2024-09-18 15:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='listing',
            name='band',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='listings.band'),
            preserve_default=False,
        ),
    ]
