.PHONY: calculate-code-complexity calculate-churn freeze-dependencies
.SILENT: calculate-code-complexity calculate-churn

calculate-code-complexity:
	radon cc -na -i venv -e "*_test.py" -j -O radon-cc-output.json .
	python ./calculate_code_complexity.py
	rm radon-cc-output.json

calculate-churn:
	git log --format=format: --name-only --since=12.month \
	| egrep -v "^$" \
	| egrep ".py$" \
	| egrep -v "*_test.py$" \
	| egrep -v "^__init__.py$" \
	| sort \
	| uniq -c \
	| sort -nr \
	| head -50 \
	| grep -E '[a-zA-Z_\/]*.py' -o \
	> churn.list

identify-hotspots:
	make calculate-code-complexity
	make calculate-churn
	python ./generate_graph.py

freeze-dependencies:
	pip freeze > requirements.txt
