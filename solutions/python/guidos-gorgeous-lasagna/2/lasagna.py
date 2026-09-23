EXPECTED_BAKE_TIME = 40
def bake_time_remaining(elapsed_time):
    "return the remaining baking time"
    return EXPECTED_BAKE_TIME - elapsed_time
def preparation_time_in_minutes(number_of_layers):
    """return the preparation time based on the number of layers."""
    return number_of_layers * 2
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """return the total time spent preparing and baking the lasagna."""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

    