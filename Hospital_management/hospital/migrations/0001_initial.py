# Generated by Django 4.2.5 on 2023-09-28 07:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("doctor_name", models.CharField(max_length=255)),
                ("doctor_hospital_name", models.CharField(max_length=255)),
                (
                    "speciality",
                    models.CharField(
                        choices=[
                            ("Pediatrician", "Pediatrician"),
                            ("Gynecologist", "Gynecologist"),
                            ("Cardiologist", "Cardiologist"),
                            ("Oncologist", "Oncologist"),
                            ("Gastroenterologist", "Gastroenterologist"),
                            ("Pulmonologist", "Pulmonologist"),
                            ("Nephrologist", "Nephrologist"),
                            ("Endocrinologist", "Endocrinologist"),
                            ("Ophthalmologist", "Ophthalmologist"),
                            ("Otolaryngologist", "Otolaryngologist"),
                            ("Dermatologist", "Dermatologist"),
                            ("Psychiatrist", "Psychiatrist"),
                            ("Neurologist", "Neurologist"),
                            ("Radiologist", "Radiologist"),
                            ("Anesthesiologist", "Anesthesiologist"),
                        ],
                        max_length=255,
                    ),
                ),
                ("gender", models.CharField(max_length=255)),
                ("experience", models.PositiveIntegerField()),
                (
                    "phone",
                    models.CharField(
                        max_length=10,
                        validators=[django.core.validators.RegexValidator("^\\d{10}$")],
                    ),
                ),
                ("address", models.TextField(blank=True)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("is_active", models.BooleanField(default=True)),
                ("is_staff", models.BooleanField(default=False)),
            ],
            options={"abstract": False,},
        ),
    ]
