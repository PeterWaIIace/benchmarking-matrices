import time 
import random
import numpy as np
import jax.numpy as jnp
import matplotlib.pyplot as plt

from pbar import printProgress

def mul_mat(length,repeat = 1):
    loops_times = []
    numpy_times = []
    jax_times = []
    samples = []

    start = time.time()
    end = time.time()     

    length = length
    for n in range(1,length,1):
        printProgress(n/length)
        i = n*n
        samples.append(i)

        array_2 = [[random.random() for y in range(i) ] for x in range(i)]
        array_1 = [[random.random() for y in range(i) ] for x in range(i)]
        array_output = [[0.0 for y in range(i) ] for x in range(i)]

        np_array_1 = np.array(array_1)
        np_array_2 = np.array(array_2)
        np_array_out = np.array(array_output)

        jnp_array_1 = jnp.array(array_1)
        jnp_array_2 = jnp.array(array_2)
        jnp_array_out = jnp.array(array_output)

        avg_time = 0
        for _ in range(repeat):
            start = time.time()
            for j,col in enumerate(array_output):
                for m, _ in enumerate(col):
                    array_output[j][m] += array_2[j][m] * array_1[m][j]
            end = time.time()
            avg_time += end - start

        avg_time = avg_time/repeat
        loops_times.append(avg_time)

        avg_time = 0
        for _ in range(repeat):
            start = time.time()
            np_array_out = np.matmul(np_array_1,np_array_2)
            end = time.time()
            avg_time += end - start

        avg_time = avg_time/repeat
        numpy_times.append(avg_time)

        avg_time = 0
        for _ in range(repeat):
            start = time.time()
            jnp_array_out = np.matmul(jnp_array_1,jnp_array_2)
            end = time.time()
            avg_time += end - start

        avg_time = avg_time/repeat
        jax_times.append(avg_time)

    plt.title('mat_mul')
    plt.xlabel('Array size')
    plt.ylabel('Time')
    plt.plot(samples,loops_times, label=f"loops_{repeat}")
    plt.plot(samples,numpy_times, label=f"numpy_{repeat}")
    plt.plot(samples,jax_times  , label=f"jax_{repeat}")
    ax = plt.gca()
    ax.set_ylim([0, 0.01])

mul_mat(40,40)
plt.legend()
plt.show()