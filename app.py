import hashlib

def get_sha256_hash(user_input: str) -> str:
    """Returns the SHA-256 hash of the given input string."""
    return hashlib.sha256(user_input.encode()).hexdigest()

def get_sha256_hash_from_file(file_path: str) -> str:
    """Returns the SHA-256 hash of the contents of a given .txt file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        print(f"Contents of the file:\n{content}")  # Print the contents of the file
        return hashlib.sha256(content.encode()).hexdigest()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    user_input = input("Enter a string: ")
    hash_output = get_sha256_hash(user_input)
    print(f"User input: {user_input}")
    print(f"SHA-256 Hash: {hash_output}")
    
    file_path = input("Enter the path to a .txt file: ")
    file_hash_output = get_sha256_hash_from_file(file_path)
    print(f"SHA-256 Hash of file: {file_hash_output}")

if __name__ == "__main__":
    main()