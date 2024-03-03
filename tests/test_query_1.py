import datetime

from sqlalchemy import Engine, text

from sql_queries import TASK_1_QUERY


async def test_query_1(engine: Engine) -> None:
    #  flight_no | duration
    # -----------+----------
    #  PG0235    | 00:25:00
    #  PG0234    | 00:25:00
    #  PG0233    | 00:25:00
    #  PG0235    | 00:25:00
    #  PG0234    | 00:25:00
    async with engine.connect() as conn:
        res = await conn.execute(text(TASK_1_QUERY))

    assert res.all() == [
        ("PG0235", datetime.timedelta(seconds=1500)),
        ("PG0234", datetime.timedelta(seconds=1500)),
        ("PG0233", datetime.timedelta(seconds=1500)),
        ("PG0235", datetime.timedelta(seconds=1500)),
        ("PG0234", datetime.timedelta(seconds=1500)),
    ]
