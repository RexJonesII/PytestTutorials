import pytest

# @pytest.mark.skip(reason="Demonstrate How To Skip A Class")
# @pytest.mark.xfail (reason="Demonstrate How To XFAIL/XPASS A Class")
class Test_Math:
  # Pass
  def test_number_square(self):
    num = 10
    result = num * num # 10 * 10 = 100
    assert result == num ** 2

  def test_divide_number(self):
    # Fail
    num = 10
    result = num + num
    assert result == num / num

  # Fail
  def test_square_number(self):
    num = 10
    result = num + num # 10 * 10 = 100
    assert result == num ** 2

  # Pass
  def test_cube_number(self):
    num = 10
    result = num * num * num # 10 * 10 * 10 = 1000
    assert result == num ** 3
