import hashlib

def calcular_md5sum(ruta_archivo, tamano_bloque=65536):
    md5 = hashlib.md5()
    try:
        with open(ruta_archivo, 'rb') as archivo:
            for bloque in iter(lambda: archivo.read(tamano_bloque), b''):
                md5.update(bloque)
        return md5.hexdigest()
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al calcular el hash MD5: {e}")
        return None
    
def get_hashes(filepath):
    with open(filepath, "r") as f:
        expected_hashes = [line.strip() for line in f.readlines()]
        return expected_hashes

def detect_integrity_violation(root_path, expected_hashes):
    print("Detecting integrity violation...")
    for expected_hash in expected_hashes:
        expected_hash, blank, file = expected_hash.split(" ")
        path = root_path+file
        actual_hash = calcular_md5sum(path)
        if actual_hash != expected_hash:
            print(f"Integrity violation detected in file '{path}'")
            print(f"Expected hash: {expected_hash}")
            print(f"Actual hash: {actual_hash}")
            return True
    
    print("No integrity violation detected")
    return False

hashes = get_hashes("PyJ Systems\hashes.txt")
detect_integrity_violation("PyJ Systems/", hashes)