# Generated by Django 3.0.3 on 2020-03-05 19:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0007_appointments_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='available',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='doctor',
            name='max_slots',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='docid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor'),
        ),
    ]
