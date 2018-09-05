# Generated by Django 2.0 on 2018-08-15 15:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0006_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('notes', models.TextField()),
                ('guests', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='guests', to=settings.AUTH_USER_MODEL)),
                ('lead_booker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='Status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='UserType',
            new_name='userType',
        ),
    ]
