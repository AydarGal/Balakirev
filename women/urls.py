from django.urls import path, re_path
from . import views
from women.views import page_not_found

urlpatterns = [
    path('', views.index, name='home'),

    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<int:cat_id>', views.show_category, name='category')
]


hanlder404 = page_not_found
