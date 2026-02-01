<p align="center">
  <h1 align="center">AgnBlue Vyākaraṇa</h1>
  <p align="center"><strong>व्याकरणम् इव कोडः</strong> — Code as Grammar</p>
  <p align="center">
    <a href="https://github.com/twomathematicians-code/agnblue-vyakarana/actions"><img src="https://github.com/twomathematicians-code/agnblue-vyakarana/workflows/Vyākaraṇa%20CI%20—%20Ṣaḍvidha-Pariśuddhi/badge.svg" alt="CI Status"></a>
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
    <a href="#"><img src="https://img.shields.io/badge/Python-3.10%2B-blue.svg" alt="Python"></a>
  </p>
</p>

---

## 🕉️ What is This?

AgnBlue Vyākaraṇa is the first programming language based on **Pāṇinian Sanskrit grammar** (Aṣṭādhyāyī, ~500 BCE). 

Instead of classes and functions, you write **Dhātus** (roots), **Kārakas** (grammatical roles), and **Vākyas** (sentences). The compiler translates your English-syntax blueprint into Sanskrit structural logic.

```agnblue
// Example: A Todo in AgnBlue
blueprint TodoApp { version: "0.1.0" }

root Create { 
    gana: 8           // Transitivity class
    visibility: public // Udātta - high pitch
}

entity Todo {
    @public title: String       // Externally visible
    @private id: UUID           // Submerged (Anudatta)
    @immutable created: DateTime // Sealed forever (Samvrita)
    
    action create implements Create {
        perform User as kartri      // Agent (Nominative)
        receive Todo as karman      // Object (Accusative)
        send Database as sampradana // Recipient (Dative)
    }
}
