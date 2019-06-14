all:
	@find . -name "*.pyc" -type f -print0 | xargs -0 /bin/rm -f
	@find . -name "__pycache__" -print0 | xargs -0 /bin/rm -rf