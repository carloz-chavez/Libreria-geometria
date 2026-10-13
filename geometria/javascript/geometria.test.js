import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import {areaPoligono, areaFirmada} from './geometria.js';
const casos = JSON.parse(readFileSync(new URL('../tests/casos.json',import.meta.url)));
for (const c of casos) test(c.nombre,()=>assert.ok(Math.abs(areaPoligono(c.puntos.map(([x,y])=>({x,y})))-c.area)<1e-9));
test('invalidos',()=>{
  for(const p of [[],[{x:0,y:0}], [{x:0,y:0},{x:1,y:0},{x:NaN,y:1}],
    [{x:0,y:0},{x:1,y:0},{x:1,y:Infinity}], [{x:0,y:0},{x:1e308,y:0},{x:0,y:1e308}]])
    assert.throws(()=>areaPoligono(p));
});
test('propiedades',()=>{
 const p=[{x:0,y:0},{x:4,y:0},{x:0,y:3}];
 assert.equal(areaFirmada(p),-areaFirmada([...p].reverse()));
 assert.equal(areaPoligono(p.map(q=>({x:q.x+1e9,y:q.y-1e9}))),6);
 assert.equal(areaPoligono(p.map(q=>({x:q.x*2,y:q.y*2}))),24);
});
