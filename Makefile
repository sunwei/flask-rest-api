env     ?= develop

install:
	pip install virtualenv && \
	virtualenv -p `which python3` venv && \
	source venv/bin/activate && \
	pip install -r requirements.txt && \
	python setup.py $(env)

run:
	source venv/bin/activate && \
	python visitor_experience/app.py

clean:
	rm -rf venv