#Importing OS.
import os

def create_directory_structure():
    """
    Kicks off the directory tree setup using the os module's mkdir function.
    Includes simple exception handling just in case the folders already exist.
    """
    # Setting up the target names for the operation.
    main_dir = 'MyFiles'
    sub_dirs = ['Docs', 'Images', 'Videos']
    
    try:
        # Initializing the primary container. This function will throw FileExistsError if it's already there.
        print(f"Action: Attempting to initialize primary directory '{main_dir}'...")
        os.mkdir(main_dir)
        print(f"Success! Root directory '{main_dir}' deployed.")
        
        # Looping through and creating the nested paths required for the hierarchy.
        for sub_dir in sub_dirs:
            # os.path.join() handles correct, OS-specific path separators (e.g., / or \), which is good practice.
            full_path = os.path.join(main_dir, sub_dir)
            
            print(f"Action: Creating nested path: {full_path}")
            os.mkdir(full_path)
            print(f"Path created: {sub_dir}")

    except FileExistsError:
        # A clean way to handle idempotence. If the file structure is present, we just skip creation.
        print("\nStructure detected! Directory architecture is already deployed; aborting creation attempt.")
    except OSError as e:
        # Catch any serious non-existence errors (like permissions) and report the exception details.
        print(f"\nCRITICAL I/O ERROR: Failed to execute mkdir operation. Check permissions or path integrity. Details: {e}")
        
    print("\nDirectory organization task finished.")

create_directory_structure()