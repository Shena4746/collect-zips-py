# Command line tool to collect and rename zip files

A command line tool to rename zip files to their parent directory name and copy (or move) them to other directory.

## Usage

Suppose zip files are placed like this.

```txt
./sample/
└── dirs
    ├── dir1
    │   └── hoge.zip
    └── dir2
        └── fuga.zip
```

In order to copy these zips to sample directory with renaming them, run the following

```bash
python /path/to/colzips.py ./sample/dirs/ -d ./sample/
```

to get

```txt
./sample/
├── dir1.zip
├── dir2.zip
└── dirs
    ├── dir1
    │   └── hoge.zip
    └── dir2
        └── fuga.zip
```

The same result can be derived by running

```bash
python /path/to/colzips.py ./sample/ -d ./sample/
```

since it searches files recursively.

If you would like to move zip files instead of copying them, simply add `-m` option. For more (nothing much) information, run

```bash
python /path/to/colzips.py --help
```

## Install

The script depends only on standard libraries and click library. The following step can be skipped if you have these libraries with appropriate versions in your environment (see pyproject.toml).

- Tested Environment
  - Windows 10 + WSL2 + Ubuntu 20.04
  - python 3.10.5 (pyenv 2.3.2) + poetry (1.1.11)

Follow a typical routine of setting up a virtual environment by pyenv + poetry.

Copy this project in some way, for instance, by git clone or create a repository from this template project.

```bash
git clone https://github.com/Shena4746/collect-zips-py.git
cd ./collect-zips-py
```

Enable python 3.10.5 at the top of the project directory. We do it simply by pyenv here.

```bash
pyenv local 3.10.5
```

It fails if you have not downloaded python 3.10.5. Run the following to download it, and try the previous command again.

```bash
pyenv install 3.10.5
```

Locate the python interpreter at {project-top}/.venv. Then let poetry perform a local installation of dependency.

```bash
python3 -m venv .venv
poetry install
```

Make sure that poetry uses the intended python interpreter.

```bash
poetry run which python
poetry run python --version
```
