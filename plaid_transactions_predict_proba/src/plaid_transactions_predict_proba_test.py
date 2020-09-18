from . import plaid_transactions_predict_proba

def test_plaid_transactions_predict_proba():
    assert plaid_transactions_predict_proba.apply("Jane") == "hello Jane"
