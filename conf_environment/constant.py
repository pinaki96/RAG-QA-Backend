import os


def default_files_dir_created():
    """Ensures default directories exist for file storage."""
    base_dirs = ["uploads", "logs", "temp"]
    for directory in base_dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Created directory: {directory}")
