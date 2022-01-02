import numpy as np
import math

# Dati della tabella
data = np.array([[833. ,  37. ],
                 [987. ,  41.6],
                 [883. ,  37.2],
                 [378. ,  15.2],
                 [ 84. ,   3.4],
                 [483. ,  19.6],
                 [835. ,  35.1],
                 [646. ,  28.9],
                 [508. ,  22.6],
                 [ 90. ,   3.7]])

#------------------------
# definizione del modello
#------------------------

class LinearModel:

    def __init__(self):
        self.angular_coeff = None
        self.intercept = None
        self.train_data = None


    def compute_angular_coeff(self, xs, ys):
        corrcoef = np.corrcoef(xs, ys)[0,1]
        m = corrcoef * (np.std(ys) / np.std(xs))
        return m


    def compute_intercept(self, xs, ys, m):
        q = np.mean(ys) - m * np.mean(xs)
        return q


    def fit(self, train_data):
        # controllo che train_data sia della forma giusta
        try:
            assert(len(train_data.shape)==2)
            assert(train_data.shape[1]==2)
        except:
            raise Exception("Bad train_data shape! {} should be (*,2)".format(train_data.shape))
        
        # ricavo le x e le y da train_data
        xs = train_data[:,0]
        ys = train_data[:,1]
        
        self.angular_coeff = self.compute_angular_coeff(xs, ys)
        self.intercept = self.compute_intercept(xs, ys, self.angular_coeff)
            
        self.train_data = train_data


    def compute_y(self, x, m, q):
        return m * x + q


    def predict(self, xs):
        
        if self.angular_coeff is None or self.intercept is None:
            raise Exception("Angular coeff is {}, intercept is {}. Both should be defined!".format(self.angular_coeff, self.intercept))
        
        predicted_ys = []
        for x in xs: predicted_ys.append(self.compute_y(x, self.angular_coeff, self.intercept))
        
        return predicted_ys


#-------------------------
# applicazione del modello
#-------------------------

lm = LinearModel()
lm.fit(data)

km_tragitto = 2500
litri_tragitto = lm.predict([km_tragitto])[0]

prezzo_benzina = litri_tragitto * 1.4
quota_individuale = prezzo_benzina / 3

# Stampa i risultati a schermo
print("Litri di benzina totali: {} lt\nQuota individuale: {} €".format(litri_tragitto,quota_individuale))

plot = False

if plot:
    from matplotlib import pyplot
    pyplot.scatter(*zip(*data))
    pyplot.scatter(km_tragitto, litri_tragitto, color='tab:red')
    pyplot.show()