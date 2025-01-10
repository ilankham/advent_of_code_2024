[![Python 3.12](https://img.shields.io/badge/python-3.12-brightgreen.svg)](#prerequisites)  [![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

# Advent of Code 2024 Progress

## Getting Started

1. [Clone](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) or [download/unzip](https://github.com/ilankham/advent_of_code_2024/archive/main.zip) this repo.

2. Inside the local clone, create a new directory called `config`.

3. Inside the `config` directory, create a file called `session_id.txt`.
   
4. Log into https://adventofcode.com/ using a web browser, and use [developer tools](https://firefox-source-docs.mozilla.org/devtools-user/storage_inspector/) to copy the value of a cookie named "session" associated with the domain adventofcode.com. (Note: As of this writing, when logged in using a Google account, session id is a 128-digit hexadecimal number.)
   
5. Paste the contents of this cookie into the file `config/session_id.txt`.

6. Install packages specified in [requirements.txt](requirements.txt), e.g., from the command line:
```
pip install -r requirements.txt
```

7. Open the solution for a specific day, e.g., from the command line:
```
jupyter lab day01.ipynb
```

8. For context about a specific problem, see <https://adventofcode.com/2024/>


### Prerequisites

Python 3.12 or greater, preferably running in a virtual environment (or equivalent) with JupyterLab installed.

For example, using the [`uv`](https://github.com/astral-sh/uv) package manager for Python, this environment could be created as follows:
```
uv venv --python 3.12
source .venv/bin/activate
uv pip install jupyterlab
```

### License
All repo contents are licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Notes

### Approach

As a second-time Advent of Code (AoC) participant getting a late start, the goal is to balance pacing with learning. This has led to several conventions:

* To focus more fully on puzzle solving, tooling was created to automate extracting test cases and puzzle input.
  
* To facilitate code reuse, a primative test harness was created, allowing known working cases to be used to test refactored code.

* As a way to learn it better, [`polars`](https://pola.rs) is often used as a data structure.

### Takeaways

[to be added]

## Author
* [ilankham](https://github.com/ilankham)

## Disclaimer

This project is in no way affiliated with [Advent of Code](https://adventofcode.com).
