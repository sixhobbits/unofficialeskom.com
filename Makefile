site/:	docs/jobs.md
	mkdocs build

docs/jobs.md: jobs.txt
	python3 scripts/jobs_to_md.py

jobs.txt:
	scripts/get_jobs.sh

.PHONY : clean
clean:
	rm jobs.txt

