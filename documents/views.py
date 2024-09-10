from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
from .models import Document
from .serializers import DocumentSerializer

class DocumentUploadView(generics.CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentListView(APIView):
    def get(self, request):
        documents = Document.objects.all()
        serializer = DocumentSerializer(documents, many=True)
        return Response(serializer.data)

class DocumentDetailView(APIView):
    def get(self, request, pk):
        document = get_object_or_404(Document, pk=pk)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)

    def put(self, request, pk):
        document = get_object_or_404(Document, pk=pk)
        serializer = DocumentSerializer(document, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentCreateDraftView(APIView):
    def post(self, request):
        data = request.data.copy()
        title = data.get('title', '')
        
        if title.lower() == "drafted contract":
            data['is_draft'] = True
        
        serializer = DocumentSerializer(data=data)
        if serializer.is_valid():
            document = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DocumentAgreementView(APIView):
    def patch(self, request, pk):
        document = get_object_or_404(Document, pk=pk)
        user = request.user
        
        if not (user == document.owner or user in [document.land_owner, document.land_seller]):
            return Response({'detail': 'You do not have permission to agree to this document.'}, status=status.HTTP_403_FORBIDDEN)
        
        if user == document.land_owner:
            document.land_owner_agreed = True
        elif user == document.land_seller:
            document.land_seller_agreed = True
        
        document.save()
        return Response({'detail': 'Agreement recorded successfully.'}, status=status.HTTP_200_OK)

    def get(self, request, pk):
        document = get_object_or_404(Document, pk=pk)
        serializer = DocumentSerializer(document)
        return Response(serializer.data)
