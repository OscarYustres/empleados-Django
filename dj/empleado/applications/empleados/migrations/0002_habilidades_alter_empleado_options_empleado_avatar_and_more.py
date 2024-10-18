# Generated by Django 5.1.2 on 2024-10-14 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0003_alter_departamento_options_alter_departamento_name_and_more'),
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades Empleados',
            },
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['first_name', 'last_name'], 'verbose_name': 'Mi Empleado', 'verbose_name_plural': 'Empleados de la empresa'},
        ),
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
        migrations.AlterUniqueTogether(
            name='empleado',
            unique_together={('first_name', 'departamento')},
        ),
    ]
