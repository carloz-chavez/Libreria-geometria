package geometria
import ("testing"; "math")
func TestCasos(t *testing.T) {
if a,e:=AreaPoligono([]Punto{{0,0},{4,0},{4,3},{0,3}}); e!=nil || math.Abs(a-12)>1e-9 { t.Fatal("rectangulo",a,e) }
if a,e:=AreaPoligono([]Punto{{0,3},{4,3},{4,0},{0,0}}); e!=nil || math.Abs(a-12)>1e-9 { t.Fatal("horario",a,e) }
if a,e:=AreaPoligono([]Punto{{0,0},{4,0},{0,3}}); e!=nil || math.Abs(a-6)>1e-9 { t.Fatal("triangulo",a,e) }
if a,e:=AreaPoligono([]Punto{{0,0},{4,0},{4,4},{2,2},{0,4}}); e!=nil || math.Abs(a-12)>1e-9 { t.Fatal("concavo",a,e) }
if a,e:=AreaPoligono([]Punto{{-3,-2},{1,-2},{1,1},{-3,1}}); e!=nil || math.Abs(a-12)>1e-9 { t.Fatal("negativos",a,e) }
if a,e:=AreaPoligono([]Punto{{0,0},{1,1},{2,2}}); e!=nil || math.Abs(a-0)>1e-9 { t.Fatal("colineal",a,e) }
if a,e:=AreaPoligono([]Punto{{0,0},{4,0},{0,3},{0,0}}); e!=nil || math.Abs(a-6)>1e-9 { t.Fatal("cierre",a,e) }
if a,e:=AreaPoligono([]Punto{{0,0},{0.5,0},{0,0.5}}); e!=nil || math.Abs(a-0.125)>1e-9 { t.Fatal("fraccion",a,e) }

}
func TestInvalidos(t *testing.T) {
 for _,p:=range [][]Punto{nil,{{0,0},{1,0}},{{0,0},{1,0},{math.NaN(),1}},{{0,0},{1,0},{math.Inf(1),1}},{{0,0},{1e308,0},{0,1e308}}} {
  if _,e:=AreaPoligono(p); e==nil { t.Fatal("se esperaba error") }
 }
}
func TestPropiedades(t *testing.T) {
 a,_:=AreaFirmada([]Punto{{0,0},{4,0},{0,3}}); b,_:=AreaFirmada([]Punto{{0,3},{4,0},{0,0}})
 if a != -b { t.Fatal("orientación") }
 a,e:=AreaPoligono([]Punto{{1e9,-1e9},{1e9+4,-1e9},{1e9,-1e9+3}}); if e!=nil||a!=6 { t.Fatal("traslación") }
 a,e=AreaPoligono([]Punto{{0,0},{8,0},{0,6}}); if e!=nil||a!=24 { t.Fatal("escala") }
}
