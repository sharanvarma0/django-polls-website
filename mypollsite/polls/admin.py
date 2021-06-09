from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fields = ['question_text', 'pub_date']
    inlines = [ChoiceInline]
admin.site.register(Question, QuestionAdmin)
