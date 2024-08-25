from academy.datamodel.students import Students
from academy.db_utilities.session import AcademySession


def prefill_students():
    with AcademySession.get_session() as session:
        students_data = [
            Students(
                name='Emily Davis',
                age=22,
                subject='Python',
                teacher_id=1
            ),
            Students(
                name='Michael Rodriguez',
                age=17,
                subject='Python',
                teacher_id=1
            ),
            Students(
                name='Olivia Thompson',
                age=15,
                subject='Python',
                teacher_id=1
            ),
            Students(
                name='Matthew Johnson',
                age=13,
                subject='Python',
                teacher_id=1
            ),
            Students(
                name='Sophia Martinez',
                age=34,
                subject='Python',
                teacher_id=1
            ),
            Students(
                name='William Brown',
                age=28,
                subject='Python',
                teacher_id=1
            ),
            Students(
                name='Ava Wilson',
                age=21,
                subject='Python',
                teacher_id=1
            ),
            Students(
                name='James King',
                age=41,
                subject='C++',
                teacher_id=2
            ),
            Students(
                name='Charlotte Lewis',
                age=14,
                subject='C++',
                teacher_id=2
            ),
            Students(
                name='Charles Mitchell',
                age=24,
                subject='C++',
                teacher_id=2
            ),
            Students(
                name='Amelia Robinson',
                age=23,
                subject='C++',
                teacher_id=2
            ),
            Students(
                name='Thomas Walker',
                age=11,
                subject='C++',
                teacher_id=2
            ),
            Students(
                name='Harper Young',
                age=26,
                subject='C++',
                teacher_id=2
            ),
            Students(
                name='Samuel Jobs',
                age=31,
                subject='Java',
                teacher_id=3
            ),
            Students(
                name='Madison Zaicev',
                age=32,
                subject='Java',
                teacher_id=3
            ),
            Students(
                name='Christopher',
                age=14,
                subject='Java',
                teacher_id=3
            ),
            Students(
                name='Avery Baker',
                age=27,
                subject='Java',
                teacher_id=3
            ),
            Students(
                name='Andrew Turner',
                age=29,
                subject='Java',
                teacher_id=3
            ),
            Students(
                name='Victoria Phillips',
                age=21,
                subject='Java',
                teacher_id=3
            ),
            Students(
                name='Joshua Parker',
                age=39,
                subject='Java',
                teacher_id=3
            ),
            Students(
                name='Lily Evans',
                age=16,
                subject='Java',
                teacher_id=3
            ),
            Students(
                name='Olivia Johnson',
                age=29,
                subject='DevOps',
                teacher_id=4
            ),
            Students(
                name='Daniel Scott',
                age=35,
                subject='DevOps',
                teacher_id=4
            ),
            Students(
                name='Abigail White',
                age=22,
                subject='DevOps',
                teacher_id=4
            ),
            Students(
                name='Samuel Hall',
                age=45,
                subject='DevOps',
                teacher_id=4
            ),
            Students(
                name='Madison Green',
                age=37,
                subject='DevOps',
                teacher_id=4
            ),
            Students(
                name='Christopher Adams',
                age=27,
                subject='DevOps',
                teacher_id=4
            ),
            Students(
                name='Anna Baker',
                age=41,
                subject='DevOps',
                teacher_id=4
            ),
            Students(
                name='Andrey Turner',
                age=55,
                subject='DevOps',
                teacher_id=4
            ),
            Students(
                name='Victoria Secret',
                age=32,
                subject='DevOps',
                teacher_id=4
            ),
            Students(
                name='Laura Smith',
                age=34,
                subject='SQL professional',
                teacher_id=5
            ),
            Students(
                name='Michael Lee',
                age=46,
                subject='SQL professional',
                teacher_id=5
            ),
            Students(
                name='Sarah Johnson',
                age=28,
                subject='SQL professional',
                teacher_id=5
            ),
            Students(
                name='David Williams',
                age=52,
                subject='SQL professional',
                teacher_id=5
            ),
            Students(
                name='James Kings',
                age=26,
                subject='Game/Web Design',
                teacher_id=6
            ),
            Students(
                name='Charlotte Lewi',
                age=33,
                subject='Game/Web Design',
                teacher_id=6
            ),
            Students(
                name='Charlie Mitchell',
                age=42,
                subject='Game/Web Design, PHP',
                teacher_id=6
            ),
            Students(
                name='Amelia Kolumb',
                age=29,
                subject='PHP',
                teacher_id=6
            ),
            Students(
                name='Thomas Walkers',
                age=37,
                subject='PHP',
                teacher_id=6
            ),
            Students(
                name='Sophia Martini',
                age=22,
                subject='Python',
                teacher_id=7
            ),
            Students(
                name='William Browns',
                age=33,
                subject='Python',
                teacher_id=7
            ),
            Students(
                name='Anna Wilson',
                age=27,
                subject='Python',
                teacher_id=7
            ),
            Students(
                name='James Taylor',
                age=31,
                subject='Python',
                teacher_id=7
            ),
            Students(
                name='Isabella Moore',
                age=25,
                subject='Python',
                teacher_id=7
            ),
            Students(
                name='Robert Anderson',
                age=30,
                subject='Python',
                teacher_id=7
            ),
            Students(
                name='Mia Clark',
                age=28,
                subject='Python',
                teacher_id=7
            ),
            Students(
                name='Ethan Thompson',
                age=25,
                subject='CSS',
                teacher_id=8
            ),
            Students(
                name='Emma White',
                age=32,
                subject='CSS',
                teacher_id=8
            ),
            Students(
                name='Liam Davis',
                age=28,
                subject='CSS',
                teacher_id=8
            ),
            Students(
                name='Oliver Martinez',
                age=36,
                subject='CSS',
                teacher_id=8
            ),
            Students(
                name='Ava Garcia',
                age=24,
                subject='CSS',
                teacher_id=8
            ),
            Students(
                name='Mason Wilson',
                age=29,
                subject='Swift',
                teacher_id=8
            ),
            Students(
                name='Aria Clark',
                age=31,
                subject='Swift',
                teacher_id=8
            ),
            Students(
                name='Elijah Lewis',
                age=37,
                subject='Swift',
                teacher_id=8
            ),
            Students(
                name='Chloe Robinson',
                age=33,
                subject='Swift',
                teacher_id=8
            )
        ]
        session.add_all(students_data)
        session.commit()
