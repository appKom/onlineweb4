# Generated by Django 2.1.9 on 2019-08-24 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0033_auto_20190823_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='FikenOrderLine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('vat_type', models.CharField(choices=[('NONE', 'NONE'), ('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('RAW_FISH', 'RAW_FISH'), ('LOW', 'LOW'), ('EXEMPT_IMPORT_EXPORT', 'EXEMPT_IMPORT_EXPORT'), ('EXEMPT', 'EXEMPT'), ('OUTSIDE', 'OUTSIDE'), ('EXEMPT_REVERSE', 'EXEMPT_REVERSE')], max_length=200)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='fikenorderline',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_lines', to='payment.FikenSale'),
        ),
    ]