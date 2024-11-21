# Generated by Django 5.1.3 on 2024-11-21 19:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member_app', '0007_alter_convite_limiteconvites'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='convite',
            name='email',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='convite',
            name='mensagem',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='convite',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='convite',
            name='validade',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
