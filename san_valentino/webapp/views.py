from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import json
from django.shortcuts import render

from rest_framework import viewsets
from .models import Message
from .serializers import MessageSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

@csrf_exempt
def calculate_days(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            start_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
            today = datetime.now().date()
            days_passed = (today - start_date).days
            
            return JsonResponse({
                'days_passed': days_passed,
                'start_date': data['date'],
                'description': data.get('description', '')
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    
    return JsonResponse({'error': 'Only POST method is allowed'}, status=405)

def test_view(request):
    return render(request, 'test.html')