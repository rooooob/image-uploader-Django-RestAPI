from .models import Image
from .serializers import ImageSerializer
from rest_framework.response import Response
from rest_framework.decorators import parser_classes, api_view
from rest_framework.parsers import FileUploadParser


@api_view(['GET'])
def images_view(request):
    images = Image.objects.all()
    serializer = ImageSerializer(images, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def image_detail(request, pk):
    image = Image.objects.get(id=pk)
    serializer = ImageSerializer(image, many=False)

    return Response(serializer.data)


@api_view(['POST'])
@parser_classes([FileUploadParser, ])
def image_create(request, format=None):
    serializer = ImageSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    
    print(f'&&: {request}, {request.data}')
    return Response({'received data': serializer.data})
    