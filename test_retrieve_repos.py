import retrieve_repos as retrep;

def test_parsing():
    assert retrep.retrieve_repos("talisainen") == 6
