# toh.py - Create a lookup table of points awarded for completing stages in a 
# tower from the ROBLOX game Tower of Hell by YXceptional Studios.

import math
import pandas as pd

# Global variables for stage constraints.
MIN_STAGES = 4
EFFECTIVE_MAX_STAGES = 18
TRUE_MAX_STAGES = 40
MAX_POINTS = 300

# Lookup table for tower stage count to total points.
STAGE_POINTS: dict[int, int] = {
    4:  30,
    5:  70,
    6:  100,
    7:  120, 
    8:  150,
    9:  180,
    10: 210,
    11: 229,
    12: 250,
    13: 254,
    14: 260,
    15: 270,
    16: 280,
    17: 290
}

# Calculates total points of a tower based on the number of stages.
def total_stages_to_points(stages: int) -> int:
    if stages < MIN_STAGES or stages > TRUE_MAX_STAGES:
        raise ValueError(f"Stage count must be between {MIN_STAGES} and {TRUE_MAX_STAGES}.")

    # Stages are capped at rewarding 300 points at most.
    if stages >= EFFECTIVE_MAX_STAGES:
        return MAX_POINTS

    return STAGE_POINTS[stages]

# Calculate the points awarded for completing stages in a tower.
def calculate_points(completed_stages: int, total_stages: int) -> int:
    if completed_stages > total_stages:
        raise ValueError("Completed stages cannot exceed total stages.")
    
    if completed_stages < 0 or total_stages < 0:
        raise ValueError("Completed and total stages cannot be negative.")
    
    if completed_stages == 0:
        return 0

    total_points: int = total_stages_to_points(total_stages)
    completed_percent: float = completed_stages / total_stages

    return math.floor(total_points * pow(completed_percent, exp=2))

# Generate a pandas dataframe of points awarded for completing stages in a tower.
def generate_points_table() -> pd.DataFrame:
    records = [
        {
            "total_stages": total,
            "completed_stages": completed,
            "points_awarded": calculate_points(completed, total),
        }
        for total in range(MIN_STAGES, EFFECTIVE_MAX_STAGES + 1)
        for completed in range(1, total + 1)
    ]
    return pd.DataFrame(records)

if __name__ == "__main__":
    df = generate_points_table()
    print(df)