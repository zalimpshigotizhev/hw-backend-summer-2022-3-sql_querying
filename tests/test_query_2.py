from sqlalchemy import Engine, text

from sql_queries import TASK_2_QUERY


async def test_query_2(engine: Engine) -> None:
    #  flight_no | count
    # -----------+-------
    #  PG0260    |    27
    #  PG0371    |    27
    #  PG0310    |    27
    async with engine.connect() as conn:
        res = await conn.execute(text(TASK_2_QUERY))

    assert res.all() == [
        ("PG0260", 27),
        ("PG0371", 27),
        ("PG0310", 27),
    ]
