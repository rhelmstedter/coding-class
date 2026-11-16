from casing import (lowercase_autobot,
                    uppercase_decepticon,
                    titlecase_transformers)


def test_strings():
    assert lowercase_autobot == "optimus"
    assert uppercase_decepticon == "MEGATRON"
    assert titlecase_transformers == "Robots In Disguise"
