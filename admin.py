from django.contrib import admin
from . models import Study

@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    list_display = ('study_name', 'study_phase', 'sponser_name', 'study_description')
    search_fields = ('study_name', 'sponser_name')
    list_filter = ('study_phase',)


