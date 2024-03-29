# Generated by Django 4.1.4 on 2022-12-17 00:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0002_remove_campaign_completed_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='due_date',
            field=models.DateField(default=datetime.date(2023, 3, 17)),
        ),
    ]
