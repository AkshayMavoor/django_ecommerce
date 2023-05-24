import code
from itertools import product
from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import AddProductForm
from .forms import UpdateProductForm
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from.models import Product
from django.core.exceptions import PermissionDenied
from django.db.models import Sum 
from .models import UserModel,Cart
from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
# Create your views here.

@method_decorator(login_required,name='dispatch')
class E_product(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            cart = Cart.objects.filter(user_id_id=request.user.id).update(quantity=0,total_purchase=0,date_of_update=datetime.now())
            products = Product.objects.all()
            context = {'current_path':"Cart" , "products": products, 'user_id' :request.user.id}
            return render(request, 'e_products.html',context)
        else:
            raise PermissionDenied()
        
@method_decorator(login_required,name='dispatch')
class Checkout(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            price = Cart.objects.filter(user_id_id=request.user.id).aggregate(Sum('total_purchase'))
            print(price)
            context = {'price' : price['total_purchase__sum']}
            print(context)
            return render(request, 'check_out.html',context)
        else:
            raise PermissionDenied()
    def post(self, request, *args , **kwargs):
        if not request.user.is_superuser:
            price = Cart.objects.filter(user_id_id=request.user.id).aggregate(Sum('total_purchase'))
            print(price)
            context = {'price' : price['total_purchase__sum']}
            print(context)
            return render(request, 'check_out.html',context)
        else:
            raise PermissionDenied()

@method_decorator(login_required,name='dispatch')
class AddProduct(View):
    def get(self, request, *args, **kwargs):
        
        form = AddProductForm
        if not request.user.is_superuser:
            raise PermissionDenied()
        else :
            context = {'form': form}
            return render(request, 'addProducts.html',context)
    def post(self, request, *args, **kwargs):
        form = AddProductForm
        if request.method == 'POST':
            form = AddProductForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Product added successfully")
                return redirect('addProducts')
            else:
                messages.error(request,"error")
        return redirect(request, 'addProducts')
@method_decorator(login_required,name='dispatch')

class UpdateProductView(View): 
    # template_name = 'updateProducts.html'
    def get(self, request,id, *args, **kwargs):
        if request.user.is_superuser:
            productData = Product.objects.get(id=id)
            data = {"stock": productData.stock,
                    "price" : productData.price,
                    "imageUrl" : productData.imageUrl,
                    "description" : productData.description,
                    "name" : productData.name,                
                    "id": productData.id,}
            context ={}
            form    = UpdateProductForm(data)
            context['form'] = form
            return render(request, 'updateProducts.html', context)
        else:
            raise PermissionDenied()
       
    
    def post(self, request, *args, **kwargs):
        id = request.POST['id']
        if request.method == 'POST':       

            updatedRecord = Product.objects.get(id=id)

            updatedRecord. product_name = request.POST['name']
            updatedRecord. price = request.POST['price']
            updatedRecord. image = request.POST['imageUrl']
            updatedRecord. stock = request.POST['stock']
            updatedRecord. description = request.POST['description']
            updatedRecord.save()
            messages.success(request,"Product updated successfully")
            return redirect('ProductTable')
        else:
            messages.success(request,"Product updated failed")
            form = UpdateProductForm()
        return redirect(request, 'updateProducts')
    
@method_decorator(login_required,name='dispatch')
class ProductTable(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_superuser:
            tables = Product.objects.all().order_by('id')
            context = {'current_path':"Manage Shop",'tables': tables}
            return render(request, 'productTable.html', context)
        else:
            raise PermissionDenied()
@method_decorator(login_required,name='dispatch')
class DeleteProductView(View):
    def get (self, request, id):
        if request.user.is_superuser:
            product = Product.objects.get(id=id)
            product.delete()
            messages.success(request,"Product Deleted")
            return HttpResponseRedirect(reverse('ProductTable'))
        else:
            raise PermissionDenied()


from django.http import HttpResponseRedirect, JsonResponse


def cart_update(request, *args, **kwargs):
    print(request.POST)
    product_id = request.POST['p_id'][8:]
    qauntity = request.POST['qauntity']
    userid = request.POST['userid']
    product = Product.objects.filter(id=product_id).first()
    cart = Cart.objects.filter(user_id_id=userid,product_id=product_id)
    if cart:
        total = float(qauntity)*float(product.price)
        cart.update(quantity=qauntity,unit_price=product.price,date_of_update = datetime.now(),total_purchase=total)
    else:
        total = float(qauntity)*float(product.price)
        print(total,qauntity,product.price)
        Cart.objects.create(user_id_id=userid,product_id=product_id,quantity=qauntity,unit_price=product.price,date_of_update = datetime.now(),total_purchase=total)
    return_data={}
    return_data['updated'] = True

    return JsonResponse(return_data)

