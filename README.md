# Sesión Práctica #7: Continuous Integration

**Universidad del Valle de Guatemala – Campus Central**  
Facultad de Ingeniería · Semestre II 2026  
Departamento de Ciencias de la Computación · Ciclo 2 – Año 5  
CC3047 – Administración y Mantenimiento de Sistemas  
Catedrático: Vinicio Paz

## Objetivo

Implementar una librería pequeña de matemática básica, probar sus casos exitosos y de error, y ejecutar las pruebas automáticamente en cada Pull Request dirigido a `main`.

## Funciones

El módulo [`mathlib.py`](mathlib.py) ofrece estas funciones:

| Función | Comportamiento |
| --- | --- |
| `square(n)` | Retorna el cuadrado de un número real. |
| `factorial(n)` | Retorna el factorial de un entero no negativo. `factorial(0)` retorna `1`. |
| `is_prime(n)` | Retorna `True` si el entero es primo. Los enteros menores que `2` retornan `False`. |
| `gcd(a, b)` | Retorna el máximo común divisor no negativo. |
| `lcm(a, b)` | Retorna el mínimo común múltiplo no negativo. Si algún valor es `0`, retorna `0`. |

Las funciones que requieren enteros rechazan valores no enteros con `TypeError`. `factorial` rechaza negativos con `ValueError`. `square` acepta números reales, incluidos negativos y decimales, y rechaza booleanos y valores no numéricos con `TypeError`.

## Ejecutar las pruebas

Se requiere Python 3.10 o posterior; no hay dependencias externas.

```bash
python -m unittest discover -s tests -v
```

Las pruebas están en [`tests/test_matematicas.py`](tests/test_matematicas.py). Cada función tiene escenarios exitosos y casos borde o de error.

## Integración continua

El workflow [`.github/workflows/tests.yml`](.github/workflows/tests.yml) corre en cada Pull Request hacia `main`. Para impedir el merge mientras las pruebas fallen, la rama `main` debe requerir el check **Pruebas unitarias** en la protección de rama.

## Demostración sugerida

1. Abre un Pull Request hacia `main` y confirma que el check **Pruebas unitarias** pasa.
2. En la rama del PR, cambia temporalmente un resultado esperado en una prueba para que contradiga la implementación y sube el cambio.
3. Muestra que el check falla y que GitHub bloquea el merge mientras el check requerido esté pendiente o fallido.
4. Restaura el resultado correcto, sube la corrección y espera a que el check pase antes de hacer merge.

No dejes el cambio intencionalmente incorrecto en `main`.
