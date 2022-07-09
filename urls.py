from django.urls import include, path


urlpatterns = [
    path(r'myapp/', include('myapp.urls'))
]
