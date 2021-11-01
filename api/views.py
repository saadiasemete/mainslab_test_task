from rest_framework import mixins, views, viewsets
from django.core.mail import send_mail, BadHeaderError
from models import SentMessageData
from serializers import SentMessageDataSerializer
from django.http import JsonResponse


class EmailViewSet(mixins.ListModelMixin,
            mixins.RetrieveModelMixin,
            viewsets.GenericViewSet):
    queryset = SentMessageData.objects.all()
    serializer_class = SentMessageDataSerializer

    def create(self, request):
        message = request.POST.get('message')
        if not message:
            return JsonResponse({'Bad message': 'No message'}, status=400)
        serializer = SentMessageDataSerializer(data=request.data)
        if serializer.is_valid():
            from_email = None
            try:
                send_mail(
                    serializer.validated_data['subject'], 
                    message, 
                    from_email, 
                    serializer.validated_data['to_email'])
                serializer.save()
                return JsonResponse(serializer.data, status=200)
            except BadHeaderError:
                return JsonResponse({'Bad message': 'Header is corrupted'}, status=400)
        else:
            return JsonResponse(serializer.errors, status=400)

class RetrieveDayAnalytics(views.APIView):
    def get(request):
        return JsonResponse(SentMessageData.analyze_last_24_hours(), 200)