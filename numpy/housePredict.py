import csv
import numpy as np

def readData():
    X = []
    y = []
    with open('Housing.csv') as f:
        rdr = csv.reader(f)
        # Skip the header row
        next(rdr)
        # Read X and y
        for line in rdr:
            xline = [1.0]
            for s in line[2:6]:
              xline.append(float(s))
            for s in line[6:11]:
              if s== 'yes':
                xline.append(1)
              else:
                xline.append(0)
            X.append(xline)
            y.append(float(line[1]))
    return (X,y)

X0,y0 = readData()

print(X0,y0)

Convert all but the last 10 rows of the raw data to numpy arrays
d = len(X0)-10
X = np.array(X0[:d])
y = np.transpose(np.array([y0[:d]]))

# Compute beta
Xt = np.transpose(X)
XtX = np.dot(Xt,X)
Xty = np.dot(Xt,y)
beta = np.linalg.solve(XtX,Xty)
print(beta)

# Make predictions for the last 10 rows in the data set
for data,actual in zip(X0[d:],y0[d:]):
    x = np.array([data])
    prediction = np.dot(x,beta)
    print('prediction = '+str(prediction[0,0])+' actual = '+str(actual))