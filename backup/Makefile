.SILENT:
calculate-code-complexity:
	radon cc -nc -i venv -e "*_test.py" -j -O radon-cc-output.json .
	python ./playgrounds/calculate_complexity_playground.py
	rm radon-cc-output.json

.SILENT:
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
	python ./playgrounds/generate_graph.py
