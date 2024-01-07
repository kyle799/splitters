#!/bin/python3
import os, hashlib, argparse


def split_file(file_path, chunk_size):
    file_size = os.path.getsize(file_path)
    chunk_size_bytes = chunk_size * 1024 * 1024 * 1024  # Convert GB to bytes
    chunk_size_bytes = int(chunk_size_bytes)
    num_chunks = file_size // chunk_size_bytes
    num_chunks = (int(num_chunks))

    with open(file_path, 'rb') as file:
        for i in range(num_chunks):
            chunk_data = file.read(chunk_size_bytes)
            chunk_file_name = f'{file_path}.part{i+1}'
            print(f"Chonking file {i+1} of {num_chunks+1} {round((i+1)/num_chunks*100)}% complete {' ' * 20}", end='\r')
            with open(chunk_file_name, 'wb') as chunk_file:
                chunk_file.write(chunk_data)

        # Write the remaining data to the last chunk file
        remaining_data = file.read()
        last_chunk_file_name = f'{file_path}.part{num_chunks+1}'
        with open(last_chunk_file_name, 'wb') as last_chunk_file:
            last_chunk_file.write(remaining_data)
            print(f"Chonking file {num_chunks+1} of {num_chunks+1} 100% complete {' ' * 20}", end='\r')

def get_sha256(file_path):
    sha256_hash = hashlib.sha256()
    print(f"Hashing file {file_path} {' ' * 20}")
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
    print(f"Hashing complete\n{sha256_hash.hexdigest()}")
    return sha256_hash.hexdigest()

parser = argparse.ArgumentParser(description="Split files to fit on DVD's (or CD's).")
parser.add_argument('-f', '--file', type=str, help='The file to chunk')
parser.add_argument('-s', '--size', type=float, help='The size of each file to fit on CD (700MB) or DVD (4.5GB)')
args = parser.parse_args()

def main():
    file_path = args.file if args.file else input("Enter the file path: ")
    chunk_size_gb = args.size if args.size else input("Enter the file chunk size (in GB), default to 4.5 GB: ")
    if chunk_size_gb == "":
        chunk_size_gb = 4.5
    else:
        chunk_size_gb = float(chunk_size_gb)
    split_file(file_path, chunk_size_gb)
    print(f"Wrote all files to {os.getcwd()}/{file_path}.part(NUM)")
    with open(f"{file_path}.sha256", "w") as f:
        f.write(get_sha256(file_path))
if __name__ == "__main__":
    main()