import hashlib
import sys

def calculate_sha256(filepath, chunk_size=8192):
    """Calculate SHA256 hash of a file reading it in chunks"""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(chunk_size):
                sha256_hash.update(chunk)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python check_hash.py <file_path> <expected hash>")
        sys.exit(1)

    data_file_path = sys.argv[1]
    checksum_file_path = sys.argv[2]

    # Calculate the hash of the data file
    print(f"Calculating hash of {data_file_path}...")
    calculated_hash = calculate_sha256(data_file_path)

    if calculated_hash is None:
        print(f"Error: file {data_file_path} not found")
        sys.exit(1)

    print(f"Calculated hash: {calculated_hash}")

    # Read the expected hash from the .CHECKSUM file
    try:
        with open(checksum_file_path, 'r') as f:
            line = f.readline().strip()
            expected_hash = line.split()[0]
            print(f"Expected hash: {expected_hash}")
    except FileNotFoundError:
        print(f"Error: CHECKSUM file {checksum_file_path} not found")
        sys.exit(1)
    except IndexError:
        print(f"Error: cannot read hash from file 'checksum_file_path'. The file is empty or has an invalid format")
        sys.exit(1)

    # Compare hashes
    if calculated_hash.lower() == expected_hash.lower():
        print("\nThe check is passed! The checksums match. The file was downloaded correctly")
    else:
        print("\nAttention! The checksums DON'T match. The file may be corrupted.")