# Generated by Django 4.2.5 on 2023-09-07 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='outcome',
            field=models.CharField(default='Manual Review', max_length=200),
            preserve_default=False,
        ),
    ]
