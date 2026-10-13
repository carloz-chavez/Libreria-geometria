export function areaFirmada(puntos) {
  if (!Array.isArray(puntos) || puntos.length < 3) throw new RangeError('Se requieren tres puntos');
  if (puntos.some(p => !p || !Number.isFinite(p.x) || !Number.isFinite(p.y)))
    throw new TypeError('Coordenadas finitas requeridas');
  const o = puntos[0];
  let suma = 0;
  for (let i = 0; i < puntos.length; i++) {
    const p = puntos[i], q = puntos[(i+1)%puntos.length];
    suma += (p.x-o.x)*(q.y-o.y)-(q.x-o.x)*(p.y-o.y);
  }
  const area = suma/2;
  if (!Number.isFinite(area)) throw new RangeError('Desbordamiento numérico');
  return area;
}
export const areaPoligono = puntos => Math.abs(areaFirmada(puntos));
