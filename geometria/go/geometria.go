package geometria
import ("errors"; "math")
type Punto struct { X, Y float64 }
func AreaFirmada(p []Punto) (float64, error) {
    if len(p)<3 { return 0, errors.New("se requieren tres puntos") }
    for _,q:=range p { if math.IsNaN(q.X)||math.IsNaN(q.Y)||math.IsInf(q.X,0)||math.IsInf(q.Y,0) {
        return 0, errors.New("coordenadas no finitas")
    } }
    suma:=0.0
    for i,a:=range p {
        b:=p[(i+1)%len(p)]
        suma+=(a.X-p[0].X)*(b.Y-p[0].Y)-(b.X-p[0].X)*(a.Y-p[0].Y)
    }
    area:=suma/2
    if math.IsInf(area,0)||math.IsNaN(area) { return 0,errors.New("desbordamiento numérico") }
    return area,nil
}
func AreaPoligono(p []Punto) (float64,error) {
    a,err:=AreaFirmada(p)
    if err!=nil { return 0,err }; return math.Abs(a),nil
}
