import pytest
from src.vltava import DocumentProcessor


@pytest.mark.parametrize(
    "doc, tokenize, expected",
    [
        ("ahoj, to je Test. nejlepší", True, ["test", "dobry"]),
        ("<div>ahoj, to máš 22342442 xaaa</div> Piva", False, "xaaa pivo")
    ]
)
def test_process(doc, tokenize, expected):

    assert DocumentProcessor().process(doc, tokenize) == expected


def test_process_from_iterable():

    docs = ["dnes test dokumenty ... piva 1", "89 počítače"] * 10
    expected = [['test', 'dokument', 'pivo'], ["pocitace"]] * 10

    result = DocumentProcessor().process_from_iterable(docs, n_jobs=2)
    assert result == expected


def test_raise_exception_if_unknown_backend():
    with pytest.raises(ValueError):
        DocumentProcessor(backend="test")
