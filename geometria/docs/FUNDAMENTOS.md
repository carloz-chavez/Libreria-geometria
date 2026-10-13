# Fundamento del algoritmo

Sean P₀,…,Pₙ₋₁ los vértices ordenados de un polígono simple y Pₙ=P₀. Definimos el determinante 2D `det(a,b)=a.x*b.y-b.x*a.y`.

El área firmada es:

```text
S = 1/2 · Σ(i=0…n−1) [xᵢ yᵢ₊₁ − xᵢ₊₁ yᵢ]
A = |S|
```

## Demostración por integral sobre el contorno

El teorema de Green da el área firmada como `1/2 ∮ (x dy − y dx)`. En el segmento de P a Q parametrizamos `r(t)=P+t(Q−P)`, con `0≤t≤1`. Al sustituir, los términos en t se cancelan y la integral del segmento es `P.x*Q.y−Q.x*P.y`. La suma de los segmentos produce la expresión anterior. El signo corresponde a la orientación; el valor absoluto da el área geométrica para un contorno simple. La forma clásica de Green supone una región no degenerada; para puntos colineales la fórmula algebraica produce cero directamente.

## Traslación y estrategia alternativa

Para cualquier origen O:

```text
det(Pᵢ−O,Pᵢ₊₁−O)
 = det(Pᵢ,Pᵢ₊₁) − det(Pᵢ,O) − det(O,Pᵢ₊₁)
```

Los términos adicionales se cancelan al sumar un ciclo, porque la lista de primeros y segundos extremos es la misma. Por eso se puede elegir O=P₀. Los segmentos que tocan P₀ aportan cero y queda la suma de `n−2` triángulos firmados `(P₀,Pᵢ,Pᵢ₊₁)`. Esta identidad justifica la estrategia `Abanico` de la demostración SOLID.

En un polígono cóncavo algunos triángulos pueden tener signo negativo. Se suman los determinantes **antes** de aplicar valor absoluto; sumar las áreas absolutas de cada triángulo podría contar regiones de más. El abanico algebraico no exige que esas piezas sean una partición interior sin solapamiento.

## Ejemplo y pseudocódigo

Para `(0,0),(4,0),(4,3),(0,3)` los productos cruzados son `0,12,12,0`. La suma es 24; el área es 12. Invertir el orden cambia la suma a −24 y conserva el área absoluta.

```text
AreaPoligono(puntos):
    validar al menos 3 coordenadas finitas
    origen ← puntos[0]
    suma ← 0
    para i desde 0 hasta n−1:
        p ← puntos[i] − origen
        q ← puntos[(i+1) mod n] − origen
        suma ← suma + p.x*q.y − q.x*p.y
    area ← suma / 2
    si area no es finita: devolver error
    devolver abs(area)
```

La validación y el cálculo recorren la entrada un número constante de veces: O(n) tiempo. Solo se mantienen índices y acumuladores: O(1) memoria auxiliar. El área depende del orden del contorno; ordenar por coordenada x o por ángulo no es una corrección general de una entrada arbitraria.
