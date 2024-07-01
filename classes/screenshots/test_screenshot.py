import pytest

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_make_report(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

    return rep



@pytest.fixture()
def log_on_failure(request):
    msgs = []
    yield msgs.append
    item = request.node
    print(type(item))
    print(rep)

    # if item.rep_call.failed:
    # if 1 == 1:
    # print('\nlogged messages:', item.nodeid)
    # for m in msgs:
    #     print(m.rep_call)




def test_screenshot_001(log_on_failure):
    assert 1 == 1
    print("Hoooo")
