def tables_info(table_cata: str) -> any:
    return """| Column  | Comment |
|--------|--------|
| companycode |公司编号 |
| companyname |公司名称 |
| is_listed | 是否上市公司 |
| country | 国家 |
| city | 城市 |
| SecretaryBD | 董事会秘书 |
| SecretaryBDTel | 	董秘电话 |
| SecretaryBDFax | 董秘传真 |
| SecuAffairsRepr | 证券/股证事务代表 |
| SecuAffairsReprTel | 证券事务代表电话 |
"""


def table_columns(table_name: str) -> any:
    tables_name = [table.strip() for table in table_name.split(",")]
    return """| Column  | Comment |
|--------|--------|
| companycode |公司编号 |
| companyname |公司名称 |
| is_listed | 是否上市公司 |
| country | 国家 |
| city | 城市 |
| SecretaryBD | 董事会秘书 |
| SecretaryBDTel | 	董秘电话 |
| SecretaryBDFax | 董秘传真 |
| SecuAffairsRepr | 证券/股证事务代表 |
| SecuAffairsReprTel | 证券事务代表电话 |
"""
