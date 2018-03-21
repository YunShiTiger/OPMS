# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-03-05 11:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('record', '0004_auto_20180209_1551'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DeployRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Tag')),
                ('deploy_time', models.DateTimeField(verbose_name='添加时间')),
                ('ps', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('add_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='添加者')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='record.Areas', verbose_name='区级')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='record.Cities', verbose_name='市级')),
                ('pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.Provinces', verbose_name='省份')),
            ],
            options={
                'verbose_name': '发布记录表',
                'verbose_name_plural': '发布记录表',
            },
        ),
        migrations.CreateModel(
            name='MiddlewareRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tomcat_version', models.CharField(blank=True, max_length=20, null=True, verbose_name='TOMCAT版本')),
                ('jdk_version', models.CharField(blank=True, max_length=20, null=True, verbose_name='JDK版本')),
                ('other_version', models.TextField(blank=True, null=True, verbose_name='其它服务版本')),
                ('ps', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('add_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='添加者')),
                ('area', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='record.Areas', verbose_name='区级')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='record.Cities', verbose_name='市级')),
                ('pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='record.Provinces', verbose_name='省份')),
            ],
            options={
                'verbose_name': '中间件表',
                'verbose_name_plural': '中间件表',
            },
        ),
        migrations.CreateModel(
            name='ProductionService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='服务名称')),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('add_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='添加人')),
            ],
            options={
                'verbose_name': '服务表',
                'verbose_name_plural': '服务表',
            },
        ),
        migrations.AddField(
            model_name='middlewarerecord',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_deploy.ProductionService', verbose_name='服务'),
        ),
        migrations.AddField(
            model_name='deployrecord',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online_deploy.ProductionService', verbose_name='服务'),
        ),
    ]