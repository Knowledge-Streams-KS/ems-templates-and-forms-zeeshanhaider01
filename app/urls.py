from django.urls import path
from app import views

app_name="app"
urlpatterns=[
    path("createevent/",views.createvent, name="create_event"),
    path("updateevent/<id>/<name>/",views.updateevent),
    path("createevent/form/",views.createvent),
    path("createuser/",views.createuser),
    path("createuser/form/", views.createuser),
    path("events/",views.allevents),
    path("register/<int:id>/",views.register_in_event, name="register"),
    path("register/form/",views.register_in_event_form),


]