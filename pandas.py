# import pandas as pd
# import numpy as np


# df=DataFrame({"Name":["Tom", "Mike","Tiffany"],
#               "Language":["Python", "Python","R"],
#               "Courses":[5,4,7]})

# df.iloc[0:1]

# df.loc[[0,2],"Name"]

# df[df["Courses"]>4]

import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 30, 28]
}

df = pd.DataFrame(data)
print(df)