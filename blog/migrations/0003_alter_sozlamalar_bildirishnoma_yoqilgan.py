# Generated by Django 5.1.1 on 2025-04-05 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_data_user_date_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sozlamalar',
            name='bildirishnoma_yoqilgan',
            field=models.BooleanField(choices=[('Yes', 'Ha'), ('Uzbek', 'Uzbek'), ('Rus', 'Rus'), ('English', 'English')], default=True),
        ),
    ]
