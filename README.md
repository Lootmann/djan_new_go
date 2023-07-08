# Django MEMO

## Overview

Memorize English Words

## Model

```python
class Word:
    spell = CharField()
    meaning = CharField()
    

class Example:
    word = ForeignKey()
    sentence = Textarea()
    translation = Textarea()
```
