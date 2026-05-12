import { useEffect, useRef } from 'react'

const vertexShader = `
  void main() {
    gl_Position = vec4(position, 1.0);
  }
`

const fragmentShader = `
  precision highp float;

  uniform vec2 iResolution;
  uniform float iTime;
  uniform float uSpeed;
  uniform float uFractalStep;
  uniform float uFractalAmp;
  uniform float uTerrainScale;
  uniform float uTerrainBaseHeight;
  uniform float uTerrainAmp;
  uniform float uGroundOffset;
  uniform vec3 uColor1;
  uniform vec3 uColor2;
  uniform vec3 uColor3;
  uniform vec3 uColor4;
  uniform float uSeed;

  vec3 getGradient(float t, vec3 c1, vec3 c2, vec3 c3, vec3 c4) {
    t = fract(t);
    if (t < 0.25) return mix(c1, c2, smoothstep(0.0, 0.25, t));
    if (t < 0.50) return mix(c2, c3, smoothstep(0.25, 0.50, t));
    if (t < 0.75) return mix(c3, c4, smoothstep(0.50, 0.75, t));
    return mix(c4, c1, smoothstep(0.75, 1.0, t));
  }

  mat2 getRotationMatrix(float theta) {
    float s = sin(theta);
    float c = cos(theta);
    return mat2(c, s, -s, c);
  }

  float hash(vec2 p) {
    p = fract(p * vec2(125.86, 458.36));
    p += dot(p, p + 44.21);
    return fract(p.x * p.y);
  }

  float getIGN(vec2 p) {
    vec3 magic = vec3(0.02711056, 0.00583715, 52.9829189);
    return fract(magic.z * fract(dot(p, magic.xy)));
  }

  float noise2d(vec2 x) {
    vec2 p = floor(x);
    vec2 f = fract(x);
    f = f * f * (3.0 - 2.0 * f);
    float a = hash(p + vec2(0.0, 0.0));
    float b = hash(p + vec2(1.0, 0.0));
    float c = hash(p + vec2(0.0, 1.0));
    float d = hash(p + vec2(1.0, 1.0));
    return mix(mix(a, b, f.x), mix(c, d, f.x), f.y);
  }

  const mat2 rot55 = mat2(-0.163296, 8.20684, 2.54316, 5.356704);

  float fbm(vec2 p, float d) {
    float value = 0.0;
    float amp = 0.5;
    vec2 shift = vec2(uSeed * 0.13, uSeed * 0.07);

    for (int i = 0; i < 4; i++) {
      if (i > 2) break;
      value += amp * noise2d(p + shift);
      p = rot55 * p * uFractalStep + vec2(1.7, -0.6);
      amp *= 0.52 + uFractalAmp;
    }

    return value;
  }

  float getTerrain(vec3 p, float d) {
    if (p.y > 6.0) return p.y;

    vec2 uv = p.xz * uTerrainScale + vec2(0.0, iTime * uSpeed * 0.16) + uSeed;
    float mountain = fbm(uv, d);
    float ridge = 1.0 - abs(2.0 * mountain - 1.0);
    ridge = pow(ridge, 1.7);
    float h = uTerrainBaseHeight + ridge * uTerrainAmp;

    return p.y + uGroundOffset - h;
  }

  float mapScene(vec3 p, float d) {
    return getTerrain(p, d);
  }

  vec3 getNormal(vec3 p, float d) {
    vec2 e = vec2(0.018, 0.0);
    return normalize(vec3(
      mapScene(p + e.xyy, d) - mapScene(p - e.xyy, d),
      mapScene(p + e.yxy, d) - mapScene(p - e.yxy, d),
      mapScene(p + e.yyx, d) - mapScene(p - e.yyx, d)
    ));
  }

  float trace(vec3 ro, vec3 rd, out vec3 p) {
    float t = 0.0;
    float hit = 0.0;

    for (int i = 0; i < 46; i++) {
      p = ro + rd * t;
      float d = mapScene(p, t);
      if (abs(d) < 0.02 || t > 48.0) {
        hit = step(t, 48.0);
        break;
      }
      t += max(abs(d) * 0.56, 0.055);
    }

    return hit;
  }

  void main() {
    vec2 fragCoord = gl_FragCoord.xy;
    vec2 uv = (fragCoord * 2.0 - iResolution.xy) / max(iResolution.x, iResolution.y);
    float aspect = iResolution.x / iResolution.y;

    vec3 ro = vec3(0.0, 2.35, -10.4 + iTime * uSpeed * 0.13);
    vec3 target = vec3(0.0, -0.44, ro.z + 11.6);
    vec3 ww = normalize(target - ro);
    vec3 uu = normalize(cross(vec3(0.0, 1.0, 0.0), ww));
    vec3 vv = normalize(cross(ww, uu));
    vec3 rd = normalize(uv.x * uu * aspect + uv.y * vv + 1.58 * ww);
    rd.xz = getRotationMatrix(0.025 * sin(iTime * 0.17)) * rd.xz;

    vec3 horizon = getGradient(uv.y * 0.18 + 0.54 + iTime * 0.015, uColor1, uColor2, uColor3, uColor4);
    vec3 sky = mix(vec3(0.004, 0.008, 0.026), horizon * 0.38, smoothstep(-0.34, 0.76, uv.y));

    vec3 p;
    float hit = trace(ro, rd, p);
    vec3 col = sky;

    if (hit > 0.5) {
      vec3 n = getNormal(p, length(p - ro));
      vec3 lightDir = normalize(vec3(-0.35, 0.9, -0.18));
      float diff = clamp(dot(n, lightDir), 0.0, 1.0);
      float fresnel = pow(1.0 - clamp(dot(-rd, n), 0.0, 1.0), 2.0);
      float lines = smoothstep(0.985, 1.0, sin(p.x * 5.8) * 0.5 + 0.5) +
                    smoothstep(0.988, 1.0, sin((p.z + iTime * uSpeed) * 5.4) * 0.5 + 0.5);
      float fog = smoothstep(7.0, 36.0, length(p - ro));
      vec3 terrainColor = getGradient(p.y * 0.08 + p.z * 0.015 + iTime * 0.025, uColor1, uColor2, uColor3, uColor4);
      col = terrainColor * (0.18 + diff * 0.55) + terrainColor * fresnel * 0.9;
      col += terrainColor * lines * 0.22;
      col = mix(col, sky, fog);
    }

    float vignette = smoothstep(1.4, 0.18, length(uv));
    col *= 0.58 + vignette * 0.42;
    col += (getIGN(fragCoord) - 0.5) * 0.018;

    gl_FragColor = vec4(col, 0.74);
  }
`

