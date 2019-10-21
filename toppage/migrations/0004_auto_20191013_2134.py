# Generated by Django 2.1 on 2019-10-13 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toppage', '0003_auto_20191011_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='administrative',
            field=models.CharField(blank=True, max_length=20, verbose_name='管理費'),
        ),
        migrations.AlterField(
            model_name='article',
            name='balArea',
            field=models.CharField(blank=True, max_length=20, verbose_name='バルコニー（テラス）面積'),
        ),
        migrations.AlterField(
            model_name='article',
            name='environmentMet',
            field=models.CharField(blank=True, max_length=20, verbose_name='距離1'),
        ),
        migrations.AlterField(
            model_name='article',
            name='environmentMin',
            field=models.CharField(blank=True, max_length=10, verbose_name='時間1'),
        ),
        migrations.AlterField(
            model_name='article',
            name='exclusiveArea',
            field=models.CharField(blank=True, max_length=20, verbose_name='専有面積'),
        ),
        migrations.AlterField(
            model_name='article',
            name='price',
            field=models.CharField(blank=True, max_length=20, verbose_name='価格'),
        ),
        migrations.AlterField(
            model_name='article',
            name='priceSquare',
            field=models.CharField(blank=True, max_length=20, verbose_name='㎡単価'),
        ),
        migrations.AlterField(
            model_name='article',
            name='priceTsubo',
            field=models.CharField(blank=True, max_length=20, verbose_name='坪単価'),
        ),
        migrations.AlterField(
            model_name='article',
            name='repairReserve',
            field=models.CharField(blank=True, max_length=20, verbose_name='修繕積立金'),
        ),
        migrations.AlterField(
            model_name='article',
            name='station2',
            field=models.CharField(blank=True, max_length=200, verbose_name='その他交通手段'),
        ),
        migrations.AlterField(
            model_name='article',
            name='walkMet1',
            field=models.CharField(blank=True, max_length=20, verbose_name='徒歩（m）2（1）'),
        ),
        migrations.AlterField(
            model_name='article',
            name='walkMet2',
            field=models.CharField(blank=True, max_length=20, verbose_name='交通（m）2'),
        ),
        migrations.AlterField(
            model_name='article',
            name='walkMin1',
            field=models.CharField(blank=True, max_length=10, verbose_name='徒歩（分）1（1）'),
        ),
        migrations.AlterField(
            model_name='article',
            name='walkMin2',
            field=models.CharField(blank=True, max_length=10, verbose_name='交通（分）1'),
        ),
    ]
