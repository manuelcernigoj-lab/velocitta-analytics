"""
Creating the function calculate_duration_minutes(start_time: str, end_time: str) -> int
    - Input format: "HH:MM"
    - Raises ValueError if end_time is earlier than start_time
"""

def duration_minutes_calculator(start_time: str, end_time: str) -> int:
    """
    Calculates the duration in minutes between two times in 'HH:MM' format.

    Parameters
    ----------
    start_time : str
    Start time, 'HH:MM' format (e.g., '08:30').
    end_time : str
    End time, 'HH:MM' format (e.g., '09:15').

    Returns
    -------
    int
    Duration in whole minutes between the two times.

    Raises
    ------
    ValueError
    If end_time is before or equal to start_time.

    Examples
    --------
    >>> duration_minutes_calculator('08:30', '09:15')
    45
    >>> duration_minutes_calculator('23:00', '08:00')
    ValueError: end_time must be later than start_time
    """
    
    # --[internal function to validate that the time is in the correct format]--
    def _time_validator(time: str, name: str) -> tuple[int, int]:
        """
        Validates format and values of a time 'HH:MM', returns (hours, minutes).
        """

        try:
            hh, mm = time.split(":")
            hh, mm = int(hh), int(mm)
        except ValueError:
            raise ValueError(f"{name} is not in valid format 'HH:MM': '{time}'")
            # ↘ The name parameter is used to provide precise error messages
            #   about which of the two times is incorrect.

        if not (0 <= hh <= 23):
            raise ValueError(f"{name}: hours out of range (0-23), received {hh}")
        if not (0 <= mm <= 59):
            raise ValueError(f"{name}: minutes out of range (0-59), received {mm}")
        
        return hh, mm

    # --[saving start and end hh and mm in variables]--
    hh_i, mm_i = _time_validator(start_time, "start_time")
    hh_f, mm_f = _time_validator(end_time,   "end_time")

    # --[calculate start and end totals in minutes to simplify verification]--
    start_tot = hh_i * 60 + mm_i
    end_tot   = hh_f * 60 + mm_f

    # --[raises 'ValueError' if end_time is earlier than start_time]--
    if end_tot <= start_tot:
        raise ValueError(f"end_time '{end_time}' must be later than start_time '{start_time}'")

    return end_tot - start_tot

"""
Creating the function rides_classifier(duration_minutes: int) -> str
    - "short" if < 15 min, "medium" if 15-45 min, "long" if > 45 min
"""

def rides_classifier(duration_min: int) -> str:
    """
    Classifies a ride based on its duration in minutes.

    Parameters
    ----------
    duration_min : int
    Ride duration in whole minutes. Must be > 0.

    Returns
    -------
    str
    Ride category:
    - 'short' : duration < 15 min
    - 'medium' : 15 <= duration <= 45 min
    - 'long' : duration > 45 min

    Raises
    ------
    ValueError
    If duration_min is <= 0.

    Examples
    --------
    >>> rides_classifier(10)
    'short'
    >>> rides_classifier(30)
    'medium'
    >>> rides_classifier(60)
    'long'
    """

    # --[classification by conditions if/else]--
    if duration_min <= 0:
        raise ValueError(f"duration_min '{duration_min}' must be greater than or equal to zero'")
        # ↘ check on the insertion of negative values ​​→ raise ValueError

    elif duration_min < 15:
        return "short"
    elif duration_min <= 45:
        return "medium"
    else:
        return "long"
    
"""
Creating the function summary_rides(list_durations: list) -> dict
    - Returned keys: total, medium, max, min, short, medium, long
"""

def summary_rides(duration_list: list) -> dict:
    """
    Calculates summary statistics on a list of trip durations.

    Parameters
    ----------
    duration_list : list[int]
    List of durations in whole minutes. Must not be empty.

    Returns
    -------
    dict
    Dictionary with the following keys:
    - 'total'   : int — total trip duration
    - 'average' : float — average duration in minutes
    - 'max'     : int — maximum duration in minutes
    - 'min'     : int — minimum duration in minutes
    - 'short'   : int — number of trips < 15 minutes
    - 'medium'  : int — number of trips between 15 and 45 minutes
    - 'long'    : int — number of trips > 45 minutes

    Raises
    ------
    ValueError
    If duration_list is empty.

    Examples
    --------
    >>> summary_rides([10, 30, 60, 20, 5])
    {
        'total'     : 125,
        'average'   : 25.0,
        'max'       : 60,
        'min'       : 5,
        'short'     : 2,
        'medium'    : 2,
        'long'      : 1
    }
    """

    # --[input validation]--
    if not duration_list:
        raise ValueError("duration_list can't be empty")

    # --[statistics calculation for summary]--
    t_duration =    sum(duration_list)
    avg =           sum(duration_list) / len(duration_list)
    maximum =       max(duration_list)
    minimum =       min(duration_list)

    # for categorization, reuse the 'rides_classifier()' function
    short, medium, long = 0, 0, 0
    for d in duration_list:
        cat = rides_classifier(d)
        if   cat == "short":    short  += 1
        elif cat == "medium":   medium  += 1
        else:                   long += 1
    
    # --[output dictionary creation]--
    summary = {
        "total":    t_duration,
        "average":  avg,
        "max":      maximum,
        "min":      minimum,
        "short":    short,
        "medium":   medium,
        "long":     long
        }
    
    return summary

"""
Additional utility to validate the bike_id format using the 're' module
"""
import re

def bike_id_validator(bike_id: str) -> None:
    """
    Validates the format of a bike ID using a regular expression.

    The expected format is 'AA-000': two uppercase letters, a hyphen,
    three numeric digits. Valid examples: 'MI-042', 'TO-001', 'RM-300'.

    Regex pattern used: r"^[A-Z]{2}-\\d{3}$"
    - ^ start of string
    - [A-Z]{2} exactly 2 uppercase letters (A-Z)
    - - literal hyphen
    - \\d{3} exactly 3 numeric digits (0-9)
    - $ end of string

    Parameters
    ----------
    bike_id : str
    Identifier of the bike to validate.

    Returns
    -------
    None
    Returns nothing if the format is valid.

    Raises
    ------
    ValueError
    If bike_id does not match the 'AA-000' format.

    Examples
    --------
    >>> bike_id_validator('MI-042') # no error
    >>> bike_id_validator('mi-042')
    ValueError: Invalid id format 'mi-042': expected 'AA-000'
    >>> bike_id_validator('MI-42')
    ValueError: Invalid id format 'MI-42': expected 'AA-000'
    """

    if not re.match(r"^[A-Z]{2}-\d{3}$", bike_id):
        raise ValueError(f"Invalid id format '{bike_id}': expected 'AA-000'")