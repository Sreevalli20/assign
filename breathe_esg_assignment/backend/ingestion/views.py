from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import EmissionRecord

@api_view(['POST'])
def upload_data(request):
    EmissionRecord.objects.create(
        source_type='sap',
        scope='Scope 1',
        category='Diesel',
        quantity=500,
        unit='L',
        co2e=1340.5
    )
    return Response({'message': 'Sample ESG data uploaded successfully'})

@api_view(['GET'])
def records(request):
    data = list(EmissionRecord.objects.values())
    return Response(data)