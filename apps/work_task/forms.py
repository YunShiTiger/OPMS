########################################################################################################################
## Django 自带模块导入
########################################################################################################################
from django import forms

########################################################################################################################
## 系统自带模块导入
########################################################################################################################


########################################################################################################################
## 自建模块导入
########################################################################################################################
from .models import *


########################################################################################################################
## 添加任务
########################################################################################################################
class AddTaskForm(forms.ModelForm):
    class Meta:
        model = UserWorkTask
        exclude = ['status', 'create_user', 'add_time']








