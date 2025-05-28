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
