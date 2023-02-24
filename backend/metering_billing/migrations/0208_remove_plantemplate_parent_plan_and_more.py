# Generated by Django 4.0.5 on 2023-02-24 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metering_billing', '0207_transfer_custom_plans'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plantemplate',
            name='parent_plan',
        ),
        migrations.RemoveField(
            model_name='plantemplate',
            name='target_customer',
        ),
        migrations.AddField(
            model_name='historicalplanversion',
            name='addon_spec',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='metering_billing.addonspecification'),
        ),
        migrations.AddField(
            model_name='plantemplate',
            name='is_addon',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='planversion',
            name='addon_spec',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='plan_version', to='metering_billing.addonspecification'),
        ),
    ]
