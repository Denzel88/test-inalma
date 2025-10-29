Prueba Técnica Semi-Senior - Solución

Este documento describe las decisiones técnicas tomadas para completar la prueba y las instrucciones para ejecutarla.1. Cómo Probar la SoluciónPara ejecutar la solución, sigue estos pasos desde la raíz del proyecto.Backend (Python/Django)

1. Navega a la carpeta backend:
   backend
   Activa el entorno virtual:Bash# Windows
   .venv\Scripts\activate

# macOS / Linux

source .venv/bin/activate
Ejecuta los tests de Python:
pytest -q

(Opcional) Ejecuta el servidor:
python manage.py runserver

Frontend (React)Navega a la carpeta frontend:
frontend
(Si es la primera vez) Instala las dependencias:Bashnpm install
Ejecuta los tests de React:
npm test
(Opcional) Ejecuta la aplicación de desarrollo:
npm run dev

2. Decisiones Técnicas y Trade-OffsA continuación se detallan las decisiones clave tomadas para cada módulo.Backend:

Algoritmos (src/algos/functions.py)is_palindrome: Se implementó una solución estándar, normalizando el string a minúsculas (.lower()) y eliminando espacios (.replace()) antes de comparar con su reverso ([::-1]).

compress_ranges: Se utilizó un enfoque de iteración única, manteniendo punteros de start y end para construir los rangos. Se prestó especial atención al caso de guardar el último rango pendiente después de que el bucle finalizara.

min_path_sum: Se identificó como un problema de Programación Dinámica (DP). La solución modifica la matriz in-place, acumulando los costos mínimos de camino. Esto es mucho más eficiente ($O(m*n)$) que una solución recursiva/backtracking ($O(2^{m+n})$).

top_k_frequent_words: Se usó la herramienta collections.Counter de Python para un conteo eficiente de frecuencias. La clave de la solución fue el método de ordenación (sorted), usando una tupla key=lambda w: (-counts[w], w) para manejar la doble condición: ordenar por frecuencia descendente (usando el negativo) y desempatar alfabéticamente.

Backend: API (src/catalog/)Validación de POST (Trade-off):
La lógica de validación de nombre único case-insensitive se movió desde la Vista (views.py) al Serializador (serializers.py), que es la capa correcta para la validación de datos. Se implementó usando el UniqueValidator de DRF con lookup='iexact', lo cual es más declarativo y limpio que un método validate_name manual.

Filtro de tags (Trade-off Clave): La decisión más importante. El intento inicial fue usar un filtro a nivel de BD (tags**contains=["tech", "pc"]) para máxima eficiencia.Problema: el proyecto no soporta consultas **contains complejas en campos JSONField.Solución (Trade-off): Se optó por una solución híbrida. El queryset se filtra primero en la BD por precio, búsqueda y orden. Luego, el filtrado de tags se realiza en Python (en memoria) antes de devolver los datos a la vista. Esto es menos eficiente que un filtro de BD, pero es la única solución compatible para pasar el test bajo las restricciones de la BD.

Eliminación de Warnings: Se añadió un order_by('id') al queryset base en get_queryset para establecer un orden por defecto. Esto elimina el UnorderedObjectListWarning de la paginación, asegurando resultados consistentes.

Frontend: UI (React)Arquitectura:
La arquitectura existente (Contenedor App.jsx + Componentes "tontos" ProductList y SearchBar) era limpia y se mantuvo.Debounce: La lógica de debounce ya estaba correctamente implementada en el SearchBar.jsx usando el hook useDebounce, que propaga el valor debunceado al App.jsx, disparando el useEffect de carga de datos eficientemente.

Resolución de Tests:
El test de frontend fallaba no por lógica de React, sino por una dependencia de desarrollo faltante. Se identificó y se añadió @testing-library/user-event al package.json para permitir que el entorno de test simulara eventos de usuario.
