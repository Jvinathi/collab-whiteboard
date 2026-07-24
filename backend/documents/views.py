from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Workspace, WorkspaceMembership, Document
from .serializers import (
    WorkspaceSerializer, DocumentListSerializer, DocumentDetailSerializer
)


class WorkspaceViewSet(viewsets.ModelViewSet):
    serializer_class = WorkspaceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # only show workspaces the logged-in user is a member of
        return Workspace.objects.filter(memberships__user=self.request.user).distinct()

    def perform_create(self, serializer):
        workspace = serializer.save(owner=self.request.user)
        WorkspaceMembership.objects.create(
            workspace=workspace, user=self.request.user, role=WorkspaceMembership.Role.OWNER
        )


class DocumentViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list':
            return DocumentListSerializer
        return DocumentDetailSerializer

    def get_queryset(self):
        # only documents in workspaces the user belongs to
        return Document.objects.filter(workspace__memberships__user=self.request.user).distinct()

    def perform_create(self, serializer):
        workspace = serializer.validated_data['workspace']
        is_member = WorkspaceMembership.objects.filter(
            workspace=workspace, user=self.request.user
        ).exists()
        if not is_member:
            raise PermissionDenied("You are not a member of this workspace.")
        serializer.save(created_by=self.request.user)
