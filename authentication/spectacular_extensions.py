from drf_spectacular.extensions import OpenApiViewExtension
from drf_spectacular.utils import extend_schema, extend_schema_view
from djoser.views import UserViewSet

# ------------------------------------------------------------


class UserViewSetExtension(OpenApiViewExtension):
    ''' grouping endpoints in swagger ui '''
    
    target_class = "djoser.views.UserViewSet"

    def view_replacement(self):
        @extend_schema_view(
            create=extend_schema(tags=["User Registration"]),
            list=extend_schema(tags=["User Management"]),
            retrieve=extend_schema(tags=["User Management"]),
            update=extend_schema(tags=["User Management"]),
            partial_update=extend_schema(tags=["User Management"]),
            destroy=extend_schema(tags=["User Management"]),
            activation=extend_schema(tags=["Account Activation"]),
            resend_activation=extend_schema(tags=["Account Activation"]),
            reset_password=extend_schema(tags=["Password Management"]),
            reset_password_confirm=extend_schema(tags=["Password Management"]),
            reset_username=extend_schema(tags=["Username Management"]),
            reset_username_confirm=extend_schema(tags=["Username Management"]),
            set_password=extend_schema(tags=["Password Management"]),
            set_username=extend_schema(tags=["Username Management"]),
        )
        class FixedViewSet(UserViewSet):
            pass

        return FixedViewSet
