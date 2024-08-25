from django.contrib import admin

from .models import Question, QuestionSet, Quiz, Answer, AnswerDetail, Option


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('name', 'set')
    list_filter = ['name', 'set']
    search_fields = ['name']


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'amount')
    search_fields = ['name', 'author', 'amount']



admin.site.register(Answer)
admin.site.register(AnswerDetail)
admin.site.register(Option)
admin.site.register(Question, QuestionAdmin)
admin.site.register(QuestionSet)
admin.site.register(Quiz, QuizAdmin)
