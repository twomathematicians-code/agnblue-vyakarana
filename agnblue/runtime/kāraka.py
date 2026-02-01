"""
Kāraka (कारक) - Dependency Injection through Grammatical Roles
Crafted under the reverse-thinking spirit of Scitamehtam Maisu
"""

from dataclasses import dataclass
from typing import Any

class KārakaType:
    """The six factors of action"""
    KARTṚ = ("nominative", "agent")
    KARMAN = ("accusative", "object")
    KARAṆA = ("instrumental", "instrument")
    SAMPRADĀNA = ("dative", "recipient")
    APĀDĀNA = ("ablative", "source")
    ADHIKARAṆA = ("locative", "location")

@dataclass
class Kāraka:
    role: KārakaType
    value: Any
    required: bool = True

class GrammarError(Exception):
    pass