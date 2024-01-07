import os

def split_file(file_path, chunk_size):
    file_size = os.path.getsize(file_path)
    chunk_size_bytes = chunk_size * 1024 * 1024 * 1024  # Convert GB to bytes
    num_chunks = file_size // chunk_size_bytes

    with open(file_path, 'rb') as file:
        for i in range(num_chunks):
            chunk_data = file.read(chunk_size_bytes)
            chunk_file_name = f'{file_path}.part{i+1}'
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
    chunk_size_gb = 4.5
    split_file(file_path, chunk_size_gb)


if main == "__main__":
    main()