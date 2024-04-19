import time 
import random
import numpy as np
import jax.numpy as jnp
import matplotlib.pyplot as plt

from pbar import printProgress

def add_number(length,repeat = 1):
    value_to_add = 1432
    loops_times = []
    numpy_times = []
    jax_times = []
    samples = []

    start = time.time()
    end = time.time()    

    for n in range(1,length,1):
        printProgress(n/length)
        i = n*10
        samples.append(i)

        array = [x for x in range(i)]
        np_array = np.array(array)
        jnp_array = jnp.array(array)

        for _ in range(repeat):
            start = time.time()
            for j,_ in enumerate(array):
                array[j] += value_to_add
            end = time.time()
        loops_times.append(end - start)

        for _ in range(repeat):
            start = time.time()
            np_array = np.add(np_array,value_to_add)
            end = time.time()
        numpy_times.append(end - start)

        for _ in range(repeat):
            start = time.time()
            jnp_array = jnp.add(jnp_array, value_to_add)
            end = time.time()
        jax_times.append(end - start)


    plt.title('add_number')
    plt.xlabel('Array size')
    plt.ylabel('Time')
    plt.plot(samples,loops_times, label=f"loops_{repeat}")
    plt.plot(samples,numpy_times, label=f"numpy_{repeat}")
    plt.plot(samples,jax_times  , label=f"jax_{repeat}")

add_number(500,20)
add_number(500,40)
plt.legend()
plt.show()