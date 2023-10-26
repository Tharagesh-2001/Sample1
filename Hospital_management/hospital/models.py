from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import RegexValidator

class DoctorManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class Doctor(AbstractBaseUser):
    SPECIALITY_CHOICES = (
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
    )

    doctor_name = models.CharField(max_length=255)
    doctor_hospital_name = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255, choices=SPECIALITY_CHOICES)
    gender = models.CharField(max_length=255)
    experience = models.PositiveIntegerField()
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')])
    address = models.TextField(blank=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = DoctorManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["doctor_name", "doctor_hospital_name", "speciality", "gender", "experience", "phone"]

    def __str__(self):
        return self.doctor_name

class PatientManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class Patient(AbstractBaseUser):
    GENDER_CHOICES = (
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    )

    patient_name = models.CharField(max_length=255)
    patient_gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{10}$')])
    patient_address = models.TextField(blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    blood_pressure = models.CharField(max_length=20)
    problem = models.CharField(max_length=255)
    preferred_doctor = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = PatientManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["patient_name", "patient_gender", "phone", "weight", "height", "blood_pressure", "problem", "preferred_doctor"]

    def __str__(self):
        return self.patient_name