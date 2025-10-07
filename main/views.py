from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST # Ini sebenarnya tidak digunakan di kode Anda, bisa dihapus jika tidak dipakai
import json


# Create your views here.
def show_main(request):
    filter_type = request.GET.get("filter", "all")
    category = request.GET.get("category", None)

    if category:
        product_list = Product.objects.filter(category=category)
    elif filter_type == "all":
        product_list = Product.objects.all()
    elif request.user.is_authenticated: # Hanya tampilkan produk user jika sudah login
        product_list = Product.objects.filter(user=request.user)
    else: # Jika filter 'my' tapi belum login, atau filter lain yang tidak dikenal, tampilkan semua
        product_list = Product.objects.all()

    context = {
        'name': request.user.username if request.user.is_authenticated else 'Guest', # Mengamankan jika user belum login
        'class': 'PBP F',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'selected_category': category,
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def show_category(request, category):
    # filter produk sesuai kategori
    product_list = Product.objects.filter(category=category)

    context = {
        'name': request.user.username,
        'class': 'PBP F',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
        'selected_category': category,  # buat highlight di navbar
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    if request.method == "POST":
        # Check if AJAX request (JSON)
        if request.headers.get('Content-Type') == 'application/json':
            try:
                data = json.loads(request.body)
                
                # Validasi sederhana untuk data yang diperlukan
                required_fields = ['name', 'price', 'category']
                if not all(field in data for field in required_fields):
                    return JsonResponse({'error': 'Missing required fields'}, status=400)

                product = Product.objects.create(
                    user=request.user,
                    name=data.get('name'),
                    specification=data.get('specification', ''),
                    price=data.get('price'),
                    description=data.get('description', ''),
                    thumbnail=data.get('thumbnail', ''),  # String URL
                    category=data.get('category'),
                    is_featured=data.get('is_featured', False)
                )
                
                # FIX: Safe thumbnail handling for response
                if hasattr(product.thumbnail, 'url'):
                    thumbnail_value = product.thumbnail.url if product.thumbnail else None
                else:
                    thumbnail_value = product.thumbnail if product.thumbnail else None
                
                return JsonResponse({
                    'id': product.id,
                    'name': product.name,
                    'specification': product.specification,
                    'price': str(product.price),
                    'description': product.description,
                    'thumbnail': thumbnail_value,
                    'category': product.category,
                    'is_featured': product.is_featured,
                    'user_id': product.user_id,
                }, status=201)
            except json.JSONDecodeError:
                return JsonResponse({'error': 'Invalid JSON'}, status=400)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=400)
        
        # Regular form submission
        form = ProductForm(request.POST)
        if form.is_valid():
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()
            messages.success(request, "Product created successfully!")
            return redirect('main:show_main')
        else:
            messages.error(request, "Failed to create product. Please check the form.")
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    filter_type = request.GET.get("filter", "all")
    category = request.GET.get("category", None)

    if category:
        product_list = Product.objects.filter(category=category)
    elif filter_type == "all":
        product_list = Product.objects.all()
    elif request.user.is_authenticated and filter_type == "my":
        product_list = Product.objects.filter(user=request.user)
    else:
        product_list = Product.objects.all()

    data = []
    for product in product_list:
        # FIX: Check if thumbnail is ImageField or CharField
        if hasattr(product.thumbnail, 'url'):
            # It's an ImageField
            thumbnail_value = product.thumbnail.url if product.thumbnail else None
        else:
            # It's a CharField (string URL)
            thumbnail_value = product.thumbnail if product.thumbnail else None
        
        data.append({
            'id': product.id,
            'name': product.name,
            'specification': product.specification,
            'price': str(product.price),  # Convert to string to avoid decimal issues
            'description': product.description,
            'thumbnail': thumbnail_value,  # Use the safe value
            'category': product.category,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        })
    
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related("user").get(pk=product_id)
        
        # FIX: Safe thumbnail handling
        if hasattr(product.thumbnail, 'url'):
            thumbnail_value = product.thumbnail.url if product.thumbnail else None
        else:
            thumbnail_value = product.thumbnail if product.thumbnail else None
        
        data = {
            "id": str(product.id),
            "name": product.name,
            "specification": product.specification,
            "price": str(product.price),
            "description": product.description,
            "thumbnail": thumbnail_value,
            "category": product.category,
            "is_featured": product.is_featured,
            "user": {
                "id": product.user_id,
                "username": product.user.username if product.user_id else None,
            },
        }
        return JsonResponse({"product": data})
    except Product.DoesNotExist:
        return JsonResponse({"detail": "Not found"}, status=404)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            if is_ajax:
                return JsonResponse({
                    'success': True,
                    'message': 'Your account has been successfully created!',
                    'redirect_url': reverse('main:login')
                })
            else:
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        else:
            if is_ajax:
                errors = {}
                for field, error_list in form.errors.items():
                    errors[field] = [str(error) for error in error_list]
                
                return JsonResponse({
                    'success': False,
                    'errors': errors
                })
            else:
                # Menambahkan pesan error untuk non-AJAX
                for field, error_list in form.errors.items():
                    for error in error_list:
                        messages.error(request, f"{field.capitalize()}: {error}")
    
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            if is_ajax:
                response_data = {
                    'success': True,
                    'message': 'Login successful!',
                    'redirect_url': reverse('main:show_main')
                }
                response = JsonResponse(response_data)
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
        else:
            if is_ajax:
                errors = {}
                for field, error_list in form.errors.items():
                    errors[field] = [str(error) for error in error_list]
                
                return JsonResponse({
                    'success': False,
                    'errors': errors,
                    'message': 'Invalid username or password.'
                })
            else:
                messages.error(request, "Invalid username or password.") # Menambahkan pesan error untuk non-AJAX
    else:
        form = AuthenticationForm(request)
    
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    messages.info(request, "You have been logged out.") # Tambahkan pesan info
    return response

@login_required(login_url='/login')
def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    
    # Check if AJAX request
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Tambahkan pengecekan kepemilikan
        if product.user != request.user:
            return JsonResponse({'success': False, 'message': 'You are not authorized to delete this product'}, status=403)
        product.delete()
        return JsonResponse({'success': True, 'message': 'Product deleted successfully'})
    
    # Regular request
    if product.user != request.user:
        messages.error(request, "You are not authorized to delete this product.")
        return HttpResponseRedirect(reverse('main:show_main'))
    product.delete()
    messages.success(request, "Product deleted successfully!")
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    
    # Pengecekan kepemilikan
    if product.user != request.user:
        messages.error(request, "You are not authorized to edit this product.")
        return redirect('main:show_main')

    form = ProductForm(request.POST or None, instance=product)
    
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Product updated successfully!")
        return redirect('main:show_main')

    context = {
        'form': form,
        'product': product,   # ✅ Tambahkan ini biar template kamu nggak error
        'product_id': id,
    }

    return render(request, "edit_product.html", context)


# Fungsi ini tidak lengkap dan tidak memiliki return statement.
# Jika tidak digunakan, sebaiknya dihapus. Jika digunakan, perlu dilengkapi.
# Saya akan meninggalkannya seperti adanya, tapi ini adalah potensi masalah jika dipanggil.
def product_navbar(request,id):
    product = Product.objects.all()

@login_required(login_url='/login')
def get_product_json(request, id):
    try:
        product = Product.objects.get(pk=id, user=request.user)
        
        # Handle thumbnail safely
        if hasattr(product.thumbnail, 'url'):
            thumbnail_value = product.thumbnail.url if product.thumbnail else ''
        else:
            thumbnail_value = product.thumbnail if product.thumbnail else ''
        
        data = {
            'id': str(product.id),
            'name': product.name,
            'specification': product.specification,
            'price': str(product.price),
            'description': product.description or '',
            'thumbnail': thumbnail_value,
            'category': product.category,
            'is_featured': product.is_featured,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


# ========== EDIT PRODUCT AJAX ==========
@login_required(login_url='/login')
@csrf_exempt
def edit_product_ajax(request, id):
    if request.method != 'POST':
        return JsonResponse({'error': 'Method not allowed'}, status=405)
    
    try:
        product = Product.objects.get(pk=id, user=request.user)
        data = json.loads(request.body)
        
        product.name = data.get('name')
        product.specification = data.get('specification')
        product.price = data.get('price')
        product.description = data.get('description', '')
        product.thumbnail = data.get('thumbnail', '')
        product.category = data.get('category')
        product.is_featured = data.get('is_featured', False)
        
        product.save()
        
        return JsonResponse({
            'status': 'success', 
            'message': 'Product updated successfully'
        })
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)