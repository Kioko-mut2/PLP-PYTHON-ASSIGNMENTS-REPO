def file_read_write_challenge():
    """
    File Read & Write Challenge with Error Handling
    Reads a file, modifies its content, and writes to a new file
    """
    
    print("📁 File Read & Write Challenge 🖋️")
    print("=" * 50)
    
    while True:
        try:
            # Get input filename from user
            input_filename = input("\nEnter the filename to read (or 'quit' to exit): ").strip()
            
            if input_filename.lower() == 'quit':
                print("Goodbye! 👋")
                break
            
            if not input_filename:
                print("❌ Please enter a valid filename.")
                continue
            
            # Read the file
            print(f"📖 Attempting to read: {input_filename}")
            
            try:
                with open(input_filename, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                print(f"✅ Successfully read {len(content)} characters from {input_filename}")
                
                # Modify the content (example modifications)
                modified_content = modify_content(content)
                
                # Get output filename
                output_filename = get_output_filename(input_filename)
                
                # Write to new file
                try:
                    with open(output_filename, 'w', encoding='utf-8') as file:
                        file.write(modified_content)
                    
                    print(f"✅ Successfully wrote modified content to: {output_filename}")
                    print(f"📊 Original size: {len(content)} characters")
                    print(f"📊 Modified size: {len(modified_content)} characters")
                    
                except PermissionError:
                    print(f"❌ Permission denied: Cannot write to {output_filename}")
                except IOError as e:
                    print(f"❌ Error writing to file: {e}")
                
            except FileNotFoundError:
                print(f"❌ File not found: {input_filename}")
                print("💡 Please check the filename and try again.")
            except PermissionError:
                print(f"❌ Permission denied: Cannot read {input_filename}")
            except UnicodeDecodeError:
                print(f"❌ Encoding error: Could not read {input_filename} as text")
                print("💡 This might be a binary file or use a different encoding.")
            except IOError as e:
                print(f"❌ Error reading file: {e}")
            
        except KeyboardInterrupt:
            print("\n\n👋 Operation cancelled by user. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Unexpected error: {e}")

def modify_content(content):
    """
    Modify the file content with various transformations
    """
    print("\n🔄 Modifying content...")
    
    # Example modifications - you can customize these
    modifications = []
    
    # 1. Convert to uppercase
    uppercase_content = content.upper()
    modifications.append(("Uppercase conversion", uppercase_content))
    
    # 2. Add line numbers
    lines = content.split('\n')
    numbered_lines = [f"{i+1:3d}: {line}" for i, line in enumerate(lines)]
    numbered_content = '\n'.join(numbered_lines)
    modifications.append(("Added line numbers", numbered_content))
    
    # 3. Reverse the content
    reversed_content = content[::-1]
    modifications.append(("Reversed content", reversed_content))
    
    # 4. Double spaces (new modification)
    double_spaced = content.replace('\n', '\n\n')
    modifications.append(("Double spaced lines", double_spaced))
    
    # Let user choose modification
    print("\nChoose modification type:")
    for i, (mod_name, _) in enumerate(modifications, 1):
        print(f"{i}. {mod_name}")
    
    while True:
        try:
            choice = input(f"Enter choice (1-{len(modifications)}): ").strip()
            if choice and 1 <= int(choice) <= len(modifications):
                mod_name, modified_content = modifications[int(choice) - 1]
                print(f"✅ Selected: {mod_name}")
                return modified_content
            else:
                print("❌ Invalid choice. Please try again.")
        except ValueError:
            print("❌ Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nUsing default modification (uppercase)")
            return modifications[0][1]

def get_output_filename(input_filename):
    """
    Generate output filename based on input filename
    """
    import os
    import time
    
    # Extract base name without extension
    base_name = os.path.splitext(input_filename)[0]
    extension = os.path.splitext(input_filename)[1] or '.txt'
    
    # Create output filename with timestamp
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    output_filename = f"{base_name}_modified_{timestamp}{extension}"
    
    # Ensure filename is valid and doesn't exist
    counter = 1
    original_output = output_filename
    
    while os.path.exists(output_filename):
        output_filename = f"{base_name}_modified_{timestamp}_{counter}{extension}"
        counter += 1
        if counter > 100:  # Safety limit
            break
    
    return output_filename

def create_sample_file():
    """
    Create a sample file for testing if needed
    """
    sample_content = """Hello World!
This is a sample file for testing.
File Read & Write Challenge 🖋️
Error Handling Lab 🧪
Python is awesome! 🐍
Programming is fun! 💻
"""
    
    try:
        with open('sample.txt', 'w', encoding='utf-8') as file:
            file.write(sample_content)
        print("✅ Created sample.txt for testing")
        return 'sample.txt'
    except IOError as e:
        print(f"❌ Could not create sample file: {e}")
        return None

# Main execution
if __name__ == "__main__":
    print("Welcome to the File Read & Write Challenge! 🎯")
    print("This program reads a file, modifies it, and saves a new version.")
    print("-" * 60)
    
    # Offer to create a sample file
    create_sample = input("Would you like to create a sample file for testing? (y/n): ").lower()
    if create_sample in ['y', 'yes']:
        sample_file = create_sample_file()
        if sample_file:
            print(f"💡 You can now try reading: {sample_file}")
    
    print("\n" + "="*60)
    # Start the main program
    file_read_write_challenge()