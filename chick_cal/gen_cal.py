from datetime import timedelta
from typing import Optional, List, overload
from enum import Enum

import arrow
from ics import Calendar, Event
from ics.alarm.base import BaseAlarm
from ics.alarm import DisplayAlarm

CLASS_TYPES = {0: "Workshop", 1: "01 Lecture", 2: "02 Tutorial"}
TZ = "Asia/Singapore"
SEM_PREFIX = r"CU_TRI323_FT"


class ClassType(Enum):
    WORKSHOP = "0"
    LEC = "01 Lecture"
    TUT = "02 Tutorial"


def gen_name(code: str, idx: int, ct: ClassType) -> str:
    PREFIX = f"{SEM_PREFIX}_{code}_S{idx:02}_"
    if ct == ClassType.LEC:
        return PREFIX + "Lec/1"
    elif ct == ClassType.TUT:
        if code.startswith("MI"):
            return PREFIX + "Tut_B"
        if code.startswith("ECS2"):
            return PREFIX.rstrip("_") + "A Tut A"
        return PREFIX + "Tut/1"
    else:
        return PREFIX + "Workshop"


@overload
def gen_event(
    name: str,
    desc: str,
    start_time: arrow.Arrow,
    end_time: arrow.Arrow | None = None,
    all_day: bool = False,
    duration: int = 3,
    location: str = "Main Wing",
    class_type: ClassType = ClassType.LEC,
    alarms: Optional[List[BaseAlarm]] = None,
) -> Event:
    ...


@overload
def gen_event(
    name: str,
    desc: str,
    start_time: arrow.Arrow,
    end_time: arrow.Arrow | None = None,
    all_day: bool = False,
    duration: int = 3,
    location: str = "Main Wing",
    class_type: int = 0,
    alarms: Optional[List[BaseAlarm]] = None,
) -> Event:
    ...


def gen_event(
    name: str,
    desc: str,
    start_time: arrow.Arrow,
    end_time: arrow.Arrow | None = None,
    all_day: bool = False,
    duration: int = 3,
    location: str = "Main Wing",
    class_type: ClassType | int = ClassType.LEC,
    alarms: List[BaseAlarm] | None = None,
) -> Event:
    e = Event()
    e.name = name
    e.begin = start_time
    if not all_day:
        e.duration = timedelta(hours=duration)
    else:
        e.make_all_day()
        # e.all_day = True

    if end_time:
        e.end = end_time

    if isinstance(class_type, ClassType):
        e.description = desc + "\n" + class_type.value
    else:
        e.description = desc + "\n" + CLASS_TYPES.get(class_type, "")
    e.location = location
    e.url = "https://www.psb-academy.edu.sg/wordpress/wp-content/uploads/2020/11/Tri-223-CU_FTBArts-BM-223_Term-1-Timetable.pdf"
    e.alarms = (
        alarms if alarms is not None else [DisplayAlarm(trigger=timedelta(hours=-1))]
    )
    return e


def gen_mi(c: Calendar):
    CODE, l, START_DATE = (
        "MI(2007MK)",
        "Frank Boey Chong King",
        arrow.get(2023, 7, 24, tzinfo="Asia/Singapore").replace(hour=15, minute=30),
    )

    c.events.add(
        gen_event(
            name=gen_name(CODE, 1, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=25),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 2, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=1, month=8),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 3, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=8, month=8),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 4, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=14, month=8, hour=12, minute=0),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 5, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=15, month=8),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 6, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=21, month=8, hour=12, minute=0),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 7, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=22, month=8),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 8, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=29, month=8),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 9, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=5, month=9),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 10, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=12, month=9),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 11, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=19, month=9),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 12, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=26, month=9),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 13, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=3, month=10),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 14, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=10, month=10),
            class_type=1,
        )
    )
    return c


def gen_mlm(c: Calendar) -> Calendar:
    CODE, l, START_DATE = (
        "MLM(2000HR)",
        "Salitha Nair",
        arrow.get(2023, 7, 28, tzinfo="Asia/Singapore").replace(hour=12),
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 1, ClassType.LEC),
            desc=l,
            start_time=START_DATE,
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 2, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=2, month=8),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 3, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=11, month=8),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 4, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=16, month=8, hour=12, minute=0),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 5, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=23, month=8),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 6, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=28, month=8, hour=12, minute=0),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 7, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=30, month=8),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 8, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=6, month=9),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 9, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=8, month=9),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 10, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=13, month=9),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 11, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=20, month=9),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 12, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=27, month=9),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 13, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=4, month=10),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 14, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=11, month=10),
            class_type=1,
        )
    )
    return c


