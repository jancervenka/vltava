import pytest
from src.vltava import _MajkaAnalyzer, _MorphoditaAnalyzer


@pytest.mark.parametrize(
    "analyzer_class, raw_word, expected",
    [
        (_MajkaAnalyzer, "nejlepsi", "dobrý"),
        (_MajkaAnalyzer, "xxxzzz", "xxxzzz"),
        (_MorphoditaAnalyzer, "nejlepsi", "dobrý"),
        (_MorphoditaAnalyzer, "zzz123", "zzz123"),
    ],
)
def test_get_lemma(analyzer_class, raw_word, expected):
    assert analyzer_class().get_lemma(raw_word) == expected
