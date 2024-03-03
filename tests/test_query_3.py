from sqlalchemy import Engine, text

from sql_queries import TASK_3_QUERY


async def test_query_3(engine: Engine) -> None:
    #  count
    # --------
    #  16824
    async with engine.connect() as conn:
        res = await conn.execute(text(TASK_3_QUERY))

    assert res.scalar() == 16824
