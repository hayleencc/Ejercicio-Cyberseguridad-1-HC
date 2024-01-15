from script import calcular_md5sum

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