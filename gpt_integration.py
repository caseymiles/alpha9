import os
import openai

# Configure your OpenAI API key
openai.api_key = "your-api-key-here"

# Set the path to your project folder
project_path = "C:/Users/casey/websites/Alpha9/files"

# Function to list all files in the project folder
def list_files():
    print("\nFiles in your project folder:\n")
    for root, dirs, files in os.walk(project_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)

# Function to read the contents of a selected file
def read_file():
    list_files()
    file_path = input("\nEnter the full path of the file you want to read: ").strip()
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            print(f"\nContents of {file_path}:\n")
            print(content)
            return file_path, content
    except Exception as e:
        print(f"Error reading file: {e}")
        return None, None

# Function to analyze a file using GPT
def analyze_file(content):
    prompt = f"Analyze the following file and suggest improvements:\n\n{content}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
        )
        suggestions = response['choices'][0]['message']['content']
        print("\nGPT Suggestions:\n")
        print(suggestions)
        return suggestions
    except Exception as e:
        print(f"Error analyzing file: {e}")
        return None

# Function to update a file with new content
def write_file(file_path, new_content):
    try:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(new_content)
        print(f"\nFile {file_path} updated successfully!")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Main loop to interact with the script
def main():
    while True:
        print("\nOptions:")
        print("1. List all files")
        print("2. Read a file")
        print("3. Analyze a file with GPT")
        print("4. Update a file with GPT suggestions")
        print("5. Exit")

        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            list_files()
        elif choice == "2":
            _, content = read_file()
        elif choice == "3":
            file_path, content = read_file()
            if content:
                suggestions = analyze_file(content)
        elif choice == "4":
            file_path, content = read_file()
            if content:
                suggestions = analyze_file(content)
                if suggestions:
                    confirm = input("\nDo you want to update the file with GPT suggestions? (yes/no): ").strip().lower()
                    if confirm == "yes":
                        write_file(file_path, suggestions)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
