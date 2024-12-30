
from django.http import JsonResponse,HttpResponse
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view


from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializers
@api_view(["GET","POST"])
def api_home(request, *args, **kwargs):
    print(request.method)
    if(request.method == "POST"):
        return Response({"message":"Not found"},status=404)
    model_data = Product.objects.all().order_by("?").first()
    if model_data:
        # product_data = model_to_dict(model_data, fields=["title","id","price","sale_price"])
        product_data = ProductSerializers(model_data).data
        print(product_data)
        return Response(product_data)
    else:
        return JsonResponse({"error": "No product found."}, status=404)

