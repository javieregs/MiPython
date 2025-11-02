"""
EJEMPLO 14: APIS Y REQUESTS
----------------------------
Aprende a hacer peticiones HTTP y trabajar con APIs (requiere: pip install requests)
"""

# Nota: Para ejecutar este ejemplo, instala requests: pip install requests

try:
    import requests
    import json
    
    print("=== HACER PETICIONES HTTP ===")
    
    # PETICIÓN GET SIMPLE
    print("\n1. Petición GET simple:")
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=5)
        response.raise_for_status()  # Lanza excepción si hay error HTTP
        
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(list(response.headers.items())[:3])}")
        
        datos = response.json()
        print(f"\nDatos recibidos:")
        print(f"Título: {datos.get('title', 'N/A')}")
        print(f"Body: {datos.get('body', 'N/A')[:50]}...")
    except requests.exceptions.RequestException as e:
        print(f"Error en la petición: {e}")
    
    # PETICIÓN POST (crear recurso)
    print("\n2. Petición POST:")
    try:
        nuevo_post = {
            "title": "Mi nuevo post",
            "body": "Este es el contenido de mi post",
            "userId": 1
        }
        
        response = requests.post(
            "https://jsonplaceholder.typicode.com/posts",
            json=nuevo_post,
            timeout=5
        )
        response.raise_for_status()
        
        print(f"Status Code: {response.status_code}")
        respuesta = response.json()
        print(f"Post creado con ID: {respuesta.get('id')}")
    except requests.exceptions.RequestException as e:
        print(f"Error en la petición: {e}")
    
    # API PÚBLICA: REST Countries
    print("\n3. Consultar API de países:")
    try:
        response = requests.get("https://restcountries.com/v3.1/name/spain", timeout=5)
        response.raise_for_status()
        
        pais = response.json()[0]
        print(f"País: {pais['name']['common']}")
        print(f"Capital: {', '.join(pais.get('capital', ['N/A']))}")
        print(f"Población: {pais['population']:,}")
        print(f"Región: {pais['region']}")
    except requests.exceptions.RequestException as e:
        print(f"Error en la petición: {e}")
    
    # MANEJO DE ERRORES
    print("\n4. Manejo de errores:")
    def hacer_peticion_segura(url):
        """Hace una petición HTTP con manejo de errores"""
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.Timeout:
            print(f"Timeout: La petición tardó demasiado")
            return None
        except requests.exceptions.ConnectionError:
            print(f"Error de conexión: No se pudo conectar al servidor")
            return None
        except requests.exceptions.HTTPError as e:
            print(f"Error HTTP {e.response.status_code}: {e}")
            return None
        except requests.exceptions.RequestException as e:
            print(f"Error en la petición: {e}")
            return None
    
    datos = hacer_peticion_segura("https://jsonplaceholder.typicode.com/posts/1")
    if datos:
        print("Petición exitosa")
    
    # TRABAJAR CON HEADERS
    print("\n5. Petición con headers personalizados:")
    try:
        headers = {
            "User-Agent": "MiAppPython/1.0",
            "Accept": "application/json"
        }
        
        response = requests.get(
            "https://httpbin.org/headers",
            headers=headers,
            timeout=5
        )
        response.raise_for_status()
        
        datos = response.json()
        print(f"Headers enviados:")
        print(json.dumps(datos.get('headers', {}), indent=2))
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    
    # EJEMPLO PRÁCTICO: Clase para API
    print("\n6. Clase para trabajar con APIs:")
    
    class ClienteAPI:
        """Clase para interactuar con una API"""
        
        def __init__(self, base_url):
            self.base_url = base_url
            self.session = requests.Session()
        
        def get(self, endpoint, params=None):
            """Hace una petición GET"""
            url = f"{self.base_url}{endpoint}"
            try:
                response = self.session.get(url, params=params, timeout=5)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"Error en GET: {e}")
                return None
        
        def post(self, endpoint, data=None):
            """Hace una petición POST"""
            url = f"{self.base_url}{endpoint}"
            try:
                response = self.session.post(url, json=data, timeout=5)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                print(f"Error en POST: {e}")
                return None
    
    # Usar la clase
    cliente = ClienteAPI("https://jsonplaceholder.typicode.com")
    
    # Obtener posts
    posts = cliente.get("/posts", params={"_limit": 3})
    if posts:
        print(f"\nPrimeros 3 posts:")
        for post in posts:
            print(f"- Post {post['id']}: {post['title'][:40]}...")

except ImportError:
    print("=== REQUESTS NO INSTALADO ===")
    print("\nPara ejecutar este ejemplo, instala la biblioteca requests:")
    print("pip install requests")
    print("\nEste ejemplo muestra cómo trabajar con APIs HTTP en Python.")
    print("Puedes instalar requests y ejecutar este script para ver ejemplos prácticos.")

