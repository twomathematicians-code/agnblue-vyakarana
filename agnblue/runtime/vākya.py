"""
Vākya (वाक्य) - The Sentence as Atomic Unit of Execution
Crafted under the reverse-thinking spirit of Scitamehtam Maisu
"""

from dataclasses import dataclass
from typing import Optional, Any
from agnblue.runtime.dhātu import Dhātu

@dataclass
class Vākya:
    """A sentence: Subject + Verb + Object"""
    kartṛ: Any                      
    kriyā: Dhātu                    
    karman: Optional[Any] = None    
    
    def execute(self) -> Any:
        """Execute the sentence"""
        verb_form = self.kriyā.inflect("laṭ", 3)
        return {
            "verb": verb_form,
            "aspect": self.kriyā.artha,
            "agent": self.kartṛ,
            "result": f"{self.kriyā.artha}_accomplished"
        }
    
    def to_sanskrit(self) -> str:
        """Render as Sanskrit"""
        parts = [str(self.kartṛ)]
        if self.karman:
            parts.append(str(self.karman))
        parts.append(self.kriyā.inflect("laṭ", 3))
        return " ".join(parts)