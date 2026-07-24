from rest_framework import serializers
from .models import Workspace, WorkspaceMembership, Document
from accounts.serializers import UserSerializer


class WorkspaceMembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = WorkspaceMembership
        fields = ('id', 'user', 'role', 'joined_at')


class WorkspaceSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    member_count = serializers.SerializerMethodField()

    class Meta:
        model = Workspace
        fields = ('id', 'name', 'owner', 'member_count', 'created_at', 'updated_at')

    def get_member_count(self, obj):
        return obj.memberships.count()


class DocumentListSerializer(serializers.ModelSerializer):
    """Lightweight — used for list views, excludes heavy `content` field."""
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Document
        fields = ('id', 'workspace', 'title', 'created_by', 'created_at', 'updated_at')


class DocumentDetailSerializer(serializers.ModelSerializer):
    """Full detail — includes `content`, used when opening a single document."""
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Document
        fields = ('id', 'workspace', 'title', 'content', 'created_by', 'created_at', 'updated_at')