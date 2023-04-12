from .base import Base


class TableInfo(Base):
    def answer(self) -> any:
        return """| Cata | Table | Table Comment |
|----------|-------|---------------|
| 公司管理    | comp_info    | 公司基本信息 |
| 公司管理    | comp_stock    | 公司涉及证券 |
"""
