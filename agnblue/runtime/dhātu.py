"""
Dhātu (धातु) - Root Capability System
The atomic units of computation in AgnBlue.

Crafted under the reverse-thinking spirit of Scitamehtam Maisu
"""

from dataclasses import dataclass
from typing import Optional
from enum import Enum

class Svara(Enum):
    """Pitch accent determines visibility"""
    UDATTA = ("high", "public")      
    ANUDATTA = ("low", "private")    
    SVARITA = ("mixed", "protected") 
    SAMVRITA = ("closed", "final")   

class Liṅga(Enum):
    """Gender determines behavior"""
    PUM = "masculine"      
    STRĪ = "feminine"      
    NAPUMSAKA = "neutral"  

class Gaṇa(Enum):
    """Verb class determines transitivity"""
    BHVADI = 1      
    TANADI = 8      

@dataclass(frozen=True)
class Dhātu:
    """Root of action"""
    phoneme: str                   
    gaṇa: Gaṇa                      
    artha: str                      
    svara: Svara = Svara.UDATTA    
    
    def inflect(self, lakara: str, purusha: int = 3) -> str:
        """Make verb form"""
        return f"{self.phoneme}ti"

@dataclass
class Prātipadika:
    """Noun stem"""
    stem: str
    dhātu: Dhātu
    pratyaya: str                   
    liṅga: Liṅga
    
    def decline(self, vibhakti: int):
        """Add case ending"""
        return f"{self.stem}ḥ"

@dataclass(frozen=True)
class Subanta:
    """Complete word"""
    word: str
    stem: Prātipadika
    vibhakti: int           
    karaka: str = "unknown"
    
    @property
    def access_modifier(self) -> str:
        """Map Svara to visibility"""
        svara_map = {
            Svara.UDATTA: "public",
            Svara.ANUDATTA: "private",
            Svara.SVARITA: "protected",
            Svara.SAMVRITA: "readonly"
        }
        return svara_map.get(self.stem.svara, "public")