def gen_db(c: Calendar):
    CODE, l, START_DATE = (
        "DB(2009MK)",
        "Cheng Biqing Christopher",
        arrow.get(2023, 7, 27, tzinfo="Asia/Singapore").replace(hour=15, minute=30),
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 1, ClassType.LEC),
            desc=l,
            start_time=START_DATE,
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 2, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=3, month=8),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 3, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=7, month=8, hour=12, minute=0),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 4, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=10, month=8),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 5, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=17, month=8),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 6, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=24, month=8),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 7, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=31, month=8),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 8, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=4, month=9, hour=12, minute=0),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 9, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=7, month=9),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 10, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=14, month=9),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 11, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=21, month=9),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 12, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=28, month=9),
            class_type=1,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 13, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=5, month=10),
            class_type=2,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 14, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=12, month=10),
            class_type=1,
        )
    )


def gen_mm(c: Calendar):
    CODE, l, START_DATE = (
        "MM(5010MKT)",
        "Ng Siah Heng",
        arrow.get(2023, 11, 20, tzinfo=TZ).replace(hour=12),
    )

    # Lectures - November
    c.events.add(
        gen_event(
            name=gen_name(CODE, 1, ClassType.LEC),
            desc=l,
            start_time=START_DATE,
            class_type=ClassType.LEC,
        )
    )

    c.events.add(
        gen_event(
            name=gen_name(CODE, 2, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=24, hour=8, minute=30),
            class_type=ClassType.LEC,
        )
    )

    c.events.add(
        gen_event(
            name=gen_name(CODE, 3, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=27, hour=15, minute=30),
            class_type=ClassType.TUT,
        )
    )

    # Lectures - December
    dec = arrow.get(2023, 12, 1, tzinfo=TZ)
    c.events.add(
        gen_event(
            name=gen_name(CODE, 4, ClassType.LEC),
            desc=l,
            start_time=dec.replace(day=1, hour=8, minute=30),
            class_type=ClassType.LEC,
        )
    )

    c.events.add(
        gen_event(
            name=gen_name(CODE, 5, ClassType.TUT),
            desc=l,
            start_time=dec.replace(day=4, hour=15, minute=30),
            class_type=ClassType.TUT,
        )
    )

    c.events.add(
        gen_event(
            name=gen_name(CODE, 6, ClassType.LEC),
            desc=l,
            start_time=dec.replace(day=11, hour=15, minute=30),
            class_type=ClassType.LEC,
        )
    )

    c.events.add(
        gen_event(
            name=gen_name(CODE, 7, ClassType.TUT),
            desc=l,
            start_time=dec.replace(day=14, hour=12),
            class_type=ClassType.TUT,
        )
    )

    jan = arrow.get(2024, 1, 1, tzinfo=TZ)
    c.events.add(
        gen_event(
            name=gen_name(CODE, 8, ClassType.LEC),
            desc=l,
            start_time=jan.replace(day=4, hour=12),
            class_type=ClassType.LEC,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 9, ClassType.TUT),
            desc=l,
            start_time=jan.replace(day=5, hour=12),
            class_type=ClassType.TUT,
            location="Stem WIng",
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 10, ClassType.LEC),
            desc=l,
            start_time=jan.replace(day=8, hour=15, minute=30),
            class_type=ClassType.LEC,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 11, ClassType.TUT),
            desc=l,
            start_time=jan.replace(day=15, hour=15, minute=30),
            class_type=ClassType.TUT,
        )
    )

    c.events.add(
        gen_event(
            name=gen_name(CODE, 12, ClassType.LEC),
            desc=l,
            start_time=jan.replace(day=18, hour=8, minute=30),
            class_type=ClassType.LEC,
        )
    )

    c.events.add(
        gen_event(
            name=gen_name(CODE, 13, ClassType.TUT),
            desc=l,
            start_time=jan.replace(day=22, hour=15, minute=30),
            class_type=ClassType.TUT,
            location="Stem Wing",
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 14, ClassType.LEC),
            desc=l,
            start_time=jan.replace(day=26, hour=15, minute=30),
            class_type=ClassType.LEC,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 13, ClassType.TUT),
            desc=l,
            start_time=jan.replace(day=22, hour=15, minute=30),
            class_type=ClassType.TUT,
        )
    )


