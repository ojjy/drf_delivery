find . -name "__pycache__" -exec  rm -rf {} +
find . -name "0*" -exec rm -rf {} +
rm -rf db.sqlite3