SHELL=/bin/bash
.DEFAULT_GOAL := help

help: ## Show this help.
	@grep -E '^[a-zA-Z0-9 -]+:.*#'  Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

pip-install: ## Install python dependencies
	pip install -r requirements.txt

flask-api: ## Run extended SBB API in Flask; port 5000 must be open!
	flask --app extended_api run


