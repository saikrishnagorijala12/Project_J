# ------------------ File Commands ------------------
def handle_file(text):
    text_lower = text.lower()
    if "list" in text_lower:
        files = os.listdir(".")
        return "Files: " + ", ".join(files)
    elif "create folder" in text_lower:
        os.makedirs("NewFolder", exist_ok=True)
        return "Folder 'NewFolder' created"
    elif "delete folder" in text_lower:
        if os.path.exists("NewFolder"):
            os.rmdir("NewFolder")
            return "Folder 'NewFolder' deleted"
        else:
            return "Folder 'NewFolder' does not exist"
    elif "open folder" in text_lower:
        os.system("xdg-open . &")
        return "Opening current folder"
    else:
        return "File command not recognized."