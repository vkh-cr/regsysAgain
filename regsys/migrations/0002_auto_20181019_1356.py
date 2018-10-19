# Generated by Django 2.1.2 on 2018-10-19 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regsys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailregistration',
            name='id',
        ),
        migrations.RemoveField(
            model_name='detailregistration',
            name='reg_id',
        ),
        migrations.AlterField(
            model_name='detailregistration',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='detailregistration',
            name='fri_night',
            field=models.CharField(choices=[('Postel', 'Ubytování s příslušenstvím - postel'), ('Spacak', 'Ubytování spacák a karimatka'), ('Sirak', 'Bez ubytovani')], default='Postel', max_length=10),
        ),
        migrations.AlterField(
            model_name='detailregistration',
            name='price',
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='detailregistration',
            name='reg_type',
            field=models.CharField(choices=[('Ucastnik', 'Ucastnik'), ('Dobrovolnik', 'Dobrovolnik'), ('Host', 'Host'), ('Duchovni', 'Duchovni'), ('Tym', 'Tym')], default='Ucastnik', max_length=10),
        ),
        migrations.AlterField(
            model_name='detailregistration',
            name='sat_night',
            field=models.CharField(choices=[('Postel', 'Ubytování s příslušenstvím - postel'), ('Spacak', 'Ubytování spacák a karimatka'), ('Sirak', 'Bez ubytovani')], default='Postel', max_length=10),
        ),
        migrations.AlterField(
            model_name='detailregistration',
            name='status',
            field=models.CharField(choices=[('Ceka na zaplaceni', 'Ceka na zaplaceni'), ('Zaplaceno', 'Zaplaceno'), ('Platba vyprsela', 'Platba vyprsela'), ('Zruseno', 'Zruseno')], default='Ceka na zaplaceni', max_length=10),
        ),
        migrations.AlterField(
            model_name='detailregistration',
            name='var_symbol',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]