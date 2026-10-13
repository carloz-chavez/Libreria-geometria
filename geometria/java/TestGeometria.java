import java.util.List;
public class TestGeometria {
static void check(boolean c) { if(!c) throw new AssertionError("Fallo"); }
public static void main(String[] args) {
check(Math.abs(Geometria.areaPoligono(List.of(new Geometria.Punto(0,0),new Geometria.Punto(4,0),new Geometria.Punto(4,3),new Geometria.Punto(0,3)))-12)<1e-9);
check(Math.abs(Geometria.areaPoligono(List.of(new Geometria.Punto(0,3),new Geometria.Punto(4,3),new Geometria.Punto(4,0),new Geometria.Punto(0,0)))-12)<1e-9);
check(Math.abs(Geometria.areaPoligono(List.of(new Geometria.Punto(0,0),new Geometria.Punto(4,0),new Geometria.Punto(0,3)))-6)<1e-9);
check(Math.abs(Geometria.areaPoligono(List.of(new Geometria.Punto(0,0),new Geometria.Punto(4,0),new Geometria.Punto(4,4),new Geometria.Punto(2,2),new Geometria.Punto(0,4)))-12)<1e-9);
check(Math.abs(Geometria.areaPoligono(List.of(new Geometria.Punto(-3,-2),new Geometria.Punto(1,-2),new Geometria.Punto(1,1),new Geometria.Punto(-3,1)))-12)<1e-9);
check(Math.abs(Geometria.areaPoligono(List.of(new Geometria.Punto(0,0),new Geometria.Punto(1,1),new Geometria.Punto(2,2)))-0)<1e-9);
check(Math.abs(Geometria.areaPoligono(List.of(new Geometria.Punto(0,0),new Geometria.Punto(4,0),new Geometria.Punto(0,3),new Geometria.Punto(0,0)))-6)<1e-9);
check(Math.abs(Geometria.areaPoligono(List.of(new Geometria.Punto(0,0),new Geometria.Punto(0.5,0),new Geometria.Punto(0,0.5)))-0.125)<1e-9);

for (List<Geometria.Punto> p:List.of(List.<Geometria.Punto>of(), List.of(new Geometria.Punto(0,0),new Geometria.Punto(1,0)),
 List.of(new Geometria.Punto(0,0),new Geometria.Punto(1,0),new Geometria.Punto(Double.NaN,1)),
 List.of(new Geometria.Punto(0,0),new Geometria.Punto(1,0),new Geometria.Punto(Double.POSITIVE_INFINITY,1)),
 List.of(new Geometria.Punto(0,0),new Geometria.Punto(1e308,0),new Geometria.Punto(0,1e308)))) {
 boolean fallo=false; try { Geometria.areaPoligono(p); } catch (IllegalArgumentException|ArithmeticException e) { fallo=true; } check(fallo);
}
var p=List.of(new Geometria.Punto(0,0),new Geometria.Punto(4,0),new Geometria.Punto(0,3));
check(Geometria.areaFirmada(p)==-Geometria.areaFirmada(p.reversed()));
check(Geometria.areaPoligono(p.stream().map(q->new Geometria.Punto(q.x()+1e9,q.y()-1e9)).toList())==6);
check(Geometria.areaPoligono(p.stream().map(q->new Geometria.Punto(2*q.x(),2*q.y())).toList())==24);
System.out.println("Java: todas las pruebas pasan");
} }
