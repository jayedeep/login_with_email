# Generated by Django 3.1.2 on 2020-10-31 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201031_0417'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='contact',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]
