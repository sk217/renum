from os import listdir

from renum._renamer import Renamer


class TestRenamer:
    @staticmethod
    def _prepare(tmpdir):
        with open(tmpdir.join("file1.jpg"), "w") as f:
            f.write("a")
        with open(tmpdir.join("file2.jpg"), "w") as f:
            f.write("b")
        with open(tmpdir.join("file3.jpg"), "w") as f:
            f.write("c")

    def test_rename(self, tmpdir):
        self._prepare(tmpdir)

        renamer = Renamer(
            in_root=tmpdir,
            out_root=tmpdir,
            prefix="prefix",
            starts=0,
            digits=0,
            delimiter="_",
        )
        renamer.rename()

        assert sorted(listdir(tmpdir)) == [
            "prefix_0.jpg",
            "prefix_1.jpg",
            "prefix_2.jpg",
        ]
