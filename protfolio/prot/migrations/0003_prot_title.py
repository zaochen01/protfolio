# Generated by Django 3.0.2 on 2020-02-05 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prot', '0002_auto_20200205_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='prot',
            name='title',
            field=models.CharField(default='作品标题', max_length=50),
        ),
    ]
