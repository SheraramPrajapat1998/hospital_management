# Generated by Django 3.1.7 on 2021-04-18 13:40

import accounts.validators
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_type', models.CharField(choices=[('patient', 'Patient'), ('doctor', 'Doctor'), ('receptionist', 'Receptionist'), ('admin', 'Admin'), ('nurse', 'Nurse'), ('accountant', 'Accountant')], default='patient', max_length=20)),
                ('date_of_birth', models.DateField(blank=True, null=True, validators=[accounts.validators.validate_future_date])),
                ('mobile_num', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+9199999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('date_joining', models.DateTimeField(auto_now_add=True)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], default='male', max_length=10)),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(blank=True, max_length=50, null=True)),
                ('blood_group', models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=5, null=True)),
                ('marital_status', models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('widowed', 'Widowed'), ('divorced', 'Divorced')], default='single', max_length=10)),
                ('photo', models.ImageField(blank=True, default='default.png', upload_to='patients/%Y/%m/%d')),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.BigIntegerField(default=0)),
                ('state', models.CharField(max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_number', models.BigIntegerField(verbose_name='Aadhar Number')),
                ('empCategory', models.CharField(blank=True, max_length=20, verbose_name='Employee Category')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_discharge', models.DateTimeField(auto_now=True)),
                ('allergies', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_number', models.BigIntegerField(verbose_name='Aadhar Number')),
                ('empCategory', models.CharField(blank=True, max_length=20, verbose_name='Employee Category')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Nurses',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.CharField(max_length=20)),
                ('speciality', models.CharField(max_length=20)),
                ('department', models.CharField(choices=[('Cardiologist', 'Cardiologist'), ('Dermatologists', 'Dermatologists'), ('Emergency Medicine Specialists', 'Emergency Medicine Specialists'), ('Allergists/Immunologists', 'Allergists/Immunologists'), ('Anesthesiologists', 'Anesthesiologists'), ('Colon and Rectal Surgeons', 'Colon and Rectal Surgeons')], max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Accountant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhar_number', models.BigIntegerField(verbose_name='Aadhar Number')),
                ('empCategory', models.CharField(blank=True, max_length=20, verbose_name='Employee Category')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
