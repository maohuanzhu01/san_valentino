from django.http import JsonResponse
from datetime import datetime
from .models import DateCounter
from django.views.decorators.csrf import csrf_exempt
import json

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
            input_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
            description = data.get('description', '')
            
            # Salva la data nel database
            date_counter = DateCounter.objects.create(
                start_date=input_date,
                description=description
            )
            
            # Calcola i giorni passati
            days_passed = date_counter.days_passed()
            
            return JsonResponse({
                'days_passed': days_passed,
                'start_date': input_date.strftime('%Y-%m-%d'),
                'description': description
            })
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
            
    return JsonResponse({'error': 'Solo richieste POST sono permesse'}, status=405)