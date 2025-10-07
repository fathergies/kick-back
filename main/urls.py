from django.urls import path
from main.views import show_main, create_product, show_product
from main.views import show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register, login_user, logout_user
from main.views import edit_product, delete_product, show_category, edit_product_ajax, get_product_json

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product/', create_product, name='create_product'),
    
    # ========== PENTING: Taruh URL spesifik SEBELUM yang generic ==========
    path('product/<int:id>/json/', get_product_json, name='get_product_json'),
    path('product/<int:id>/edit/', edit_product, name='edit_product'),
    path('product/<int:id>/edit-ajax/', edit_product_ajax, name='edit_product_ajax'),
    path('product/<int:id>/delete/', delete_product, name='delete_product'),
    
    # URL generic taruh di bawah (biar gak rebutan sama yang spesifik)
    path('product/<int:id>/', show_product, name='show_product'),  # UBAH dari <str:id> jadi <int:id>
    
    # XML/JSON routes
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    
    # Auth routes
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    
    # Category
    path('category/<str:category>/', show_category, name='show_category'),
]