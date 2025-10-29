Herramientas usadas

Asistente de IA (Gemini): Utilizado como herramienta de consulta y apoyo para depuración.

Prompts o consultas clave (resumen)

Consultas generales sobre sintaxis de Python para algoritmos.

Solicitudes de depuración para errores específicos de pytest (ej. AttributeError, NotSupportedError).

Preguntas sobre buenas prácticas en Django REST Framework (ej. manejo de validaciones).

Consulta sobre cómo resolver un UnorderedObjectListWarning en la paginación de Django.

Diagnóstico de un error de importación en los tests de Vitest (Failed to resolve import).

Qué generó la herramienta y cómo lo adapté
Utilicé el asistente de IA principalmente como un recurso de apoyo para el backend, donde solicité aclaraciones sobre sintaxis y librerías específicas de Python y Django.

Módulo de Algoritmos (algos/functions.py)

La IA proveyó orientación sobre la lógica de algoritmos complejos como min_path_sum (Programación Dinámica) y top_k_frequent_words (métodos de ordenación), lo cual me ayudó a estructurar mi solución final.

Módulo de API (catalog/)

El asistente fue clave para depurar errores específicos. Por ejemplo, me ayudó a diagnosticar por qué fallaba el filtro \_\_contains en JSONField (una limitación de SQLite) y a encontrar la solución alternativa (filtrado en memoria).

Consulté sobre la forma correcta de implementar la validación case-insensitive en DRF, lo que me llevó a usar UniqueValidator en el serializador en lugar de la vista.

La IA me ayudó a identificar typos sutiles en el código (ej. CharField vs Charfield, order_by vs orderby) que estaban causando fallos inesperados en los tests.

Me orientó sobre cómo resolver el warning de paginación de Django (UnorderedObjectListWarning) añadiendo un orden por defecto al queryset.

Documentación

La IA me ayudó a generar un documento mas profecional y en menos tiempo del README_personal.md.

Entendido. Quieres que el documento refleje un rol de apoyo y consulta, no de coautor. Es una excelente idea para presentar tu trabajo.

Aquí tienes una versión revisada del AI_USAGE.md que es más general y se enfoca en mi rol como un asistente de depuración y consulta de sintaxis/librerías.

(Copia y pega este contenido en tu AI_USAGE.md)

AI_USAGE.md
Herramientas usadas
Asistente de IA (Gemini): Utilizado como herramienta de consulta y apoyo para depuración.

Prompts o consultas clave (resumen)
Consultas generales sobre sintaxis de Python para algoritmos.

Solicitudes de depuración para errores específicos de pytest (ej. AttributeError, NotSupportedError).

Preguntas sobre buenas prácticas en Django REST Framework (ej. manejo de validaciones).

Consulta sobre cómo resolver un UnorderedObjectListWarning en la paginación de Django.

Diagnóstico de un error de importación en los tests de Vitest (Failed to resolve import).

Qué generó la herramienta y cómo lo adapté
Utilicé el asistente de IA principalmente como un recurso de apoyo para el backend, donde solicité aclaraciones sobre sintaxis y librerías específicas de Python y Django.

Módulo de Algoritmos (algos/functions.py)

La IA proveyó orientación sobre la lógica de algoritmos complejos como min_path_sum (Programación Dinámica) y top_k_frequent_words (métodos de ordenación), lo cual me ayudó a estructurar mi solución final.

Módulo de API (catalog/)

El asistente fue clave para depurar errores específicos. Por ejemplo, me ayudó a diagnosticar por qué fallaba el filtro \_\_contains en JSONField (una limitación de SQLite) y a encontrar la solución alternativa (filtrado en memoria).

Consulté sobre la forma correcta de implementar la validación case-insensitive en DRF, lo que me llevó a usar UniqueValidator en el serializador en lugar de la vista.

La IA me ayudó a identificar typos sutiles en el código (ej. CharField vs Charfield, order_by vs orderby) que estaban causando fallos inesperados en los tests.

Me orientó sobre cómo resolver el warning de paginación de Django (UnorderedObjectListWarning) añadiendo un orden por defecto al queryset.

Frontend (React)

En el frontend, donde tengo más experiencia, solo usé la IA para diagnosticar un error de entorno en los tests (Failed to resolve import), identificando una dependencia de desarrollo faltante.

Documentación

La IA me ayudó a generar la estructura base para el README_personal.md.

Notas de ética/seguridad

La asistencia se centró en la depuración, la consulta de sintaxis y la comprensión de buenas prácticas.

Todo el código fue revisado, implementado y entendido por mí antes de ser enviado.

No se subió ningún tipo de secreto o credencial.
