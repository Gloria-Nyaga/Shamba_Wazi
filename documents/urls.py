from django.urls import path
from .views import DocumentUploadView, DocumentListView, DocumentDetailView, DocumentCreateDraftView, DocumentAgreementView

urlpatterns = [
    # path('create/', DocumentCreateView.as_view(), name='document-create'),
    path('upload/', DocumentUploadView.as_view(), name='document-upload'),
    path('files/', DocumentListView.as_view(), name='document-list'),
    path('files/<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
    path('agree/<int:pk>/', DocumentAgreementView.as_view(), name='document-agree'),
    path('create_draft/', DocumentCreateDraftView.as_view(), name='create-draft'),
]
