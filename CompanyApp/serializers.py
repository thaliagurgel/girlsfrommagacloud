from rest_framework import serializers
from CompanyApp.models import Products, Companies

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('ProductId',
                  'ProductName',
                  'ProducDescription',
                  'ProductPrice',
                  'PhotoFileName'
                  )

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Companies
        fields = (' CompanyID',
                  'CompanyName',
                  'CompanyCNPJ',
                  'CompanyDepartment',
                  'CompanyAdress',
                  'PhotoFileName')

