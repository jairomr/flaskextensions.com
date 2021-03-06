"""
Autor - Douglas d'Auriol <ddauriol@gmail.com>
Baseado na Live de Python e na documentação do dynaconf
https://dynaconf.readthedocs.io/en/latest/guides/validation.html
"""
from dynaconf import settings, Validator

# Register validators
# TODO - Validar os requsitos do GITHUB_TOKEN e os querisitos da SEARCH_QUERY
settings.validators.register(
    # Ensure some parameters exists (are required)
    Validator('DB_USER', 'DB_NAME', 'GITHUB_TOKEN', 'SEARCH_QUERY', must_exist=True),

    # Ensure some parameter mets a condition
    # conditions: (eq, ne, lt, gt, lte, gte, identity, is_type_of, is_in, is_not_in)
    # Validação de um valor mínimo para o DELAY e a PRIORITY
    Validator('DELAY', gte=10),
    Validator('PRIORITY', gte=100),

    # validate a value is eq in specific env

    # Validalção do modelo de DB utilizado durante o Desenvolvimento e a produção
    Validator('DATABASE_URL', eq='sqlite:///:memory:'), #TODO: Definir o Banco de produção e definir env=''
)

