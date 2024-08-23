# Code academy
This is my project that was created through SQL,
and is transferred to Python\
through SQLAlchemy.

Before using commands, it is strongly
recommended to make help on them.

# Commands:

## help:
```bash
python -m academy.main --help
```

## prefill:
```bash
python -m academy.main --prefill
```

## add new staff(it's just example, you can change the values):
```bash
python -m academy.main --new-staff 'Employee' 23 'Male' 'Manager' 'employee@mail.ru' '20/02/2001' '03/02/2020' 20
```

## add/edit [new] requirement for stuff(it's just example, you can change the values):
```bash
python -m academy.main --staff-requirements 2 '13:00 - 20:00' 'Monday, Tuesday' 'Russian'
```

## add new teacher(it's just example, you can change the values):
```bash
python -m academy.main --new-teacher 'Teacher1' 345 'Female' '21/05/1679' 3 245 'pretends to work'
```

##  add/edit [new] requirement for teacher(it's just example, you can change the values):
```bash
python -m academy.main --teacher-requirements 2 'Sunday' '14:00 - 23:00' 'Russian' 10
```

##  add/edit [new] student for teacher(it's just example, you can change the values):
```bash
python -m academy.main --add-student 'Nick Morozov' 15 'Python' 1
```
