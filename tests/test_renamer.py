import os
from os import listdir

from renum._renamer import Renamer


class TestRenamer:
    @staticmethod
    def _prepare(tmpdir):
        os.mkdir(tmpdir.join("dir-a"))
        os.mkdir(tmpdir.join("dir-b"))
        os.mkdir(tmpdir.join("dir-c"))

        with open(tmpdir.join("file_a.jpg"), "w") as f:
            f.write("a")
        with open(tmpdir.join("file_b.jpg"), "w") as f:
            f.write("b")
        with open(tmpdir.join("file_c.jpg"), "w") as f:
            f.write("c")

    def test_rename1(self, tmpdir):
        self._prepare(tmpdir)

        renamer = Renamer(
            in_root=tmpdir,
            out_root=tmpdir,
            prefix="prefix",
            starts=0,
            digits=0,
            delimiter="_",
            restriction=None,
        )
        renamer.rename()

        assert sorted(listdir(tmpdir)) == [
            "prefix_0",
            "prefix_1",
            "prefix_2",
            "prefix_3.jpg",
            "prefix_4.jpg",
            "prefix_5.jpg",
        ]

    def test_rename2(self, tmpdir):
        self._prepare(tmpdir)

        renamer = Renamer(
            in_root=tmpdir,
            out_root=tmpdir,
            prefix="prefix",
            starts=0,
            digits=0,
            delimiter="_",
            restriction="dir",
        )
        renamer.rename()

        assert sorted(listdir(tmpdir)) == [
            "file_a.jpg",
            "file_b.jpg",
            "file_c.jpg",
            "prefix_0",
            "prefix_1",
            "prefix_2",
        ]

    def test_rename3(self, tmpdir):
        self._prepare(tmpdir)

        renamer = Renamer(
            in_root=tmpdir,
            out_root=tmpdir,
            prefix="prefix",
            starts=0,
            digits=0,
            delimiter="_",
            restriction="file",
        )
        renamer.rename()

        assert sorted(listdir(tmpdir)) == [
            "dir-a",
            "dir-b",
            "dir-c",
            "prefix_0.jpg",
            "prefix_1.jpg",
            "prefix_2.jpg",
        ]
