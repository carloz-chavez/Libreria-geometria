<?php
declare(strict_types=1);
require __DIR__.'/geometria.php';
use Geometria\Punto;
use function Geometria\areaPoligono;
use function Geometria\areaFirmada;
function check(bool $c): void { if (!$c) throw new \RuntimeException('Fallo'); }
check(abs(areaPoligono([new Punto(0,0),new Punto(4,0),new Punto(4,3),new Punto(0,3)])-12)<1e-9);
check(abs(areaPoligono([new Punto(0,3),new Punto(4,3),new Punto(4,0),new Punto(0,0)])-12)<1e-9);
check(abs(areaPoligono([new Punto(0,0),new Punto(4,0),new Punto(0,3)])-6)<1e-9);
check(abs(areaPoligono([new Punto(0,0),new Punto(4,0),new Punto(4,4),new Punto(2,2),new Punto(0,4)])-12)<1e-9);
check(abs(areaPoligono([new Punto(-3,-2),new Punto(1,-2),new Punto(1,1),new Punto(-3,1)])-12)<1e-9);
check(abs(areaPoligono([new Punto(0,0),new Punto(1,1),new Punto(2,2)])-0)<1e-9);
check(abs(areaPoligono([new Punto(0,0),new Punto(4,0),new Punto(0,3),new Punto(0,0)])-6)<1e-9);
check(abs(areaPoligono([new Punto(0,0),new Punto(0.5,0),new Punto(0,0.5)])-0.125)<1e-9);

foreach ([[],[new Punto(0,0),new Punto(1,0)], [new Punto(0,0),new Punto(1,0),new Punto(NAN,1)],
 [new Punto(0,0),new Punto(1,0),new Punto(INF,1)], [new Punto(0,0),new Punto(1e308,0),new Punto(0,1e308)]] as $p) {
 $fallo=false; try { areaPoligono($p); } catch (\InvalidArgumentException|\OverflowException $e) { $fallo=true; } check($fallo);
}
$p=[new Punto(0,0),new Punto(4,0),new Punto(0,3)];
check(areaFirmada($p)===-areaFirmada(array_reverse($p)));
check(areaPoligono(array_map(fn($q)=>new Punto($q->x+1e9,$q->y-1e9),$p))===6.0);
check(areaPoligono(array_map(fn($q)=>new Punto(2*$q->x,2*$q->y),$p))===24.0);
echo "PHP: todas las pruebas pasan\n";
