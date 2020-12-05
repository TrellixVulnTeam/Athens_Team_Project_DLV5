# Generated by Django 3.1.3 on 2020-12-01 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0016_merge_20201201_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consult_tbl',
            name='cu_res_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='lecture_tbl',
            name='l_desc',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='test_detail_tbl',
            name='td_choice_1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='test_detail_tbl',
            name='td_choice_2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='test_detail_tbl',
            name='td_choice_3',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='test_detail_tbl',
            name='td_choice_4',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='test_detail_tbl',
            name='td_question',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]