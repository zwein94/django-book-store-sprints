from django.urls import path
from books import views as books_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', books_views.index.as_view(), name='home'),
    path('api/books/', books_views.book_list),
    path('api/books/<int:pk>/', books_views.book_detail),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
