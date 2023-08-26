from pathlib import Path

from pydantic import BaseSettings, Field


BASE_DIR = Path(__file__).parent.parent.parent.absolute()


class Settings(BaseSettings):
    project_name: str = Field(..., env='PROJECT_NAME')

    # sentry
    sentry_dsn: str = Field(..., env='SENTRY_DSN')

    # elasticsearch
    elastic_host: str = Field(..., env='ELASTIC_HOST')
    elastic_port: int = Field(..., env='ELASTIC_PORT')
    elastic_index: str = Field(..., env='ELASTIC_INDEX')

    def get_es_uri(self):
        return "{host}:{port}".format(
            host=self.elastic_host,
            port=self.elastic_port,
        )

    class Config:
        env_file = BASE_DIR/"./env"


settings = Settings()
