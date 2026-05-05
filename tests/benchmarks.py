import time
import phystensor as pt
import numpy as np

def benchmark_matrix_ops():
    # Measure the overhead of physical validation vs raw NumPy
    size = 500
    data = np.random.rand(size, size)
    
    # Raw NumPy
    start = time.time()
    _ = np.dot(data, data)
    numpy_time = time.time() - start
    
    # Phystensor
    t1 = pt.q(data, "m")
    t2 = pt.q(data, "m")
    start = time.time()
    _ = pt.linalg.dot(t1, t2)
    pt_time = time.time() - start
    
    print(f"\nBenchmark (Size {size}x{size}):")
    print(f"Raw NumPy: {numpy_time:.4f}s")
    print(f"Phystensor: {pt_time:.4f}s")
    print(f"Overhead: {((pt_time/numpy_time)-1)*100:.2f}%")

if __name__ == "__main__":
    benchmark_matrix_ops()
