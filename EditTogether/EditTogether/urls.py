from django.contrib import admin
from django.urls import include, path
from editor.views import editor_view
from django.http import HttpResponseRedirect
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('api/editor/', include('editor.urls')),
    path('editor/', editor_view, name='editor'),

    path('', lambda request: HttpResponseRedirect('api/auth/login/')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
