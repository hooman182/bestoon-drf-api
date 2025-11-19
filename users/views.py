from rest_framework import  permissions, generics
from .serializers import ProfileSerializer
from rest_framework.exceptions import PermissionDenied


class ProfileDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ProfileSerializer

    def get_object(self):
        return self.request.user.profile

    def perform_update(self, serializer):
        
        if not self.request.user.is_authenticated:
            raise PermissionDenied("User is not authenticated")
        
        serializer.save(user=self.request.user)
