# LeetCode Stats Updater

This Python script fetches a user's LeetCode statistics and updates a LaTeX file (cv.tex) with the latest problem-solving statistics. The script extracts relevant difficulty-level statistics and updates the cv.tex file dynamically.

# Features

- Fetches problem statistics from LeetCode using GraphQL.

- Extracts difficulty-based submission stats.

- Updates a LaTeX file (cv.tex) with the latest statistics. (very poor implementation)

- Handles JSON parsing and data extraction efficiently.

# Requirements

`Python 3.x`

`requests module`

# Installation

Clone the repository:
```
git clone https://github.com/woqwoq/leetcode-cv-updater.git
cd leetcode-stats-updater
```

# Usage
Your LaTeX CV should have a section similar to:
```
All: \hspace{1cm}{93/3496 (Beats 80.69\%)}\\
Easy: \hspace{3.05cm}{58/868 (Beats 80.69\%)}\\
Medium: \hspace{2.45cm}{33/1816 (Beats 80.69\%)}\\
Hard: \hspace{2.9cm}{2/812 (Beats 80.69\%)}\\
```

Modify `config.ini` to match values of your own 
```
LEETCODE_USERNAME=cim8848
CV_FILENAME=cv.tex
```
Run `python3 main.py`


# TODO
- Rework the update process of the CV.
