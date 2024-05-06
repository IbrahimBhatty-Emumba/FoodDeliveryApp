from django.urls import path
from .views import (
    UserApiView,
    LoginApiView,
    RolesApiView,
    PermissionsApiView
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('permissions/', PermissionsApiView.as_view(), name="get_all_permissions"),
    path('permissions/', PermissionsApiView.as_view(), name="create_permission"),
    path('permissions/<int:id>/', PermissionsApiView.as_view(), name="get_role_permissions"),
    path('permissions/', PermissionsApiView.as_view(), name="get_all_permissions"),
    path('roles/', RolesApiView.as_view(), name="create_role"),
    path('roles/', RolesApiView.as_view(), name="get_all_roles"), 
    path('<int:id>/', UserApiView.as_view(), name="delete_user"),
    path('', UserApiView.as_view(), name="update_user"),
    path('login/', LoginApiView.as_view(), name="login_user"),
    path('register/', UserApiView.as_view(), name="register_user"),
    path('<int:id>/', UserApiView.as_view(), name="get_user_by_id"),
    path('', UserApiView.as_view(), name="get_user"),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
