from django.urls import path
from . import views
from django.conf import settings
from .views import postListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PartidoListView, PartidoCreateView, PartidoDetailView
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home),

    path('signin', views.signIn),
    path('login', views.logIn),
    path('logout', views.salirSesion),

   

    path('torneos', views.torneos),
    

    path('perfil', views.perfil),
    path('ranking', views.ranking),

    path('torneo1', views.torneo1),
    path('cambiar_numero', views.cambiar_numero, name='cambiar_numero'),

   
   #INICIO
    path('inicio', postListView.as_view(), name='inicio'),
    path('post/nuevoPost', PostCreateView.as_view(), name='nuevo_post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detalle_post'),
    path('post/<int:pk>/editar', PostUpdateView.as_view(), name='editar_post'),
    path('post/<int:pk>/borrar', PostDeleteView.as_view(), name='borrar_post'),

    #PARTIDOS 
    path('partidos', views.partidos),
    path('partidos/crear-partido', PartidoCreateView.as_view(), name='nuevo_partido'),
    path('partidos/<int:pk>/', PartidoDetailView.as_view(), name='detalle_partido'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)