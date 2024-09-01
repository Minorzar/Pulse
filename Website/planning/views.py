from django.shortcuts import render
from .models import Planning


# Create your views here.
def calendar(request):
    plannings = Planning.objects.all().order_by('day', 'start')
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    calDic = {day: [] for day in days}

    for planning in plannings:
        day = days[planning.day]
        calDic[day].append(planning)

    context = {'calender': calDic}
    return render(request, 'calendar.html', context)
