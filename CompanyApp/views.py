from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from CompanyApp.models import Products, Companies
from CompanyApp.serializers import ProductsSerializer,CompanySerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def productApi(request,id=0):
    if request.method=='GET':
        product = Products.objects.all()
        products_serializer = ProductsSerializer(product, many=True)
        return JsonResponse(products_serializer.data, safe=False)

    elif request.method=='POST':
        product_data=JSONParser().parse(request)
        products_serializer = ProductsSerializer(data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
    
    elif request.method=='PUT':
        product_data = JSONParser().parse(request)
        product=Products.objects.get(ProductId=product_data['ProductId'])
        products_serializer=ProductsSerializer(product,data=product_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to Update.", safe=False)

    elif request.method=='DELETE':
        product=Products.objects.get(ProductId=id)
        product.delete()
        return JsonResponse("Deletado Com Sucesso!!", safe=False)

@csrf_exempt
def companyApi(request,id=0):
    if request.method=='GET':
        companies = Companies.objects.all()
        companies_serializer = CompanySerializer(companies, many=True)
        return JsonResponse(companies_serializer.data, safe=False)

    elif request.method=='POST':
        company_data=JSONParser().parse(request)
        company_serializer = CompanySerializer(data=company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse("Adicionado Com Sucesso!!" , safe=False)
        return JsonResponse("Falha ao adicionar.",safe=False)
    
    elif request.method=='PUT':
        company_data = JSONParser().parse(request)
        company=Companies.objects.get(CompanyId=company_data['CompanyId'])
        company_serializer=CompanySerializer(company,data=company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse("Atualizado com sucesso!!", safe=False)
        return JsonResponse("Falha ao atualizar.", safe=False)

    elif request.method=='DELETE':
        company=Companies.objects.get(CompanyId=id)
        company.delete()
        return JsonResponse("Deletado com sucesso!!", safe=False)


@csrf_exempt
def SaveFile(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name,file)

    return JsonResponse(file_name,safe=False)