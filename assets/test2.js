import * as THREE from "three";
import { Curves, OrbitControls } from "three/examples/jsm/Addons.js";
import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js";

const path = window.PRODUCT_FILE_URL;
console.log(path)

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    1000
);
const renderer = new THREE.WebGLRenderer({ antialias: true });
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

// camera.position.z = 5;

camera.position.set(453, 124, 228);

const controles = new OrbitControls(camera, renderer.domElement);
controles.enableDamping = true;
controles.dampingFactor = 0.25;
controles.enableZoom = true;

const loader = new GLTFLoader();

const ambientLight = new THREE.AmbientLight(0xffffff, 0.5); // Мягкий свет

const directionalLight = new THREE.DirectionalLight(0xffffff, 1); // Направленный свет
directionalLight.position.set(5, 5, 5);

loader.load(
    path,
    function (gltf) {
	scene.add(ambientLight);
	scene.add(directionalLight);
	scene.add(gltf.scene);

	
	gltf.animations; // Array<THREE.AnimationClip>
	gltf.scene; // THREE.Group
	gltf.scenes; // Array<THREE.Group>
	gltf.cameras; // Array<THREE.Camera>
	gltf.asset; // Object
    },
    function (xhr) {
	console.log((xhr.loaded / xhr.total) * 100 + "% loaded");
    },
    function (error) {
	console.error("Ошибка загрузки модели:", error);
    }
);

function animate() {
    // console.log(camera.position)
    requestAnimationFrame(animate);
    renderer.render(scene, camera);
}


animate();
