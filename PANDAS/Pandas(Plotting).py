# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_excel('workout_data.xlsx')

# df.plot()

# plt.show()
# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_excel('workout_data.xlsx')

# df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
# plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('workout_data.xlsx')

df["Duration"].plot(kind = 'hist')
plt.show()