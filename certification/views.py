from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Certification
from .serializers import CertificateSerializer
# Create your views here.


class CertificationList(APIView):
    def get(self, request):
        certification = Certification.objects.all()
        serializer = CertificateSerializer(certification, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CertificateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)      
    
class CertificationDetail(APIView):
    def get_object(self, pk):
        try:
            return Certification.objects.get(pk=pk)
        except Certification.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        certification = self.get_object(pk)
        if certification is None:
            return Response({"Certification not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = CertificateSerializer(certification)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        certification = self.get_object(pk)
        if certification is None:
            return Response({"Certification not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = CertificateSerializer(certification, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        certification = self.get_object(pk)
        if certification is None:
            return Response({"Certification not found"},status=status.HTTP_404_NOT_FOUND)
        certification.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        certification = self.get_object(pk)
        if certification is None:
            return Response({"Certification not found"},status=status.HTTP_404_NOT_FOUND)
        serializer = CertificateSerializer(certification, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)