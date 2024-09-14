from django.contrib import admin
from testapp.models import addquiz_model,answer_model

# Register your models here.
class addquiz_admin(admin.ModelAdmin):
    list_display=[
        'ques','A','B','C','D','Ans'
    ]
class answer_admin(admin.ModelAdmin):
    list_display=[
        'Selected_ans','unique_value1'
    ]
admin.site.register(addquiz_model,addquiz_admin)
admin.site.register(answer_model,answer_admin)
