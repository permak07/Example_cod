.PHONY: create-structure install-dep install test-pytest check-missing-reqs

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

check-missing-reqs:
	@echo "Проверка импортов, отсутствующих в requirements.txt..."
	@# Собираем все корневые имена импортов (первая часть до точки)
	@find . -name "*.py" ! -path "*/venv/*" ! -path "*/env/*" ! -path "*/.tox/*" \
		-exec grep -hE '^[[:space:]]*(from|import)[[:space:]]+([a-zA-Z0-9_]+)' {} \; \
		| awk '{print $$2}' \
		| sed 's/[.,].*//' \
		| sort -u > /tmp/imported_modules.tmp
	@# Извлекаем имена пакетов из requirements.txt (игнорируем версии и комментарии)
	@grep -v '^#' requirements.txt \
		| sed 's/[=<>~].*//' \
		| sort -u > /tmp/required_packages.tmp
	@# Исключаем стандартные модули Python (примерный список)
	@{ echo "os sys re math datetime json random time argparse collections itertools functools pathlib typing abc warnings logging traceback unittest copy pickle"; \
	   echo "subprocess multiprocessing threading concurrent queue socket ssl http urllib xml csv hashlib base64 hmac secrets token"; \
	   echo "bz2 gzip zipfile tarfile shutil tempfile glob fnmatch linecache fileinput stat"; \
	   echo "inspect pdb profile pstats cProfile timeit doctest unittest mock"; \
	   echo "sqlite3 dbm pickle shelve marshal"; \
	   echo "ctypes ctypes.util"; \
	   echo "platform sysconfig distutils pkgutil importlib"; \
	   echo "tkinter turtle"; \
	   echo "builtins __future__"; } | tr ' ' '\n' > /tmp/stdlib_modules.tmp
	@# Выводим те модули, которые есть в imported_modules, но нет в required_packages и не входят в stdlib
	@comm -23 /tmp/imported_modules.tmp /tmp/required_packages.tmp \
		| grep -v -F -f /tmp/stdlib_modules.tmp || true
	@rm -f /tmp/imported_modules.tmp /tmp/required_packages.tmp /tmp/stdlib_modules.tmp