clean_check:
	find . -name "*.txt"
	find . -name "*.log"
	find . -type d -name ".ipynb_checkpoints"

cclean:
	find . -name "*.txt" -delete
	find . -name "*.log" -delete
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +  # {} = "Replace me with found file paths", + = "Batch them up"