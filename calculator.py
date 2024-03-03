KM_IN_METERS = 1000.0
MILE_IN_METERS = 1609.34
YARD_IN_METERS = 0.9144


def calc_pace(distance, time):
    """
    Calculate pace

    :param distance: distance in meters, float
    :param time: time in seconds, float
    :return: pace in seconds per meter
    """
    assert isinstance(distance, float)
    assert isinstance(time, float)
    assert distance != 0.0
    return time / distance


def pace_to_speed(pace):
    speed = 3.6 / pace
    return speed


def format_pace(pace, unit='km'):
    """
    Format pace to string format mm:ss per kilometer

    :param unit: pace in km or mile
    :type pace: float
    :param pace: pace in seconds per meter
    :return: string format mm:ss/unit
    """
    if unit == 'km':
        pace_scaled = pace * KM_IN_METERS / 60.0
    elif unit == 'mile':
        pace_scaled = pace * MILE_IN_METERS / 60.0
    else:
        raise Exception('Incorrect pace unit')
    minutes = str(int(pace_scaled))
    seconds = str(round((pace_scaled % 1) * 60, 1))
    return minutes + ':' + seconds + '/' + unit


def format_speed(speed):
    return str(round(speed, 1)) + ' km/h'


def distance_to_meters(distance):
    """
    Convert distance input to meters

    :param distance: input string
    :return: distance in meters
    """
    assert isinstance(distance, str)
    unit = distance.split()[1]
    factor = 0.0
    if unit in ('km', 'kilometer', 'kilometers'):
        factor = KM_IN_METERS
    elif unit in ('m', 'meter', 'meters'):
        factor = 1.0
    elif unit in ('mi', 'mile', 'miles'):
        factor = MILE_IN_METERS
    elif unit in ('yd', 'yard', 'yards'):
        factor = YARD_IN_METERS
    else:
        raise Exception("Unknown distance unit")
    return float(distance.split()[0]) * factor


def time_to_seconds(time):
    """
    Convert time input to seconds

    :param time: input string
    :return: time in seconds
    """
    assert isinstance(time, str)
    time_split = time.split(':')
    seconds = 0.0
    minutes = 0.0
    hours = 0.0
    if len(time_split) == 2:
        minutes = float(time_split[0])
        seconds = float(time_split[1])
    elif len(time_split) == 3:
        hours = float(time_split[0])
        minutes = float(time_split[1])
        seconds = float(time_split[2])
    return hours*3600 + minutes*60 + seconds
