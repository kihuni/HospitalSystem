# Generated by Django 4.1.7 on 2023-03-22 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myproject', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appoitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctorname', models.CharField(max_length=50)),
                ('doctoremail', models.EmailField(max_length=50)),
                ('patientname', models.CharField(max_length=50)),
                ('patientemail', models.EmailField(max_length=50)),
                ('Appoitmentdate', models.DateField(max_length=10)),
                ('Appoitmenttime', models.TimeField(max_length=100)),
                ('symptoms', models.BooleanField()),
                ('prescription', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('gender', models.CharField(max_length=10)),
                ('phonenumber', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('bloodgroup', models.CharField(max_length=5)),
                ('specialization', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('gender', models.CharField(max_length=10)),
                ('phonenumber', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=16)),
                ('gender', models.CharField(max_length=10)),
                ('phonenumber', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('birthdate', models.DateField()),
                ('bloodgroup', models.CharField(max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='Feature',
        ),
    ]
