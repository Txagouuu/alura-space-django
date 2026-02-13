# Fix Django ModelForm Error Plan

## Problem
ValueError: ModelForm has no model class specified at /nova-imagem/

## Root Causes
1. In `apps/galeria/forms.py`: The class is named `meta` (lowercase), but Django expects `Meta` (uppercase)
2. In `apps/galeria/views.py`: Form is not instantiated - `form = FotografiaForms` should be `form = FotografiaForms()`
3. Additional typos in forms.py: `wigets` should be `widgets`, and DateTimeInput syntax issues

## Tasks
- [x] Fix `apps/galeria/forms.py`:
  - [x] Change `class meta:` to `class Meta:`
  - [x] Fix typo `wigets` to `widgets`
  - [x] Fix DateTimeInput syntax (`type: 'date'` → `'type': 'date'`)
- [x] Fix `apps/galeria/views.py`:
  - [x] Change `form = FotografiaForms` to `form = FotografiaForms()`
