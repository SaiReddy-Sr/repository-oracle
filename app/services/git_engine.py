import os
import shutil
import stat
from git import Repo

def remove_readonly(func, path, excinfo):
    """Clear the readonly bit and reattempt the removal."""
    os.chmod(path, stat.S_IWRITE)
    func(path)

def clone_repo(repo_url: str, dest_dir: str):
    """Clones the given repository to dest_dir with depth 1."""
    if os.path.exists(dest_dir):
        delete_temp_dir(dest_dir)
    Repo.clone_from(url=repo_url, to_path=dest_dir, depth=1)

def delete_temp_dir(dest_dir: str):
    """Safely delete the temp directory, handling readonly files."""
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir, onerror=remove_readonly)

def extract_code(dest_dir: str, extensions=('.py', '.js', '.go', '.md')) -> str:
    """Extract and concatenate content of specific files."""
    code_contents = []
    
    for root, dirs, files in os.walk(dest_dir):
        # Exclude hidden directories (like .git)
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        for file in files:
            if file.endswith(extensions):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        rel_path = os.path.relpath(filepath, dest_dir)
                        code_contents.append(f"--- FILE: {rel_path} ---\n{content}")
                except Exception as e:
                    print(f"Failed to read {filepath}: {e}")
                    
    return "\n\n".join(code_contents)
