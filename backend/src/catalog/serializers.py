
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    #Se agregan validadores de campo con validadores DRF
    #para garantizar que los datos sean enviados desde la API
    name = serializers.CharField(
        max_length=120,
        validators=[
                UniqueValidator(
                queryset=Product.objects.all(),
                lookup='iexact', #case-insensitive
                message="Ya existe un producto con ese nombre (insensible a mayúsculas)."
                )
        ]
    )

    class Meta:
        model = Product
        fields = ["id", "name", "price", "tags"]

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("El precio no puede ser negativo.")
        return value
    

