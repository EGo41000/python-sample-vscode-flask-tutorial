import pytest
from os import environ
from hello_app.views import recup_data

def test_mock():
  assert environ.get('BDD_URI')

  try:
    FileNotFoundError
  except NameError:
    FileNotFoundError = IOError

  with pytest.raises(FileNotFoundError):
    recup_data('')

  recup_data('https://data.seattle.gov/api/views/2bpz-gwpy/rows.csv?accessType=DOWNLOAD')

  assert True
