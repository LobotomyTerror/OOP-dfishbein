for file in data/*.in; do
    cat "$file" | python morsecodepalindrome.py | diff - "${file%.in}.ans"
done
echo "run complete"