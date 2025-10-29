
from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Q
from .models import Product
from .serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = Product.objects.all().order_by('id')
        q = self.request.query_params.get("q")
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")
        tags = self.request.query_params.get("tags")
        ordering = self.request.query_params.get("ordering")

        if q:
            qs = qs.filter(Q(name__icontains=q))

        if min_price is not None:
            try:
                qs = qs.filter(price__gte=float(min_price))
            except ValueError:
                pass

        if max_price is not None:
            try:
                qs = qs.filter(price__lte=float(max_price))
            except ValueError:
                pass
        
        #Ordenamos los datos optenidos de la BD
        allowed_ordering_fields = {"price", "-price", "name", "-name"}
        if ordering in allowed_ordering_fields:
            qs = qs.order_by(ordering)
        #Si pidiera tags, filtramos la variable qs ordenada 
        #y filtrada en memoria
        if tags:
            #Prerar tags solicitados
            requested_tags = [t.strip().lower for t in tags.split(",") if t.strip()]

            #crear una nueva lista de los resultados obtenidos
            filtered_results = []
            
            #Iterar los resultados de la DB
            for product in qs:
                #Normalizacion de los tags del producto
                product_tags_lower = [str(t).lower() for t in (product.tags or [])]

                #comprueba si todos los tags solicitados estan en el prodicto
                has_all_tags= all(req_tag in product_tags_lower for req_tag in requested_tags)

                if has_all_tags:
                    filtered_results.append(product)
            #Devuelve la lista filtrada
            return filtered_results
    
        #si no filtro por tags, devuelve la peticion normal
        return qs



                


        


