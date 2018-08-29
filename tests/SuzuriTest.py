import os
import pytest
from suzuripy import SuzuriClient
SUZURI_API_KEY = os.environ["SUZURI_API_KEY"]


class SuzuriTest:

    @pytest.fixture()
    def client(request):
        return SuzuriClient(key=SUZURI_API_KEY)
