from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    env: str = Field("dev", env="ENV")
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    LEDGER_NAME: str
    REGION_NAME: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    ACCOUNT_SID: str
    AUTH_TOKEN: str
    VERIFY_SID: str
    MAIL_USERNAME: str
    MAIL_PASSWORD: str
    MAIL_FROM: str
    MAIL_PORT: int
    MAIL_SERVER: str
    MAIL_FROM_NAME: str
    MAIL_TLS: bool
    MAIL_SSL: bool
    TEMPLATE_FOLDER: str
    STRIPE_API_KEY: str
    STRIPE_PUBLIC_KEY: str
    STRIPE_PRICE: str
    NSP_COMMISSION: int
    DSL_COMMISSION: int
    RSL_COMMISSION: int
    AGENT_COMMISSION: int
    BROKER_COMMISSION: int
    BROKER_AGENT_COMMISSION: int
    TERMS_CREATED: int
    SORRY: bool
    DEV_EMAIL: bool
    AIRTABLE_API_KEY: str
    AIRTABLE_BASE_ID: str
    AT_EMAIL_TABLE: str
    AT_PRODUCT_TABLE: str
    AT_MANUFACTURER_TABLE: str
    B12_TARGET: str
    API_KEYS: str

    class Config:
        env_file = '.env'


settings = Settings()
