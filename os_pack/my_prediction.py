import numpy as np
#import Bitcoin_model.plk

def my_prediction():
    # Step one pickel model and load pickeled model into here
    my_model = np.load("Bitcoin_model.pkl", allow_pickle=True, fix_imports=True)
    # Step two extract user argument (arg1) use it to make prediction
    my_prediction = my_model.preict(T_train.reshape(1245,1))
    # Step 3 get predcition into json form to pass through rest API
    my_predstr = my_prediction.tolist()
    my_predstr = json.dump(my_predstr)
    str = [my_predstr]
    return str

