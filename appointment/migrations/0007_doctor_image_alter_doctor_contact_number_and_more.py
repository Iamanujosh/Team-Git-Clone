# Generated by Django 5.1 on 2024-09-29 02:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0006_remove_doctor_contact_info_doctor_contact_number_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='doctors/'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='contact_number',
            field=models.CharField(default='0000000000', max_length=15),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='email',
            field=models.EmailField(default='doctor@example.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='experience',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialization',
            field=models.CharField(default='General Practitioner', max_length=100),
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_date', models.DateTimeField(auto_now_add=True)),
                ('reason', models.TextField(default='General consultation')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointment.doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