def gen_ecs2(c: Calendar):
    CODE, l, START_DATE = (
        "ECS2(A201CS)",
        "Victor Ong",
        arrow.get(2023, 11, 22, 15, 30, tzinfo=TZ),
    )

    c.events.add(
        gen_event(
            name=gen_name(CODE, 1, ClassType.LEC),
            desc=l,
            start_time=START_DATE,
            class_type=ClassType.LEC,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 2, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=29, hour=15),
            class_type=ClassType.LEC,
        )
    )

    c.events.add(
        gen_event(
            name=gen_name(CODE, 3, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=30, hour=8, minute=30),
            class_type=ClassType.TUT,
            location="Stem Wing",
        )
    )

    # Lectures - December
    d = arrow.get(2023, 12, 1, tzinfo=TZ)
    c.events.add(
        gen_event(
            name=gen_name(CODE, 4, ClassType.LEC),
            desc=l,
            start_time=d.replace(day=6, hour=15, minute=30),
            class_type=ClassType.LEC,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 5, ClassType.LEC),
            desc=l,
            start_time=d.replace(day=7, hour=15, minute=30),
            class_type=ClassType.LEC,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 6, ClassType.LEC),
            desc=l,
            start_time=d.replace(day=8, hour=15, minute=30),
            class_type=ClassType.LEC,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 7, ClassType.TUT),
            desc=l,
            start_time=d.replace(day=15, hour=15, minute=30),
            class_type=ClassType.TUT,
        )
    )

    # cw
    c.events.add(
        gen_event(
            name="Effective Communication Skills 2 CW Due",
            desc="",
            location="",
            start_time=arrow.get(2023, 12, 13, tzinfo=TZ),
            all_day=True,
            alarms=[
                DisplayAlarm(trigger=timedelta(days=-7)),
                DisplayAlarm(trigger=timedelta(days=-3)),
                DisplayAlarm(trigger=timedelta(days=-1)),
            ],
        )
    )


def gen_cb(c: Calendar):
    CODE, l, START_DATE = (
        "CB(5006MKT)",
        "S Salitha Nair D/O M Subramaniam",
        arrow.get(2023, 11, 21, tzinfo=TZ),
    )

    # Lectures - November
    c.events.add(
        gen_event(
            name=gen_name(CODE, 1, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(hour=12),
            class_type=ClassType.LEC,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 2, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=23, hour=12),
            class_type=ClassType.LEC,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 3, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=28, hour=12),
            class_type=ClassType.TUT,
        )
    )

    # Lectures - December
    d = arrow.get(2023, 12, 1, tzinfo=TZ)
    c.events.add(
        gen_event(
            name=gen_name(CODE, 4, ClassType.LEC),
            desc=l,
            start_time=d.replace(day=1, hour=12),
            class_type=ClassType.LEC,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 5, ClassType.TUT),
            desc=l,
            start_time=d.replace(day=5, hour=12),
            class_type=ClassType.TUT,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 6, ClassType.LEC),
            desc=l,
            start_time=START_DATE.replace(day=12, hour=12),
            class_type=ClassType.LEC,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 7, ClassType.TUT),
            desc=l,
            start_time=START_DATE.replace(day=13, hour=15, minute=30),
            class_type=ClassType.TUT,
        )
    )

    jan = arrow.get(2024, 1, 1, tzinfo=TZ)
    c.events.add(
        gen_event(
            name=gen_name(CODE, 8, ClassType.LEC),
            desc=l,
            start_time=jan.replace(day=9, hour=12),
            class_type=ClassType.LEC,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 9, ClassType.TUT),
            desc=l,
            start_time=jan.replace(day=12, hour=12),
            class_type=ClassType.TUT,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 10, ClassType.LEC),
            desc=l,
            start_time=jan.replace(day=16, hour=12),
            class_type=ClassType.LEC,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 11, ClassType.TUT),
            desc=l,
            start_time=jan.replace(day=23, hour=12),
            class_type=ClassType.TUT,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 12, ClassType.LEC),
            desc=l,
            start_time=jan.replace(day=25, hour=12),
            class_type=ClassType.LEC,
        )
    )

    feb = arrow.get(2024, 2, 1, tzinfo=TZ)
    c.events.add(
        gen_event(
            name=gen_name(CODE, 13, ClassType.TUT),
            desc=l,
            start_time=feb.replace(day=19, hour=15, minute=30),
            class_type=ClassType.TUT,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 14, ClassType.LEC),
            desc=l,
            start_time=feb.replace(day=20, hour=12),
            class_type=ClassType.LEC,
        )
    )

    # cw - exam
    c.events.add(
        gen_event(
            name="Consumer Behaviour CW Due",
            desc="",
            location="",
            start_time=arrow.get(2024, 1, 11, tzinfo=TZ),
            all_day=True,
            alarms=[
                DisplayAlarm(trigger=timedelta(days=-7)),
                DisplayAlarm(trigger=timedelta(days=-3)),
                DisplayAlarm(trigger=timedelta(days=-1)),
            ],
        )
    )

    c.events.add(
        gen_event(
            name="Consumer Behaviour Exam",
            desc="",
            location="",
            start_time=arrow.get(2024, 2, 29, 14, tzinfo=TZ),
            alarms=[
                DisplayAlarm(trigger=timedelta(days=-7)),
                DisplayAlarm(trigger=timedelta(days=-3)),
                DisplayAlarm(trigger=timedelta(days=-1)),
                DisplayAlarm(trigger=timedelta(hours=-3)),
            ],
        )
    )


