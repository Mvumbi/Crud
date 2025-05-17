from django.contrib import admin
from django.urls import path
from bibliotheque import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', views.BookCreate.as_view(), name='create'),
    path('', views.BookList.as_view(), name='read'),
    path('<int:pk>/edit', views.BookUpdate.as_view(), name='update'),
    path('<int:pk>/delete', views.BookDelete.as_view(), name='delete'),
    path('<int:pk>/detail', views.BookDetail.as_view(), name='detail'),
]

urlpatterns += staticfiles_urlpatterns()
