from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse, HttpResponse
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.db.models import Exists

from .models import *

# Create your views here.


def index(request):
	return render(request, 'AppLine/index.html')

@csrf_exempt	
def query1(request):
	warehouse_name = request.GET.get('warehouse_name', '')
	print(warehouse_name)
	results = Warehouse.objects.filter(w_name__regex=r'%s' %(warehouse_name))
	
	results = [(r.w_id,r.w_name) for r in results]

	return JsonResponse({"msg1": results})
	
def query2(request):
	item_name = request.GET.get('item_name', '')
	
	results = Item.objects.filter(i_name__regex=r'%s' %(item_name))
	
	results = [(r.i_id,r.i_name) for r in results]
	
	return JsonResponse({"msg2": results})
	
	
def search(request):
	warehouse_number = request.GET.get('warehouse_number', '')
	item_id = request.GET.get('item_id', '')
	quantity = request.GET.get('quantity', '')
	order_deliv = request.GET.get('order_delivery', '')
	
	if Stock.objects.filter(w=warehouse_number).filter(i=item_id).exists():
		temp = Stock.objects.get(w=warehouse_number, i=item_id)
		if order_deliv == 'Order' and temp.s_qty >= int(quantity):
			Stock.objects.filter(w = warehouse_number).filter(i = item_id).update(s_qty = F('s_qty') - int(quantity))
			return JsonResponse({"msg": f"Your Line Order has been successfully processed"})
			
		elif order_deliv == 'Order' and temp.s_qty < int(quantity):
			return JsonResponse({"msg": f"Insufficient Stock"})
			
		elif order_deliv == 'Delivery':
			Stock.objects.filter(w = warehouse_number).filter(i = item_id).update(s_qty = F('s_qty') + int(quantity))
			return JsonResponse({"msg": f"Your Delivery has been successfully processed"})
	else:
		if order_deliv == 'Order':
			return JsonResponse({"msg": f"Insufficient Stock"})
		elif order_deliv == 'Delivery':
			temp2 = Warehouse.objects.get(w_id = warehouse_number)
			temp3 = Item.objects.get(i_id = item_id)
			new = Stock(w = temp2, i = temp3, s_qty = quantity)
			new.save(Stock.s_qty)
			return JsonResponse({"msg": f"Your Delivery has been successfully processed"})