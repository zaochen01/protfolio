# Generated by Django 3.0.2 on 2020-02-05 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prot', '0003_prot_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prot',
            name='image',
            field=models.ImageField(default='default.png', upload_to='image/'),
        ),
    ]