## Overview

This repository contains a pre-generated CSV table of points awarded for completing *M* stages in an *N*-stage tower in the ROBLOX game [Tower of Hell](https://www.roblox.com/games/1962086868/Tower-of-Hell#!/about) by [YXceptional Studios](https://www.roblox.com/communities/4217910/YXceptional-Studios#!/about), as well as the Python script used to generate that file.

Notably, this script calculates points awarded for completing a given stage on a given tower using the quadratic formula used in the ROBLOX game. The total point counts for each *N*-stage tower was gathered in-game conveniently from the private server menu, which lists all of these values. These values can help us determine the best method for min-max grinding points in-game.

If you wish to see an optimal min-max strategy for Tower of Hell, then read `STRATEGY.MD`.

## Usage

Install the dependencies for the Python script using the command below:
```
pip install -r requirements.txt
```

Then run the Python script `./src/toh.py` to generate a points lookup table as a pandas dataframe:
```
python ./src/toh.py
```

You can modify the script as needed to manipulate the lookup table or export it elsewhere. For example, you can create an output CSV with the pandas dataframe values by simply appending this to the end of `./src/toh.py`:

```python
# This file will be created in your working directory.
df.to_csv("toh-points.csv", index=False)
```

Note that this table has already been pre-generated in `./out/toh-points.csv` for your convenience.

## Attribution

This script was created by [Evan Redden](https://www.linkedin.com/in/eredden). Use it however you want, but don't blame me if something goes wrong! See the `LICENSE` file for additional information.