# Generated by Django 2.2.3 on 2019-10-15 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BatchCmdLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64, verbose_name='操作人')),
                ('hosts', models.TextField(verbose_name='主机信息')),
                ('cmd', models.TextField(blank=True, null=True, verbose_name='命令详情')),
                ('detail', models.CharField(blank=True, max_length=128, null=True, verbose_name='结果详情(文件名)')),
                ('address', models.GenericIPAddressField(blank=True, null=True, verbose_name='IP地址')),
                ('useragent', models.CharField(blank=True, max_length=512, null=True, verbose_name='User_Agent')),
                ('start_time', models.DateTimeField(verbose_name='会话开始时间')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='事件时间')),
            ],
            options={
                'verbose_name': '批量命令日志',
                'verbose_name_plural': '批量命令日志',
                'ordering': ['-create_time'],
            },
        ),
    ]