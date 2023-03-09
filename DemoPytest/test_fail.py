import pytest

class Test_Math:
  def test_divide_number(self):
    pytest.xfail("Need To Investigate")
    num = 10
    result = num + num
    assert result == num / num

  @pytest.mark.xfail(reason="Result Add Numbers & Not Multiply Numbers")
  def test_square_number(self):
    num = 10
    result = num + num # 10 * 10 = 100
    assert result == num ** 2

  @pytest.mark.xfail(reason="Result & Assert Are Correct")
  def test_cube_number(self):
    num = 10
    result = num * num * num # 10 * 10 * 10 = 1000
    assert result == num ** 3

  @pytest.mark.xfail(run=False)
  def test_number_square(self):
    num = 10
    result = num * num # 10 * 10 = 100
    assert result == num ** 2
