# Generated by Django 2.2.2 on 2019-07-21 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CariKodu', models.CharField(max_length=10)),
                ('CariUnvani', models.CharField(max_length=150)),
                ('VergiDairesi', models.CharField(max_length=50)),
                ('VergiNumarasi', models.IntegerField()),
                ('IsSaved', models.BooleanField(default=False)),
                ('IsVerified', models.BooleanField(default=False)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('IsCanceled', models.BooleanField(default=False)),
                ('IsTransferred', models.BooleanField(default=False)),
                ('IsTransferCache', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CariIrtibat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CariKodu', models.CharField(max_length=10)),
                ('Il', models.CharField(max_length=50)),
                ('Ilce', models.CharField(max_length=50)),
                ('Adres', models.CharField(max_length=150)),
                ('PostaKodu', models.IntegerField()),
                ('KEP', models.EmailField(max_length=254, null=True)),
                ('Tel1', models.CharField(max_length=15)),
                ('Tel2', models.CharField(max_length=15, null=True)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('WebSitesi', models.CharField(max_length=50, null=True)),
                ('IsSaved', models.BooleanField(default=False)),
                ('IsVerified', models.BooleanField(default=False)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('IsCanceled', models.BooleanField(default=False)),
                ('IsTransferred', models.BooleanField(default=False)),
                ('IsTransferCache', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CariLokasyon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CariKodu', models.CharField(max_length=10)),
                ('LokasyonKodu', models.CharField(max_length=10, null=True)),
                ('LokasyonDetay', models.CharField(max_length=100, null=True)),
                ('IsSaved', models.BooleanField(default=False)),
                ('IsVerified', models.BooleanField(default=False)),
                ('IsDeleted', models.BooleanField(default=False)),
                ('IsCanceled', models.BooleanField(default=False)),
                ('IsTransferred', models.BooleanField(default=False)),
                ('IsTransferCache', models.BooleanField(default=False)),
            ],
        ),
    ]