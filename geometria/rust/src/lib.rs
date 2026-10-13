#[derive(Clone, Copy, Debug)]
pub struct Punto { pub x: f64, pub y: f64 }
#[derive(Debug, PartialEq)]
pub enum ErrorArea { PocosPuntos, CoordenadaNoFinita, Desbordamiento }
pub fn area_firmada(p: &[Punto]) -> Result<f64, ErrorArea> {
    if p.len()<3 { return Err(ErrorArea::PocosPuntos); }
    if p.iter().any(|q| !q.x.is_finite() || !q.y.is_finite()) {
        return Err(ErrorArea::CoordenadaNoFinita);
    }
    let mut suma=0.0;
    for (i,a) in p.iter().enumerate() {
        let b=p[(i+1)%p.len()];
        suma+=(a.x-p[0].x)*(b.y-p[0].y)-(b.x-p[0].x)*(a.y-p[0].y);
    }
    let area=suma/2.0;
    if !area.is_finite() { return Err(ErrorArea::Desbordamiento); }
    Ok(area)
}
pub fn area_poligono(p: &[Punto]) -> Result<f64, ErrorArea> { area_firmada(p).map(f64::abs) }
