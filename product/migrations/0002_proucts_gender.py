# Generated by Django 4.2.5 on 2023-09-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proucts',
            name='gender',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women')], default='', max_length=10),
            preserve_default=False,
        ),
    ]
