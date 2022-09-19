from django.shortcuts import render


def logs_index(request):
    return render(request, 'logs/logs.html', {})
