# Generated by Django 3.1.2 on 2020-11-18 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admin', '0005_auto_20201117_1648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='admin.customer_tbl')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_order_id', models.CharField(blank=True, max_length=120, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=120, null=True)),
                ('amount', models.PositiveIntegerField(default=0, null=True)),
                ('transaction_status', models.CharField(blank=True, max_length=220, null=True)),
                ('type', models.CharField(blank=True, max_length=120, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.order')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('l_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='order_products', to='admin.lecture_tbl')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.order')),
            ],
        ),
    ]