const prefersReducedMotion = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches

export default function QuantumLandscapeBackground() {
  const hostRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (!hostRef.current || prefersReducedMotion() || import.meta.env.MODE === 'test') {
      return
    }

    const host = hostRef.current
    let disposed = false
    let disposeScene = () => {}

    import('three')
      .then((THREE) => {
        if (disposed || !host.isConnected) {
          return
        }

        const scene = new THREE.Scene()
        const camera = new THREE.OrthographicCamera(-1, 1, 1, -1, 0.1, 10)
        camera.position.z = 1

        let renderer: import('three').WebGLRenderer
        try {
          renderer = new THREE.WebGLRenderer({ antialias: false, alpha: true, powerPreference: 'low-power' })
        } catch (error) {
          console.warn('Quantum landscape background disabled because WebGL is unavailable.', error)
          return
        }

        renderer.domElement.className = 'quantum-landscape-canvas'
        renderer.setClearColor(0x000000, 0)
        host.appendChild(renderer.domElement)

        const uniforms = {
          iResolution: { value: new THREE.Vector2() },
          iTime: { value: 0 },
          uSpeed: { value: 0.82 },
          uFractalStep: { value: 0.020531 },
          uFractalAmp: { value: 0.06688 },
          uTerrainScale: { value: 0.31 },
          uTerrainBaseHeight: { value: 0.46 },
          uTerrainAmp: { value: 0.52 },
          uGroundOffset: { value: 3.1 },
          uColor1: { value: new THREE.Color('#0a9fbd') },
          uColor2: { value: new THREE.Color('#00d2ff') },
          uColor3: { value: new THREE.Color('#001adb') },
          uColor4: { value: new THREE.Color('#ff0055') },
          uSeed: { value: 144.0 },
        }

        const material = new THREE.ShaderMaterial({
          uniforms,
          vertexShader,
          fragmentShader,
          transparent: true,
          depthWrite: false,
          depthTest: false,
        })
        const geometry = new THREE.PlaneGeometry(2, 2)
        const mesh = new THREE.Mesh(geometry, material)
        scene.add(mesh)

        const updateDPR = () => {
          const dpr = Math.min(window.devicePixelRatio || 1, 0.9)
          renderer.setPixelRatio(dpr)
        }

        const onWindowResize = () => {
          const width = window.innerWidth
          const height = window.innerHeight
          renderer.setSize(width, height, false)
          const pixelRatio = renderer.getPixelRatio()
          uniforms.iResolution.value.set(width * pixelRatio, height * pixelRatio)
        }

        updateDPR()
        onWindowResize()
        window.addEventListener('resize', onWindowResize)

        const clock = new THREE.Clock()
        let frameId = 0
        let lastRender = 0
        const frameInterval = 1000 / 30
        const animate = (now = 0) => {
          if (now - lastRender >= frameInterval) {
            uniforms.iTime.value = clock.getElapsedTime()
            renderer.render(scene, camera)
            lastRender = now
          }
          frameId = requestAnimationFrame(animate)
        }
        animate()

        disposeScene = () => {
          cancelAnimationFrame(frameId)
          window.removeEventListener('resize', onWindowResize)
          geometry.dispose()
          material.dispose()
          renderer.dispose()
          renderer.domElement.remove()
        }
      })
      .catch((error: unknown) => {
        console.warn('Quantum landscape background could not load Three.js.', error)
      })

    return () => {
      disposed = true
      disposeScene()
    }
  }, [])

  return <div className="site-background" aria-hidden="true" data-testid="quantum-landscape-background" ref={hostRef} />
}
