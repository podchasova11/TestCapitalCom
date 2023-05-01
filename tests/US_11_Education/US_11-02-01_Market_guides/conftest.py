import pytest
from datetime import datetime

# URL = "https://capital.com/trading-guides"


@pytest.fixture(
   scope="class",
   params=[
    "",  # "en"
    "ar",
    "bg",
    "cs",
    "da",
    "de",
    "el",
    "es",
    "et",
    "fi",
    "hr",
    "hu",
    "it",
    "lt",
    "lv",
    "nl",
    "pl",
    "pt",
    "ro",
    "ru",
    "sk",
    "sl",
    "sv",
    "vi",
    "zh",
# Education to trade present
    # id",
    # "th",
# #  -- Problem with 'Privacy policy' !
    "cn",
    "fr",
    ],
)
def cur_language(request):
    print(f"Current test language - {request.param} ")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        "au",  # Australia - "ASIC" - https://capital.com/?country=au
        "gb",  # United Kingdom - "FCA" - https://capital.com/?country=gb
        "de",  # Germany - "CYSEC" - https://capital.com/?country=de
        "tr",  # Turkey - "SCB" - https://capital.com/?country=tr
        # "ar",  # United Arab Emirates - "SCB" - https://capital.com/?country=ar
        # "bg",  # Bulgaria - "CYSEC" - https://capital.com/?country=bg

        # "NBRB" - пока не проверяем
        # "SFB",
        # "FSA"
    ],
)
def cur_country(request):
    print(f"Current test Country - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        "NoReg",
        # "Reg/NoAuth",
        # "Auth",
    ],
)
def cur_role(request):
    print(f"Current test role - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        "Empty",
        # "aqa.tomelo.an@gmail.com",
    ],
)
def cur_login(request):
    print(f"Current Login - {request.param}")
    return request.param


@pytest.fixture(
    scope="class",
    params=[
        "Empty",
        # "iT9Vgqi6d$fiZ*Z",
    ],
)
def cur_password(request):
    print(f"Current Login - {request.param}")
    return request.param


@pytest.fixture()
def cur_time():
    return str(datetime.now())
