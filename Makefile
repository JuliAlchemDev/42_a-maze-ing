NAME = a_maze_ing.py
CONFIG = config.txt
VENV = .venv
VENV_BIN  = $(VENV)/bin

# --- Colors & Styles ---
# rgb(110, 128, 156)
PRIMARY = \033[38;2;110;128;156m
# rgb(80, 215, 245)
SUCCESS = \033[38;2;80;215;245m
# rgb(235, 105, 120)
ERROR   = \033[38;2;235;105;120m
# rgb(200, 110, 220)
LINT    = \033[38;2;200;110;220m
# rgb(205, 212, 228)
HINT = \033[38;2;205;212;228m

BOLD = \033[1m
RESET   = \033[0m

install:
	@ if [ ! -d $(VENV) ]; then \
		printf "$(PRIMARY)Setting up virtual environment...$(RESET)\n"; \
		python3 -m venv $(VENV); \
		$(VENV_BIN)/python3 -m pip -q install --upgrade pip; \
	fi
	@ printf "$(PRIMARY)Syncing dependencies...$(RESET)\n"
	@ $(VENV_BIN)/pip -q install -r requirements.txt
	@ printf "$(SUCCESS)Workshop ready. Time to build mazes!$(RESET)\n"
	@ printf "$(HINT)Run \"make run\" to start.$(RESET)\n"

check-venv:
	@ if [ ! -d $(VENV) ]; then \
		printf "$(ERROR)Virtual environment not found.$(RESET)\n";\
		printf "$(HINT)==========================$(RESET)\n"; \
		printf "$(HINT)Run \"make install\" first.$(RESET)\n"; \
		printf "$(HINT)==========================$(RESET)\n"; \
		exit 1; \
	fi

run: check-venv
	@ $(VENV_BIN)/python3 $(NAME) $(CONFIG)

debug: check-venv
	@ printf "$(LINT)========================$(RESET)\n"
	@ printf "$(LINT)Starting debug mode...$(RESET)"
	@ printf "\n$(LINT)========================$(RESET)\n\n"
	@ $(VENV_BIN)/python3 -m pdb $(NAME) $(CONFIG)


clean:
	@ printf "$(PRIMARY)Removing all cache files...$(RESET)\n"
	@ find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
	@ find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null
	@ printf "$(SUCCESS)Cleaning done.$(RESET)\n"

lint: check-venv
	@ printf "$(LINT)============================$(RESET)\n"
	@ printf "$(LINT)Checking Mypy and Flake8...$(RESET)"
	@ printf "\n$(LINT)============================$(RESET)\n\n"
	@ if $(VENV_BIN)/mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs \
		&& $(VENV_BIN)/flake8 . ; then \
		printf "\n$(SUCCESS)======== All checks passed ========$(RESET)\n"; \
	else \
		printf "\n$(ERROR)======== Errors found ========$(RESET)\n"; \
	fi

lint-strict: check-venv
	@ printf "$(LINT)================================================$(RESET)\n"
	@ printf "$(LINT)Checking Mypy $(BOLD)STRICT$(RESET)$(LINT) and Flake8 $(BOLD)VERBOSE$(RESET)$(LINT) modes...$(RESET)"
	@ printf "\n$(LINT)================================================$(RESET)\n\n"
	@ if $(VENV_BIN)/mypy . --strict \
		&& $(VENV_BIN)/flake8 . -v ; then \
		printf "\n$(SUCCESS)=============== All checks passed ===============$(RESET)\n"; \
	else \
		printf "\n$(ERROR)================= Errors found ==================$(RESET)\n"; \
	fi

fclean:
	@ printf "$(PRIMARY)Removing all cache files...$(RESET)\n"
	@ find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
	@ find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null
	@ printf "$(PRIMARY)Removing virtual environment...$(RESET)\n"
	@ rm -rf $(VENV)
	@ printf "$(SUCCESS)Full clean done.$(RESET)\n"

re: fclean install

.PHONY: install run check-venv debug lint lint-strict clean fclean re
