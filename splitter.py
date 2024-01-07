#!/bin/python3
import os

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

# Usage example
def main():
    file_path = input("Enter the file path: ")
    chunk_size_gb = input("Enter the file chunk size (in GB), default to 4.5 GB: ")
    if chunk_size_gb == "":
        chunk_size_gb = 4.5
    else:
        chunk_size_gb = float(chunk_size_gb)
    
    split_file(file_path, chunk_size_gb)

if __name__ == "__main__":
    main()
    