# Generated by Django 4.2.3 on 2023-07-07 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dondesang', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entretien',
            name='code',
            field=models.CharField(default=1, editable=False, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
