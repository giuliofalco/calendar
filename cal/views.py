from django.shortcuts import render, get_object_or_404, redirect
from datetime import date, datetime, timedelta
import calendar
from .models import DayEntry
from .forms import DayEntryForm

def calendar_view(request):
    today = date.today()
    year = int(request.GET.get('year', today.year))
    month = int(request.GET.get('month', today.month))

    cal = calendar.Calendar()
    month_days = cal.monthdayscalendar(year, month)

    context = {
        'month_days': month_days,
        'year': year,
        'month': month,
        'month_name': calendar.month_name[month],
    }
    return render(request, 'cal/calendar_view.html', context)

def day_editor(request, year, month, day):
    entry_date = date(year, month, day)
    day_entry, created = DayEntry.objects.get_or_create(date=entry_date)

    if request.method == 'POST':
        form = DayEntryForm(request.POST, instance=day_entry)
        if form.is_valid():
            form.save()
            return redirect('calendar_view')
    else:
        form = DayEntryForm(instance=day_entry)

    return render(request, 'cal/day_editor.html', {'form': form, 'entry_date': entry_date})

