"""EX08.2 Tests."""
from solution import students_study, lottery, fruit_order


def test_students_study__evening_no_coffee_needed():
    """In the evening it doesn't matter whether or not coffee is drank."""
    assert students_study(20, True) is True
    assert students_study(20, False) is True


def test_students_study__night_no_study():
    """During nighttime it doesn't matter whether or not coffee is drank."""
    assert students_study(2, True) is False
    assert students_study(2, False) is False


def test_students_study__day_coffee_needed():
    """During daytime it matters whether or not coffee is drank."""
    assert students_study(10, True) is True
    assert students_study(10, False) is False


def test_student_study__evening_edge_case_evening_no_coffee_needed():
    """In the evening test whether or not 18 and 24 are included in the time check."""
    assert students_study(18, True) is True
    assert students_study(18, False) is True
    assert students_study(24, True) is True
    assert students_study(24, False) is True


def test_student_study__night_edge_case():
    """Test nighttime edge cases."""
    assert students_study(1, True) is False
    assert students_study(1, False) is False
    assert students_study(4, True) is False
    assert students_study(4, False) is False


def test_student_study__day_edge_case():
    """Test daytime edge cases."""
    assert students_study(5, True) is True
    assert students_study(5, False) is False
    assert students_study(17, True) is True
    assert students_study(17, False) is False


def test_lottery__all_fives():
    """Test lottery when all numbers are 5."""
    assert lottery(5, 5, 5) == 10


def test_lottery__all_same_positive():
    """Test lottery when all numbers are the same and positive."""
    assert lottery(2, 2, 2) == 5


def test_lottery__all_same_negative():
    """Test lottery when all numbers are the same and negative."""
    assert lottery(-2, -2, -2) == 5


def test_lottery__all_same_zero():
    """Test lottery when all numbers are the same and 0."""
    assert lottery(0, 0, 0) == 5


def test_lottery__a_b_same_c_diff():
    """Test lottery when a and b are the same but c is different."""
    assert lottery(2, 2, 3) == 0


def test_lottery__a_c_same_b_diff():
    """Test lottery when a and c are the same but b is different."""
    assert lottery(2, 3, 2) == 0


def test_lottery__b_c_same_a_diff():
    """Test lottery when b and c are the same but a is different."""
    assert lottery(3, 2, 2) == 1


def test_lottery__all_diff():
    """Test lottery when all the numbers are different."""
    assert lottery(1, 2, 3) == 1


def test_fruit_order__zero_amount_zero_small():
    """Test fruit_order when amount and small_baskets are 0."""
    assert fruit_order(0, 2, 0) == 0


def test_fruit_order__zero_amount_zero_big():
    """Test fruit_order when there are 0 big_baskets and the amount is 0."""
    assert fruit_order(2, 0, 0) == 0


def test_fruit_order__zero_amount_others_not_zero():
    """Test fruit_order when the amount is zero but big_baskets and small_baskets aren't."""
    assert fruit_order(2, 2, 0) == 0


def test_fruit_order__all_zero():
    """Test fruit_order when all the arguments are 0."""
    assert fruit_order(0, 0, 0) == 0


def test_fruit_fruit_order__not_enough():
    """Test fruit_order when there arent enough baskets for given amount."""
    assert fruit_order(3, 2, 14) == -1


def test_fruit_order__use_some_smalls_all_bigs():
    """Test fruit_order when all bigs are used but no smalls."""
    assert fruit_order(2, 2, 11) == 1


def test_fruit_order__use_some_bigs_all_smalls():
    """Test fruit_order when all bigs are used but no smalls."""
    assert fruit_order(2, 2, 7) == 2


def test_fruit_order__only_small_exact_match():
    """Test fruit_order when there are only small_baskets and it matches the amount."""
    assert fruit_order(3, 0, 3) == 3


def test_fruit_order__only_big_exact_match():
    """Test fruit_order when there are only big_baskets and it matches the amount."""
    assert fruit_order(0, 2, 10) == 0


def test_fruit_order__only_big_not_enough():
    """Test fruit_order when there are only big_baskets and it isn't enough."""
    assert fruit_order(0, 1, 10) == -1


def test_fruit_order__only_small_not_enough():
    """Test fruit_order when there are only small_baskets and it isn't enough."""
    assert fruit_order(3, 0, 4) == -1


def test_fruit_order__only_big_more_than_required_match():
    """Test fruit_order when there are more than enough big_baskets, no small_baskets and it matches."""
    assert fruit_order(0, 3, 10) == 0


def test_fruit_order__only_small_more_than_required_match():
    """Test fruit_order when there are more than enough small_baskets, no big_baskets and it matches."""
    assert fruit_order(3, 0, 2) == 2


def test_fruit_order__only_big_more_than_required_no_match():
    """Test fruit_order when there are more than enough big_baskets, no small_baskets and it doesn't match."""
    assert fruit_order(0, 3, 11) == -1


def test_fruit_order__only_small_match_more_than_5_smalls():
    """Test fruit_order when there are only small_baskets, more than 5 of them and it matches."""
    assert fruit_order(11, 0, 10) == 10


def test_fruit_order__only_small_not_enough_more_than_5_smalls():
    """Test fruit_order when there are only small_baskets, more than 5 of them and it doesn't match."""
    assert fruit_order(9, 0, 10) == -1


def test_fruit_order__match_with_more_than_5_smalls():
    """Test fruit_order when there are some big_baskets more than 5 small_baskets and it matches."""
    assert fruit_order(15, 2, 23) == 13


def test_fruit_order__all_positive_exact_match():
    """Test fruit_order when there are some big_baskets more than 5 small_baskets and it matches."""
    assert fruit_order(4, 4, 24) == 4


def test_fruit_order__use_some_smalls_some_bigs():
    """Test fruit_order when there are some big_baskets more than 5 small_baskets and it matches."""
    assert fruit_order(10, 10, 47) == 2


def test_fruit_order__enough_bigs_not_enough_smalls():
    """Test fruit_order when there are some big_baskets more than 5 small_baskets and it matches."""
    assert fruit_order(3, 10, 44) == -1


def test_fruit_order__not_enough_with_more_than_5_smalls():
    """Test fruit_order when there are some big_baskets more than 5 small_baskets and it matches."""
    assert fruit_order(11, 2, 50) == -1


def test_fruit_order__enough_bigs_not_enough_smalls_large_numbers():
    """Test fruit_order when there are some big_baskets more than 5 small_baskets and it matches."""
    assert fruit_order(3, 2222, 9999) == -1


def test_fruit_order__match_large_numbers():
    """Test fruit_order when there are some big_baskets more than 5 small_baskets and it matches."""
    assert fruit_order(9999, 2222, 15334) == 4224
