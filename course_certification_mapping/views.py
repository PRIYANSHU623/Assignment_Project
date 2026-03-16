from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import CourseCertificationMapping
from .serializer import CourseCertificationMappingSerializer


class CourseCertificationMappingList(APIView):

    def get(self, request):
        """
        List vendor-product mappings
        Supports filtering by vendor_id
        Example: /api/vendor-product-mappings/?vendor_id=1
        """

        queryset = CourseCertificationMapping.objects.filter(is_active=True)

        vendor_id = request.query_params.get("vendor_id")

        if vendor_id:
            queryset = queryset.filter(vendor_id=vendor_id)

        serializer = CourseCertificationMappingSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Create vendor-product mapping
        """

        serializer = CourseCertificationMappingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseCertificationMappingDetail(APIView):

    def get_object(self, pk):
        try:
            return CourseCertificationMapping.objects.get(pk=pk, is_active=True)
        except CourseCertificationMapping.DoesNotExist:
            return None

    def get(self, request, pk):
        """
        Retrieve mapping
        """

        mapping = self.get_object(pk)

        if mapping is None:
            return Response(
                {"error": "Mapping not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CourseCertificationMappingSerializer(mapping)
        return Response(serializer.data)

    def put(self, request, pk):
        """
        Update mapping
        """

        mapping = self.get_object(pk)

        if mapping is None:
            return Response(
                {"error": "Mapping not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CourseCertificationMappingSerializer(mapping, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        """
        Partial update mapping
        """

        mapping = self.get_object(pk)

        if mapping is None:
            return Response(
                {"error": "Mapping not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = CourseCertificationMappingSerializer(
            mapping,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """
        Soft delete mapping
        """

        mapping = self.get_object(pk)

        if mapping is None:
            return Response(
                {"error": "Mapping not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        mapping.is_active = False
        mapping.save()

        return Response(
            {"message": "Mapping deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )