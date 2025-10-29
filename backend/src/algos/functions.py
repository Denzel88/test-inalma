
def is_palindrome(s: str) -> bool:
    """Devuelve True si s es palíndromo (ignorando espacios y mayúsculas)."""

    #Limpiar la cadena 
    clean_string = s.replace(" ", "").lower()
    
    #Esta seccion compararemos el reverso de la cadena
    return clean_string  == clean_string [::-1]


def compress_ranges(nums: list[int]) -> list[str]:
    """Comprime secuencias consecutivas:
    [1,2,3,5,7,8] -> ["1-3","5","7-8"]
    """
    #Si la lista se encuentra vacia devolvemos una lista vacia
    if not nums:
        return []
    
    ranges=[]       #Lista para guardar los resultados
    start=nums[0]   #Inicio de rango actual
    end = nums[0]   #Fin de rango actual
    
    #Iterar desde el segundo elemento en el indice 1
    for num in nums[1:]:
        if num == end + 1:
            #El rango continua y actualizamos el final
            end = num
        else:
            #Si el rango se rompe, guardamos el rango anterior
            if start == end:
                #Si start y end son iguales guardamos solo ese valor
                ranges.append(str(start))
            else:
                #Si son diferentes guardamos el rango (1-3)
                ranges.append(f"{start}-{end}")
            #Empezamos un nuevo rango    
            start = num
            end = num
    #Cuando el bucle finaliza, utilizamos el mismo if para guardarlo manualmente
    if start == end:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}-{end}")
    
    return ranges


def min_path_sum(grid: list[list[int]]) -> int:
    """Suma mínima de camino desde (0,0) a (n-1,m-1) moviéndose solo derecha/abajo."""
    raise NotImplementedError

def top_k_frequent_words(words: list[str], k: int) -> list[str]:
    """Top k palabras por frecuencia; empate por orden alfabético ascendente."""
    raise NotImplementedError
