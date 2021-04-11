.PHONY: run-radon-analysis calculate-churn freeze-dependencies identify-hotspots
.SILENT: run-radon-analysis calculate-churn identify-hotspots

run-radon-analysis:
	radon cc -na -i venv -i .env -i migrations -e "*_test.py" -j -O radon-cc-output.json $(path)

calculate-churn:
	git --git-dir $(path)/.git log --format=format: --name-only --since=12.month \
	| egrep -v "^$$" \
	| egrep ".py$$" \
	| egrep -v "*_test.py$$" \
	| egrep -v "^__init__.py$$" \
	| sort \
	| uniq -c \
	| sort -nr \
	| head -50 \
	> churn.list

identify-hotspots:
	make run-radon-analysis path=$(path)
	make calculate-churn path=$(path)
	python ./generate_graph.py


freeze-dependencies:
	pip freeze > requirements.txt
