import java.util.List;
public final class Geometria {
    private Geometria() {}
    public record Punto(double x, double y) {}
    public static double areaFirmada(List<Punto> puntos) {
        if (puntos == null || puntos.size()<3) throw new IllegalArgumentException("Se requieren tres puntos");
        for (Punto p:puntos) if (p==null || !Double.isFinite(p.x()) || !Double.isFinite(p.y()))
            throw new IllegalArgumentException("Coordenadas no finitas");
        Punto o=puntos.get(0);
        double suma=0;
        for (int i=0;i<puntos.size();i++) {
            Punto p=puntos.get(i), q=puntos.get((i+1)%puntos.size());
            suma+=(p.x()-o.x())*(q.y()-o.y())-(q.x()-o.x())*(p.y()-o.y());
        }
        double area=suma/2;
        if (!Double.isFinite(area)) throw new ArithmeticException("Desbordamiento numérico");
        return area;
    }
    public static double areaPoligono(List<Punto> puntos) { return Math.abs(areaFirmada(puntos)); }
}
