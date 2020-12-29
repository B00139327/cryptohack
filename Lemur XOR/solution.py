import numpy as np
import matplotlib.pyplot as plt
import imageio

def get_flag(input_data):
    flag = np.array(imageio.imread('/home/kali/Desktop/cryptohack/Lemur XOR/flag.png'),dtype = np.int64)
    lemur = np.array(imageio.imread('/home/kali/Desktop/cryptohack/Lemur XOR/lemur.png'),dtype = np.int64)

    plt.imshow(flag ^ lemur)
    plt.show()

    return None

input_data = None

get_flag(input_data)