def gen_cp(c: Calendar):
    CODE, l, jan = ("CP(5005MKT)", "Victor Ong", arrow.get(2024, 1, 1, tzinfo=TZ))

    # Lectures - January
    c.events.add(
        gen_event(
            name=gen_name(CODE, 1, ClassType.LEC),
            desc=l,
            start_time=jan.replace(day=2, hour=15, minute=30),
            class_type=ClassType.LEC,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 2, ClassType.LEC),
            desc=l,
            start_time=jan.replace(day=3, hour=15, minute=30),
            class_type=ClassType.LEC,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 3, ClassType.TUT),
            desc=l,
            start_time=jan.replace(day=10, hour=12),
            class_type=ClassType.TUT,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 4, ClassType.LEC),
            desc=l,
            start_time=jan.replace(day=11, hour=12),
            class_type=ClassType.LEC,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 5, ClassType.LEC),
            desc=l,
            start_time=jan.replace(day=17, hour=15, minute=30),
            class_type=ClassType.LEC,
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 6, ClassType.TUT),
            desc=l,
            start_time=jan.replace(day=19, hour=12),
            class_type=ClassType.TUT,
            location="Stem Wing",
        )
    )
    c.events.add(
        gen_event(
            name=gen_name(CODE, 7, ClassType.LEC),
            desc=l,
            start_time=jan.replace(day=24, hour=15, minute=30),
            class_type=ClassType.LEC,
        )
    )

    # cw - exam
    c.events.add(
        gen_event(
            name="Career Preparation CW Due",
            desc="",
            location="",
            start_time=arrow.get(2024, 1, 24, tzinfo=TZ),
            all_day=True,
            alarms=[
                DisplayAlarm(trigger=timedelta(days=-7)),
                DisplayAlarm(trigger=timedelta(days=-3)),
                DisplayAlarm(trigger=timedelta(days=-1)),
            ],
        )
    )


