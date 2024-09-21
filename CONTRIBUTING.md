# Contributing

```sh
# Prepare virtual environment
git clone https://github.com/carbonfact/icanexplain
cd icanexplain
poetry install
poetry shell

# Install pre-commit hooks
pre-commit install --hook-type pre-push
pre-commit run --all-files

# Run tests
pytest

# Serve docs locally
make docs
```
