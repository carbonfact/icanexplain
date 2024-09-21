execute-notebooks:
	poetry run jupyter nbconvert --execute --to notebook --inplace docs/*.ipynb
	poetry run jupyter nbconvert --execute --to notebook --inplace docs/examples/*.ipynb
	poetry run jupyter nbconvert --execute --to notebook --inplace docs/methods/*.ipynb

render-notebooks:
	poetry run jupyter nbconvert --to markdown docs/*.ipynb
	poetry run jupyter nbconvert --to markdown docs/examples/*.ipynb
	poetry run jupyter nbconvert --to markdown docs/methods/*.ipynb

docs: execute-notebooks render-notebooks
	poetry run mkdocs serve
