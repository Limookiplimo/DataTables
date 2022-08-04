# Generated by Django 3.2.7 on 2022-07-31 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=50, null=True)),
                ('title', models.CharField(choices=[('Owner', 'Owner'), ('CEO', 'CEO'), ('Manager', 'Manager'), ('Ass-Manager', 'Ass-Manager'), ('Clerk', 'Clerk')], max_length=50, null=True)),
                ('occupation', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('salary', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=50, null=True)),
            ],
        ),
    ]