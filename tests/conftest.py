import asyncio
import os
from asyncio import AbstractEventLoop
from collections.abc import Iterator
from dataclasses import dataclass

import pytest
import yaml
from sqlalchemy import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.asyncio import create_async_engine


@dataclass
class DatabaseConfig:
    host: str = "localhost"
    port: int = 5432
    database: str = "demo"
    user: str | None = None
    password: str | None = None


@pytest.fixture
def config() -> DatabaseConfig:
    config_path = os.environ.get("CONFIGPATH")
    print(f"CONFIGPATH: {config_path}")  # Отладочный вывод

    if not config_path:
        raise ValueError("Переменная CONFIGPATH не установлена!")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Файл конфига не найден: {config_path}")

    with open(config_path, "r") as f:
        raw_config = yaml.safe_load(f)
        print(f"Содержимое YAML: {raw_config}")  # Что реально загружено?

    if not raw_config or "database" not in raw_config:
        raise ValueError("YAML-файл не содержит ключ 'database'!")

    return DatabaseConfig(**raw_config["database"])

@pytest.fixture(scope="session")
def loop() -> AbstractEventLoop:
    return asyncio.get_event_loop()


@pytest.fixture(autouse=True)
async def engine(
    loop: AbstractEventLoop, config: DatabaseConfig
) -> Iterator[Engine]:
    engine = create_async_engine(
        URL.create(
            drivername="postgresql+asyncpg",
            host=config.host,
            database=config.database,
            username=config.user,
            password=config.password,
            port=config.port,
        ),
        echo=True,
    )

    yield engine

    await engine.dispose()


if __name__ == "__main__":
    config_path = os.environ.get("CONFIGPATH")
    print(config_path)