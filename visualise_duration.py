import pandas as pd
import matplotlib.pyplot as plt



train = [3,5,4,2,0]
car = [3,4,5,2,0]
walk = [3,5,4,0,1]

def visualise_durations(train,car, walk):
  df = pd.DataFrame({'train' : train,'car' : car, 'walk' : walk})

  ax = df.plot.barh(stacked=True, cmap='tab10', figsize=(16, 10))

  for c in ax.containers:
      # format the number of decimal places and replace 0 with an empty string
      labels = [f'{w:.0f}' if (w := v.get_width()) > 0 else '' for v in c ]
      
      ax.bar_label(c, labels=labels, label_type='center')
  plt.xlabel('time taken/minute')

visualise_durations(train,car, walk)

