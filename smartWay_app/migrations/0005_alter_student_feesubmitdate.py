# Generated by Django 4.2.4 on 2023-10-25 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartWay_app', '0004_student_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='FeeSubmitDate',
            field=models.DateField(null=True),
        ),
    ]
