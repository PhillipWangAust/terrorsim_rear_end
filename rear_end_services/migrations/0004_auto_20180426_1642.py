# Generated by Django 2.0.4 on 2018-04-26 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rear_end_services', '0003_auto_20180426_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terrorismdata',
            name='city',
            field=models.CharField(max_length=200, null=True, verbose_name='城市'),
        ),
        migrations.AlterField(
            model_name='terrorismdata',
            name='date',
            field=models.DateField(null=True, verbose_name='时间'),
        ),
        migrations.AlterField(
            model_name='terrorismdata',
            name='day',
            field=models.IntegerField(db_index=True, null=True, verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='terrorismdata',
            name='month',
            field=models.IntegerField(db_index=True, null=True, verbose_name='月份'),
        ),
        migrations.AlterField(
            model_name='terrorismdata',
            name='motive',
            field=models.TextField(null=True, verbose_name='动机'),
        ),
        migrations.AlterField(
            model_name='terrorismdata',
            name='num_kill',
            field=models.IntegerField(null=True, verbose_name='死亡人数'),
        ),
        migrations.AlterField(
            model_name='terrorismdata',
            name='num_wound',
            field=models.IntegerField(null=True, verbose_name='受伤人数'),
        ),
        migrations.AlterField(
            model_name='terrorismdata',
            name='prop_comment',
            field=models.TextField(null=True, verbose_name='损失情况'),
        ),
        migrations.AlterField(
            model_name='terrorismdata',
            name='prop_value',
            field=models.FloatField(null=True, verbose_name='经济损失'),
        ),
        migrations.AlterField(
            model_name='terrorismdata',
            name='summary',
            field=models.TextField(null=True, verbose_name='事件报道'),
        ),
        migrations.AlterField(
            model_name='terrorismdata',
            name='year',
            field=models.IntegerField(db_index=True, null=True, verbose_name='年份'),
        ),
    ]