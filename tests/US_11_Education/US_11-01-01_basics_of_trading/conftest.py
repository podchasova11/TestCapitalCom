import pytest
from datetime import datetime

# URL = "https://capital.com/basics-of-trading"


@pytest.fixture(
    scope="class",
    params=[
          "",  # "en"
        "cs",
        "de",
        "fr",
        "bg",
        "ru",
        "da",
        "el",
        "es",
        "et",
        "hr",
        "it",
        "hu",
        "lv",
        "nl",
        "pl",
        "pt",
        "ro",
        "sk",
        "sl",
        "fi",
        "sv",
        "zh",
        "lt",
        # # "cn",
        # # "vi",
        # # "ar",
        # # "id",
    ],
)
# Выбор языка
def cur_language(request):
    print(f"Current test language - {request.param}")
    return request.param


# Выбор лицензии
@pytest.fixture(
    scope="class",
    params=[
        "au",  # Australia - "ASIC" - https://capital.com/?country=au
        "gb",  # United Kingdom - "FCA" - https://capital.com/?country=gb
        "bg",  # Bulgaria - "CYSEC" - https://capital.com/?country=bg
        # "de",  # Germany - "CYSEC" - https://capital.com/?country=de
        "tr",  # Turkey - "SCB" - https://capital.com/?country=tr
        # "ar",  # United Arab Emirates - "SCB" - https://capital.com/?country=ar


        # "NBRB" - пока не проверяем
        # "SFB",
        # "FSA"
    ],
)
def cur_country(request):
    """Fixture"""
    print(f"Current country of trading - {request.param}")
    return request.param


# Выбор роли
@pytest.fixture(
    scope="class",
    params=[
        "NoReg",
        # "Reg_NoAuth",
        # "Auth",
    ],
)
def cur_role(request):
    print(f"Current test role - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        # "Empty",
        "aqa.tomelo.an@gmail.com",
    ],
)
def cur_login(request):
    """Fixture"""
    print(f"Current login - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        # "Empty",
        "iT9Vgqi6d$fiZ*Z",
    ],
)
def cur_password(request):
    """Fixture"""
    print(f"Current login - {request.param}")
    return request.param

# Тайм штамп


@pytest.fixture()
def cur_time():
    """Fixture"""
    return str(datetime.now())
