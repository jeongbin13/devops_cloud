from .import predict_lotto_numbers

def test_predict_lotto_numbers():
    assert predict_lotto_numbers.check_available("로또")
    assert predict_lotto_numbers.check_available("로또번호 점지해줘")

    candidate_numbers = [1, 2, 3, 4, 5, 6, 7]
    