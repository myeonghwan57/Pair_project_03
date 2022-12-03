# Generated by Django 3.2.13 on 2022-12-02 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hobby', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='category',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='accepted',
            name='hobby',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accepted', to='hobby.hobby'),
        ),
    ]
