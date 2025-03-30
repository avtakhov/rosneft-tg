from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    telegram_api_base_url: str = 'https://api.telegram.org/bot'
    telegram_token: str
    telegram_updates_secret_token: str
    telegram_webhook_base_url: str
    admin_chat_id: int

    class Config:
        env_file = ".env"


settings = Settings()
