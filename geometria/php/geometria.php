<?php
declare(strict_types=1);
namespace Geometria;
final class Punto {
    public function __construct(public float $x, public float $y) {}
}
/** @param list<Punto> $puntos */
function areaFirmada(array $puntos): float {
    if (count($puntos)<3 || !array_is_list($puntos)) throw new \InvalidArgumentException('Se requiere una lista de tres puntos');
    foreach ($puntos as $p) if (!$p instanceof Punto || !is_finite($p->x) || !is_finite($p->y))
        throw new \InvalidArgumentException('Coordenadas no finitas');
    $o=$puntos[0]; $suma=0.0; $n=count($puntos);
    for ($i=0; $i<$n; $i++) {
        $p=$puntos[$i]; $q=$puntos[($i+1)%$n];
        $suma+=($p->x-$o->x)*($q->y-$o->y)-($q->x-$o->x)*($p->y-$o->y);
    }
    $area=$suma/2;
    if (!is_finite($area)) throw new \OverflowException('Desbordamiento numérico');
    return $area;
}
function areaPoligono(array $puntos): float { return abs(areaFirmada($puntos)); }
