from glob import glob
from os.path import join, splitext
from shutil import move

from tqdm import tqdm


class Renamer:
    def __init__(
        self,
        in_root: str,
        out_root: str,
        prefix: str = "",
        starts: int = 0,
        digits: int = 0,
        delimiter: str = "_",
    ):
        self._in_root = in_root
        self._out_root = out_root
        self._prefix = prefix
        self._starts = starts
        self._digits = digits
        self._delimiter = delimiter

    def rename(self):
        paths = sorted(glob(join(self._in_root, "*")))

        if self._digits == 0:
            self._digits = len(str(len(paths)))

        for num, path in tqdm(enumerate(paths)):
            _, ext = splitext(path)
            output_name = "{}{}{:{}d}{}".format(
                self._prefix, self._delimiter, num, self._digits, ext
            )
            move(path, join(self._out_root, output_name))
