from pathlib import Path

from pydantic import BaseSettings, Field

BASE_DIR = Path(__file__).parent.parent.parent.absolute()


class Settings(BaseSettings):
    # sentry
    sentry_dsn: str = Field(..., env='SENTRY_DSN')

    # elasticsearch
    elastic_host: str = Field(..., env='ELASTIC_HOST')
    elastic_port: int = Field(..., env='ELASTIC_PORT')
    elastic_index: str = Field(..., env='ELASTIC_INDEX')

    # parser configs
    worker_count: int = Field(..., env='WORKER_COUNT')
    level_down: int = Field(..., env='LEVEL_DOWN')
    url: str = Field(..., env='URL')

    def get_es_uri(self):
        return "{host}:{port}".format(
            host=self.elastic_host,
            port=self.elastic_port,
        )

    class Config:
        env_file = BASE_DIR/"./env"


settings = Settings()
