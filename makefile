dev:
	# Para encerrar o loop, tecle ^C e vá com mouse até a janela
	while true; do \
		python . ; \
		echo "Recarregando..."; \
	done

install:
	python -m venv venv && \
	source venv/bin/activate.fish && \
	pip install -r requirements.txt

run:
	source venv/bin/activate.fish && \
	python .

lint:
	blue algorithms/ libs/ __main__.py
	isort algorithms/ libs/ __main__.py

