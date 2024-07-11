from django.contrib import admin
from .models import Planning


class PlanningAdmin(admin.ModelAdmin):
    list_display = ('entry', 'get_day_display', 'get_start_display', 'get_end_display', 'disc')

    search_fields = ('entry', 'disc')
    list_filter = ('day',)
    ordering = ('day', 'start')
    fieldsets = (
        (None, {
            'fields': ('entry', 'day', 'start', 'end', 'disc')
        }),
    )

    def get_day_display(self, obj):
        days = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
        return days[obj.day] if 0 <= obj.day < len(days) else 'Invalid day'

    get_day_display.short_description = 'Day'

    def get_start_display(self, obj):
        return f'{obj.start}:00' if 0 <= obj.start < 24 else 'Invalid time'

    get_start_display.short_description = 'Start Time'

    def get_end_display(self, obj):
        return f'{obj.end + 1}:00' if 0 <= obj.end < 24 else 'Invalid time'

    get_end_display.short_description = 'End Time'


admin.site.register(Planning, PlanningAdmin)
