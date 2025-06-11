from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Record


def record_list(request):
    records = Record.objects.all()
    paginator = Paginator(records, 10)  # Show 10 records per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'records/record_list.html', {'page_obj': page_obj})