def gen_first_sem() -> Calendar:
    def gen_duedates(c: Calendar) -> Calendar:
        c.events.add(
            gen_event(
                name="Marketing Insight CW1 Due",
                desc="",
                location="",
                start_time=arrow.get(2023, 8, 29, tzinfo=TZ),
                all_day=True,
                alarms=[
                    DisplayAlarm(trigger=timedelta(days=-7)),
                    DisplayAlarm(trigger=timedelta(days=-3)),
                    DisplayAlarm(trigger=timedelta(days=-1)),
                ],
            )
        )
        c.events.add(
            gen_event(
                name="Marketing Insight CW2 Due",
                desc="",
                location="",
                start_time=arrow.get(2023, 10, 15, tzinfo=TZ),
                all_day=True,
                alarms=[
                    DisplayAlarm(trigger=timedelta(days=-7)),
                    DisplayAlarm(trigger=timedelta(days=-3)),
                    DisplayAlarm(trigger=timedelta(days=-1)),
                ],
            )
        )
        c.events.add(
            gen_event(
                name="Management and Leadership in Marketing CW Due",
                desc="",
                location="",
                start_time=arrow.get(2023, 10, 12, tzinfo=TZ),
                all_day=True,
                alarms=[
                    DisplayAlarm(trigger=timedelta(days=-7)),
                    DisplayAlarm(trigger=timedelta(days=-3)),
                    DisplayAlarm(trigger=timedelta(days=-1)),
                ],
            )
        )
        c.events.add(
            gen_event(
                name="Digital Business CW1 Due",
                desc="",
                location="",
                start_time=arrow.get(2023, 9, 12, tzinfo=TZ),
                all_day=True,
                alarms=[
                    DisplayAlarm(trigger=timedelta(days=-7)),
                    DisplayAlarm(trigger=timedelta(days=-3)),
                    DisplayAlarm(trigger=timedelta(days=-1)),
                ],
            )
        )
        c.events.add(
            gen_event(
                name="Digital Business CW2 Due",
                desc="",
                location="",
                start_time=arrow.get(2023, 10, 4, tzinfo=TZ),
                all_day=True,
                alarms=[
                    DisplayAlarm(trigger=timedelta(days=-7)),
                    DisplayAlarm(trigger=timedelta(days=-3)),
                    DisplayAlarm(trigger=timedelta(days=-1)),
                ],
            )
        )
        return c

    def gen_workshops(c: Calendar) -> Calendar:
        START_DATE = arrow.get(2023, 7, 24, tzinfo="Asia/Singapore").replace(
            hour=15, minute=30
        )
        c.events.add(
            gen_event(
                name="CU Referencing Workshop",
                desc="Dr Ng Jia Yun Florence",
                start_time=START_DATE,
                duration=3,
            )
        )
        c.events.add(
            gen_event(
                name="GNet",
                desc="",
                start_time=START_DATE.replace(day=31, month=7, hour=10, minute=0),
                duration=2,
            )
        )
        c.events.add(
            gen_event(
                name="Marketing Intensive Workshop",
                desc="Dr Liow Li Sa Melissa",
                start_time=START_DATE.replace(day=12, month=8, hour=9, minute=0),
                duration=9,
            )
        )
        return c

    c = Calendar()
    gen_workshops(c)
    gen_mi(c)  # MI(2007MK)
    gen_mlm(c)  # MLM(2000HR)
    gen_db(c)  # DB(2009MK)
    gen_duedates(c)
    return c


def gen_second_sem() -> Calendar:
    def gen_holidays(c: Calendar):
        c.events.add(
            gen_event(
                name="Midterm Break",
                desc="",
                start_time=arrow.get(2023, 12, 18, tzinfo=TZ),
                end_time=arrow.get(2023, 12, 22, tzinfo=TZ),
                all_day=True,
            )
        )

        c.events.add(
            gen_event(
                name="PH Christmas Break",
                desc="",
                start_time=arrow.get(2023, 12, 26, tzinfo=TZ),
                end_time=arrow.get(2023, 12, 30, tzinfo=TZ),
                all_day=True,
            )
        )

        c.events.add(
            gen_event(
                name="Study Break",
                desc="",
                start_time=arrow.get(2024, 1, 29, tzinfo=TZ),
                end_time=arrow.get(2024, 2, 8, tzinfo=TZ),
                all_day=True,
            )
        )

        c.events.add(
            gen_event(
                name="Chinese New Year Break",
                desc="",
                start_time=arrow.get(2024, 2, 12, tzinfo=TZ),
                end_time=arrow.get(2024, 2, 16, tzinfo=TZ),
                all_day=True,
            )
        )
    c = Calendar()
    gen_mm(c)  # MM(5010MKT)
    gen_ecs2(c)  # ECS2(A201CS)
    gen_cb(c)  # CB(5006MKT)
    gen_cp(c)  # CP(5005MKT)
    gen_holidays(c)
    return c


if __name__ == "__main__":
    c = gen_second_sem()
    with open("psb.ics", "w") as f:
        f.writelines(c.serialize_iter())
