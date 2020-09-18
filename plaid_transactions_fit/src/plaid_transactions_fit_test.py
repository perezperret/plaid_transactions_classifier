from . import plaid_transactions_fit

def test_plaid_transactions_fit():
    assert plaid_transactions_fit.apply("Jane") == "hello Jane"
