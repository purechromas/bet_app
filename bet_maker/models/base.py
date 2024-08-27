from sqlalchemy.orm import DeclarativeBase, declared_attr

from bet_library.common_utils import camel_case_2_snake_case


class BaseModelBetMakerDB(DeclarativeBase):
    @classmethod
    @declared_attr
    def __tablename__(cls):
        """Генерируем автоматически __tablename__ и преобразуем TableName(CamelCase) в table_name(snake_case)"""
        return camel_case_2_snake_case(cls.__name__)
