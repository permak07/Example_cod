.PHONY: create-structure install-dep install test-pytest

create-structure:
    mkdir -p src tests docx
    touch src/.gitkeep tests/.gitkeep
    touch docx/DOMAIN.md README.md .gitignore
    touch setup.py requirements.txt

install-dep:
    pip install -r requirements.txt

install:
    pip install -e .

test-pytest:
    python -m pytest

test: install-dep install test-pytest