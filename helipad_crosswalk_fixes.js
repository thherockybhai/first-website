// 1. Fixing the Crosswalk overlapping stripes at all intersections
// Replace original crosswalk calls with these:
crosswalk(-9, 0, 9, false); crosswalk(9, 0, 9, false);
crosswalk(0, 9, 9, true); crosswalk(0, -9, 9, true);

crosswalk(-9, -55, 9, false); crosswalk(9, -55, 9, false);
crosswalk(0, -46, 9, true);   crosswalk(0, -64, 9, true);

crosswalk(-9, 55, 9, false);  crosswalk(9, 55, 9, false);
crosswalk(0, 64, 9, true);    crosswalk(0, 46, 9, true);

// 2. Fixing the dashed lines going through the intersections
// Replace the two laneDash for-loops with these:
for(let i=-120;i<120;i+=6){ 
  if(Math.abs(i) > 6) laneDash(i,0); 
  if(Math.abs(i) > 6 && Math.abs(i+55) > 6 && Math.abs(i-55) > 6) {
      laneDash(0, i, Math.PI/2); 
  }
}
for(let i=-120;i<120;i+=6){ 
  if(Math.abs(i) > 6){ 
      laneDash(i, -55); 
      laneDash(i, 55); 
  } 
}

// 3. Fixing the Helipad 'H' layout on the rooftop
// Replace the original hBar1, hBar2, hCross declarations with these:
const hBar1 = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.08, 2.8),
  new THREE.MeshStandardMaterial({ color: 0xffcc00, emissive: 0xffcc00, emissiveIntensity: 1.0 }));
hBar1.position.set(-0.8, 0, 0); // Shifted left
heliGroup.add(hBar1);

const hBar2 = new THREE.Mesh(new THREE.BoxGeometry(0.3, 0.08, 2.8),
  new THREE.MeshStandardMaterial({ color: 0xffcc00, emissive: 0xffcc00, emissiveIntensity: 1.0 }));
hBar2.position.set(0.8, 0, 0); // Shifted right
heliGroup.add(hBar2);

const hCross = new THREE.Mesh(new THREE.BoxGeometry(1.6, 0.08, 0.3),
  new THREE.MeshStandardMaterial({ color: 0xffcc00, emissive: 0xffcc00, emissiveIntensity: 1.0 }));
hCross.position.set(0, 0, 0); // Cross bar connecting them
heliGroup.add(hCross);
