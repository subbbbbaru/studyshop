# Необязательная демонстрация GNU Make (Linux/macOS, при установленном make)
.PHONY: test package clean

test:
	python -m pytest -q

package:
	python -m build

clean:
	python -c "import shutil; [shutil.rmtree(p, ignore_errors=True) for p in ['build', 'dist']]"
