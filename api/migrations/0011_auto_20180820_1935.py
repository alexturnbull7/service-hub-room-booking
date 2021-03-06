# Generated by Django 2.0 on 2018-08-20 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20180815_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='bookings',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='api.Booking'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='lead_booker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
