// import * as THREE from "three"

// let camera, scene, renderer;
// let mesh;

// init();
// animate();

// function init() {
//   camera = new THREE.PerspectiveCamera(
//     70,
//     window.innerWidth / window.innerHeight,
//     1,
//     1000
//   );
//   camera.position.z = 400;

//   scene = new THREE.Scene();

//   const geometry = new THREE.BoxGeometry(200, 200, 200);
//   const material = new THREE.MeshBasicMaterial({ color: "red" });

//   mesh = new THREE.Mesh(geometry, material);
//   scene.add(mesh);

//   renderer = new THREE.WebGLRenderer({ antialias: true });
//   renderer.setPixelRatio(window.devicePixelRatio);
//   renderer.setSize(window.innerWidth, window.innerHeight);
//   document.body.appendChild(renderer.domElement);

//   window.addEventListener("resize", onWindowResize);
// }

// function onWindowResize() {
//   camera.aspect = window.innerWidth / window.innerHeight;
//   camera.updateProjectionMatrix();

//   renderer.setSize(window.innerWidth, window.innerHeight);
// }

// function animate() {
//   requestAnimationFrame(animate);

//   mesh.rotation.x += 0.005;
//   mesh.rotation.y += 0.01;

//   renderer.render(scene, camera);
// }

import * as THREE from 'three';
import { OrbitControls } from 'three/examples/jsm/Addons.js';
import { GLTFLoader } from 'three/examples/jsm/loaders/GLTFLoader.js';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth/window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// camera.position.z = 5;

camera.position.set(0,1,5);

const controles = new OrbitControls(camera, renderer.domElement);
controles.enableDamping = true;
controles.dampingFactor = 0.25;
controles.enableZoom = true;

const loader = new GLTFLoader();

loader.load(
  '/static/models/girl.glb',
  function (gltf) {
    scene.add(gltf.scene);
  },
  undefined,
  function (error) {
    console.error('An error happened during the model load:', error);
  }
);

function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}

animate();
