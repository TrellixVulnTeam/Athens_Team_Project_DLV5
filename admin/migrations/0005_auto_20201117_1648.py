# Generated by Django 3.1.2 on 2020-11-17 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0004_customer_tbl_c_join'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_tbl',
            name='c_gender',
            field=models.CharField(blank=True, choices=[('남', '남'), ('여', '여')], max_length=10, null=True),
        ),
    ]
