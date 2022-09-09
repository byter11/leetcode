# leetcode
## Get questions
```
# Get questions from LeetCode API
curl https://leetcode.com/api/problems/all/ | jq '[.stat_status_pairs | .[] | select(.paid_only == false)]' > questions.json

# Generate Markdown files with links and a notes section
cat questions.json | jq -r '.[] | select(.difficulty.level == 1) | "### [\(.stat.question__title)](https://leetcode.com/problems/\(.stat.question__title_slug))\n<details>\n<summary>Notes</summary>\n</details>"' > easy.md

cat questions.json | jq -r '.[] | select(.difficulty.level == 2) | "### [\(.stat.question__title)](https://leetcode.com/problems/\(.stat.question__title_slug))\n<details>\n<summary>Notes</summary>\n</details>"' > medium.md

cat questions.json | jq -r '.[] | select(.difficulty.level == 3) | "### [\(.stat.question__title)](https://leetcode.com/problems/\(.stat.question__title_slug))\n<details>\n<summary>Notes</summary>\n</details>"' > hard.md
```

## Links
* [Easy](easy.md)
* [Medium](medium.md)
* [Hard](hard.md)
