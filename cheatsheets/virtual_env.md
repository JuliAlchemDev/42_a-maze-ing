# Create and Configure Virtual Environment for Project

1. Create the environment in the working folder `python3 -m venv .venv `

2. Activate the env `source .venv/bin/activate`
```bash
# (.venv) should appear before command line
(.venv) a_maze_ing $ pwd
.../a_maze_ing
```

3. Check the env works correctly
```bash
which python
python --version
which pip

# python and pip should point to the project's .venv, e.g.
./.venv/bin/python
```

4. Check installed packages `python -m pip list`
```bash
# Starting point:
Package Version
------- -------
pip     25.1.1
```

5. Install project dependencies/tools `python -m pip install mypy flake8`
```bash
# After installation:
$ python -m pip list
Package           Version
----------------- -------
flake8            7.3.0
mypy              2.3.1
pip               25.1.1
etc ...
```

6. Verify that the installed tools belong to this environment
`which mypy` &  which `flake8`
```bash
.../.venv/bin/mypy
.../.venv/bin/flake8
```

7. Flake8 config
```bash
# create `.flake8` in root folder to exclude .venv checking
[flake8]
exclude = .venv
```

8. Mypy config

```bash
# create `pyproject.toml` in root folder to exclude .venv checking & use Strict Mode
[tool.mypy]
strict = true
exclude = '^\.venv/'
```

# Configure Error Lens to use Mypy & Flake8
1. Select Python Interpreter
> `Cmd + Shift + P` -> Python: Select Interpreter
2. Select .venv
> mod2/.venv/bin/python


<!-- Check all VSCode extensions -->
`code --list-extensions`
