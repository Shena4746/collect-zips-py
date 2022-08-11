import shutil
from pathlib import Path
from typing import TypeAlias

import click

Paths: TypeAlias = list[Path]


def get_non_unique_parent_dir(files: Paths) -> Paths:
    """return the duplicated named parent directories of input files"""
    dir_ng: Paths = []
    dir_name_pool: list[str] = []
    for f in files:
        dir_f: Path = f.parent
        if dir_f.stem in dir_name_pool and dir_f not in dir_ng:
            dir_ng.append(dir_f)
        dir_name_pool.append(dir_f.stem)
    return dir_ng


def collect_zip(search_from: Path | str, dir_out: Path | str, move: bool = False) -> Paths:
    """collect zip files in sub-directories to dir_out"""
    dir_search_from: Path = Path(search_from)
    if not dir_search_from.exists():
        raise ValueError(f"path does not exist. {search_from}")
    # recursively get zip
    zips: Paths = list(dir_search_from.glob("**/*.zip"))
    # check each file is contained in independent directory
    if (dir_ng := get_non_unique_parent_dir(zips)) != []:
        err_msg: str = "\n".join(
            [
                "zip files are not contained in distinct directories.",
                "NG:",
                "\n".join([str(d) for d in dir_ng]),
            ]
        )
        raise Exception(err_msg)
    # rename zip and move up to dir_out
    new_paths: Paths = []
    dir = Path(dir_out)
    for z in zips:
        new_path: Path = dir / f"{z.parent.stem}.zip"
        shutil.move(z, new_path) if move else shutil.copy2(z, new_path)
        new_paths.append(new_path)
    return new_paths


@click.command()
@click.argument("search_from", nargs=1, type=click.Path(exists=True, file_okay=False))
@click.option(
    "-d",
    "--dirout",
    "dir",
    default=Path.cwd(),
    type=click.Path(file_okay=False),
    help="destination directory for collected zip files. the default uses the current directory.",
)
@click.option(
    "-m",
    "--move",
    "move",
    type=bool,
    is_flag=True,
    default=False,
    help="whether to move zips. the default just copies them to the directory (-d) and keeps the original ones.",
)
def colzip(search_from: str, dir: str, move: bool):
    # print(f"type of from = {type(search_from)}")
    collect_zip(search_from=search_from, dir_out=dir, move=move)


if __name__ == "__main__":
    colzip()
