'''
Instpired by the Flaskr tests
These are going to be the initial tests that the app
has to pass
'''

from Quest import create_app

def test_config():
    '''
    The app can start on test mode, or run mode
    '''
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_help(client):
    response = client.get('/help')
    assert response.data == b'API DOC'
