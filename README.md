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


## page(example of work):

default state = 1, you can change the number, but if there are no lines for this number, you will crash with an can \
only be used to view the latest 'entity'


```bash
python -m academy.main --students --page 2
```

## see latest teachers:
```bash
python -m academy.main --teachers
```
## see latest students:
```bash
python -m academy.main --students
```
## see latest staff:
```bash
python -m academy.main --staff
```
## see latest staff preferences and responsibilities:
```bash
python -m academy.main --staff-preferences
```
## see latest teachers preferences and responsibilities:
```bash
python -m academy.main --teacher-preferences
```
## reset database:
```bash
python -m academy.main --reset
```

# The commands below do not work as we want if the prefill is executed:

## add new staff(it's just example, you can change the values):
```bash
python -m academy.main --new-staff 'Employee' 23 'Male' 'Manager' 'employee@mail.ru' '20/02/2001' '03/02/2020' 20
```

## add/edit [new] requirement for stuff(it's just example, you can change the values):
```bash
python -m academy.main --staff-requirements 1 '13:00 - 20:00' 'Monday, Tuesday' 'Russian'
```

## add new teacher(it's just example, you can change the values):
```bash
python -m academy.main --new-teacher 'Teacher1' 345 'Female' '21/05/1679' 3 245 'pretends to work' 'Python'
```

##  add/edit [new] requirement for teacher(it's just example, you can change the values):
```bash
python -m academy.main --teacher-requirements 1 'Sunday' '14:00 - 23:00' 'Russian' 10
```

##  add/edit [new] student for teacher(it's just example, you can change the values):
```bash
python -m academy.main --add-student 'Nick Morozov' 15 'Python' 1
```
