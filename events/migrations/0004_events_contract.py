# Generated by Django 3.0.3 on 2020-07-22 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0003_auto_20200722_1927'),
        ('events', '0003_auto_20200722_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Contract_Events', to='contracts.Contract'),
        ),
    ]