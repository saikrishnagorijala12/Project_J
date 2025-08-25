import os,subprocess,platform,fnmatch

# ------------------ File Commands ------------------
def handle_file(text):
    text_lower = text.lower()

    # List files in current directory
    if "list" in text_lower:
        files = os.listdir(".")
        if files:
            return "Files: " + ", ".join(files[:10])  # limit to first 10 for readability
        else:
            return "This folder is empty."

    # Create a folder dynamically
    elif "create folder" in text_lower:
        parts = text_lower.split("create folder")
        if len(parts) > 1:
            folder_name = parts[1].strip().title()  # capitalize nicely
        else:
            folder_name = "NewFolder"
        os.makedirs(folder_name, exist_ok=True)
        return f"Folder '{folder_name}' created."

    # Delete a folder dynamically
    elif "delete folder" in text_lower:
        parts = text_lower.split("delete folder")
        if len(parts) > 1:
            folder_name = parts[1].strip().title()
        else:
            folder_name = "NewFolder"
        if os.path.exists(folder_name):
            try:
                os.rmdir(folder_name)  # only works if empty
                return f"Folder '{folder_name}' deleted."
            except OSError:
                return f"Folder '{folder_name}' is not empty. Cannot delete."
        else:
            return f"Folder '{folder_name}' does not exist."

    # Open a folder
    elif "open folder" in text_lower:
        parts = text_lower.split("open folder")
        if len(parts) > 1:
            folder_name = parts[1].strip().title()
        else:
            folder_name = "."
        if os.path.exists(folder_name):
            if platform.system() == "Darwin":  # macOS
                subprocess.call(["open", folder_name])
            elif platform.system() == "Windows":
                os.startfile(folder_name)
            else:  # Linux
                subprocess.call(["xdg-open", folder_name])
            return f"Opening folder '{folder_name}'."
        else:
            return f"Folder '{folder_name}' not found."

    # Search for a file
    elif "find" in text_lower or "search" in text_lower:
        parts = text_lower.replace("find", "").replace("search", "").strip()
        results = []
        for root, _, files in os.walk(os.path.expanduser("~")):
            for name in files:
                if fnmatch.fnmatch(name.lower(), f"*{parts.lower()}*"):
                    results.append(os.path.join(root, name))
        if results:
            return f"I found {len(results)} file(s). Top result: {results[0]}"
        else:
            return "I couldn’t find that file."

    else:
        return "File command not recognized."