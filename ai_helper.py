import os
from pathspec import PathSpec


class ProjectFileCollector:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.gitignore_path = os.path.join(root_dir, '.gitignore')
        self.project_files = []
        self.ignore_spec = None

    def collect_project_files(self):
        self._parse_gitignore()
        self._walk_project_directory()
        self._save_project_files()

    def _parse_gitignore(self):
        if os.path.exists(self.gitignore_path):
            with open(self.gitignore_path, 'r') as f:
                gitignore_content = f.read()
                self.ignore_spec = PathSpec.from_lines('gitwildmatch', gitignore_content.splitlines())

    def _walk_project_directory(self):
        for root, dirs, files in os.walk(self.root_dir):
            dirs[:] = [d for d in dirs if not self._is_ignored(os.path.join(root, d))]
            for file in files:
                file_path = os.path.join(root, file)
                if not self._is_ignored(file_path):
                    self._add_file_to_project_files(file_path)

    def _is_ignored(self, path):
        if self.ignore_spec is None:
            return False
        relative_path = os.path.relpath(path, self.root_dir)
        ignored_files = ['__init__.py', '.gitignore', 'pyproject.toml', 'requirements.txt', 'ai_helper.py']
        if any(relative_path.endswith(file) for file in ignored_files):
            return True
        return self.ignore_spec.match_file(relative_path)

    def _add_file_to_project_files(self, file_path):
        encodings = ['utf-8', 'latin1', 'cp1251']  # Добавьте другие возможные кодировки
        for encoding in encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    content = f.read()
                    self.project_files.append(f"{file_path}\n{content}")
                    break
            except UnicodeDecodeError:
                continue
        else:
            print(f"Could not decode file: {file_path}")

    def _save_project_files(self):
        with open('project_files.txt', 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(self.project_files))


class GitignoreManager:
    def __init__(self, root_dir, gitignore_content):
        self.root_dir = root_dir
        self.gitignore_path = os.path.join(root_dir, '.gitignore')
        self.gitignore_content = gitignore_content

    def create_gitignore(self):
        if not os.path.exists(self.gitignore_path):
            with open(self.gitignore_path, 'w', encoding='utf-8') as f:
                f.write(self.gitignore_content)

    def update_gitignore(self):
        if os.path.exists(self.gitignore_path):
            with open(self.gitignore_path, 'r', encoding='utf-8') as f:
                existing_content = f.read()
            new_lines = [line for line in self.gitignore_content.splitlines()
                         if line.strip() and line not in existing_content]
            if new_lines:
                with open(self.gitignore_path, 'a', encoding='utf-8') as f:
                    f.write('\n' + '\n'.join(new_lines))


def main():
    root_dir = '.'
    gitignore_content = '''
# Файлы Python
*.pyc
*.pyo
*.pyd
*.pyz
*.pyw
*.pyx
*.pxi
*.egg-info/
*.egg
*.sqlite3
# Директории Python
**/__pycache__/
venv/
env/
.venv/
.env/
.virtualenv/
# Файлы Jupyter Notebook
.ipynb_checkpoints/
# Файлы конфигурации и секретов
config.yml
.env.local
.env.*.local
*.pem
*.key
# Файлы IDE и редакторов
.vscode/
.idea/
*.sublime-workspace
# Логи и временные файлы
*.log
*.tmp
*.bak
*.swp
# Файлы зависимостей
poetry.lock
Pipfile.lock
# Файлы покрытия тестами
.coverage
.coverage.*
htmlcov/
# Файлы документации
docs/
doc/
# Файлы операционной системы
.DS_Store
Thumbs.db
project_files.txt
# Другие специфичные для проекта файлы и директории
.git
*.onnx
*.mp3
*.json
*.txt
alembic/
*.ini
*.conf
*.xls
    '''

    gitignore_manager = GitignoreManager(root_dir, gitignore_content)
    gitignore_manager.create_gitignore()
    gitignore_manager.update_gitignore()

    project_file_collector = ProjectFileCollector(root_dir)
    project_file_collector.collect_project_files()


if __name__ == '__main__':
    main()
