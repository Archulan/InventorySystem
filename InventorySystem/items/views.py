from rest_framework import viewsets, status
from .models import Item
from .serializers import ItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from items.serializers import ItemSerializer
from batches.serializers import BatchSerializer
from itemtypes.serializers import ItemTypeSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class SubmitData(APIView):
    def post(self, request, *args, **kwargs):
        item_types_data = request.data.get('item_types', [])
        items_data = request.data.get('items', [])
        batches_data = request.data.get('batches', [])

        # Process item types
        for it_data in item_types_data:
            serializer = ItemTypeSerializer(data=it_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Process items
        for item_data in items_data:
            serializer = ItemSerializer(data=item_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Process batches
        for batch_data in batches_data:
            serializer = BatchSerializer(data=batch_data)
            if serializer.is_valid():
                serializer.save()
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Data submitted successfully"}, status=status.HTTP_201_CREATED)