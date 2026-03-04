from django.shortcuts import render
from .models import FireAlert
import random

def home(request):
    return render(request, 'home.html')

def detect_fire(request):
    temperature = random.randint(20, 100)

    if temperature > 60:
        status = "🔥 Fire Detected!"
    else:
        status = "✅ Safe"

    FireAlert.objects.create(
        temperature=temperature,
        status=status
    )

    return render(request, 'detect.html', {
        'temperature': temperature,
        'status': status
    })

def view_alerts(request):
    alerts = FireAlert.objects.all().order_by('-created_at')
    return render(request, 'alerts.html', {'alerts': alerts})