#!/bin/python3
import os, hashlib, argparse, re

def join_files(sorted_files, new_file):
    num=0
    for file in sorted_files:
        
        if "part" in file:
            num = num + 1
            print(f"Joining file {file} into {new_file} {round((num/len(sorted_files))*100)}% complete {' ' * 20}", end='\r')
            with open(file, 'rb') as file_to_join, open(new_file, 'ab') as file2:
                file2.write(file_to_join.read())

def get_sha256(file_path):
    sha256_hash = hashlib.sha256()
    print(f"Hashing file {file_path} {' ' * 50}")
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def compare_hashes(hash, sorted_files):
    with open(sorted_files[-1], "r") as f:
        old_hash = f.read()
    if hash == old_hash:
        print("Hashes match, join successfull")
        delete_files = input("Would you like to delete old files? (y/n)")
        if "y" or "Y" in delete_files:
            for file in sorted_files:
                os.remove(file)
    else:
        print(f"Hashes do not match, join failed, make sure the {sorted_files[-1]} file is in the same directory as the files you are trying to join, and is correct")

def extract_number(filename):
    match = re.search(r'\d+$', filename)
    return int(match.group()) if match else None


def main():
    directory = input("Enter the directory of the files you want to join: ")
    os.chdir(directory)
    files = os.listdir(directory)
    sorted_files = sorted(files, key=extract_number)
    new_file = sorted_files[0].split(".")[0]

    join_files(sorted_files, new_file)
    
    hash=get_sha256(new_file)
    compare_hashes(hash, sorted_files)
    
if __name__ == "__main__":
    main()