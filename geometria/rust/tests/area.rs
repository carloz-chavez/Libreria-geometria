use geometria::{Punto,area_poligono,area_firmada};
#[test]
fn casos() {
assert!((area_poligono(&[Punto{x:0.0,y:0.0},Punto{x:4.0,y:0.0},Punto{x:4.0,y:3.0},Punto{x:0.0,y:3.0}]).unwrap()-12.0).abs()<1e-9);
assert!((area_poligono(&[Punto{x:0.0,y:3.0},Punto{x:4.0,y:3.0},Punto{x:4.0,y:0.0},Punto{x:0.0,y:0.0}]).unwrap()-12.0).abs()<1e-9);
assert!((area_poligono(&[Punto{x:0.0,y:0.0},Punto{x:4.0,y:0.0},Punto{x:0.0,y:3.0}]).unwrap()-6.0).abs()<1e-9);
assert!((area_poligono(&[Punto{x:0.0,y:0.0},Punto{x:4.0,y:0.0},Punto{x:4.0,y:4.0},Punto{x:2.0,y:2.0},Punto{x:0.0,y:4.0}]).unwrap()-12.0).abs()<1e-9);
assert!((area_poligono(&[Punto{x:-3.0,y:-2.0},Punto{x:1.0,y:-2.0},Punto{x:1.0,y:1.0},Punto{x:-3.0,y:1.0}]).unwrap()-12.0).abs()<1e-9);
assert!((area_poligono(&[Punto{x:0.0,y:0.0},Punto{x:1.0,y:1.0},Punto{x:2.0,y:2.0}]).unwrap()-0.0).abs()<1e-9);
assert!((area_poligono(&[Punto{x:0.0,y:0.0},Punto{x:4.0,y:0.0},Punto{x:0.0,y:3.0},Punto{x:0.0,y:0.0}]).unwrap()-6.0).abs()<1e-9);
assert!((area_poligono(&[Punto{x:0.0,y:0.0},Punto{x:0.5,y:0.0},Punto{x:0.0,y:0.5}]).unwrap()-0.125).abs()<1e-9);

}
#[test]
fn invalidos() {
 for p in [vec![],vec![Punto{x:0.0,y:0.0};2],vec![Punto{x:0.0,y:0.0},Punto{x:1.0,y:0.0},Punto{x:f64::NAN,y:1.0}],
 vec![Punto{x:0.0,y:0.0},Punto{x:1.0,y:0.0},Punto{x:f64::INFINITY,y:1.0}],
 vec![Punto{x:0.0,y:0.0},Punto{x:1e308,y:0.0},Punto{x:0.0,y:1e308}]] {
  assert!(area_poligono(&p).is_err());
 }
}
#[test]
fn propiedades() {
 let p=[Punto{x:0.0,y:0.0},Punto{x:4.0,y:0.0},Punto{x:0.0,y:3.0}];
 let mut inverso=p; inverso.reverse();
 assert_eq!(area_firmada(&p).unwrap(),-area_firmada(&inverso).unwrap());
 assert_eq!(area_poligono(&p.map(|q| Punto{x:q.x+1e9,y:q.y-1e9})).unwrap(),6.0);
 assert_eq!(area_poligono(&p.map(|q| Punto{x:2.0*q.x,y:2.0*q.y})).unwrap(),24.0);
}
