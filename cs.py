import numpy as np
import time
import random
import os
from datetime import datetime

def auto_save(original, sorted_result, time_ms):
    os.makedirs("results", exist_ok=True)
    filename = f"results/sort_{len(original)}_{datetime.now().strftime('%H%M%S')}.txt"
    
    with open(filename, 'w') as f:
        f.write(f"# {datetime.now()} | 大小:{len(original)} | 时间:{time_ms:.3f}ms\n")
        f.write(f"原始: {' '.join(map(str, original))}\n")
        f.write(f"排序: {' '.join(map(str, sorted_result))}\n")

def test():
    try:
        import fast_sort
        print("排序测试 (输入 q 退出)")
        
        while True:
            inp = input("数字:（使用空格分隔）").strip()
            if inp.lower() == 'q': break
            
            try:
                if inp.startswith('r'):
                    n = int(inp[1:]) if len(inp) > 1 else 10
                    arr = [random.randint(1, 100) for _ in range(n)]
                else:
                    arr = [int(x) for x in inp.split()]
                
                if not arr: continue
                
                start = time.perf_counter()
                result = fast_sort.ultimate_sort(np.array(arr, dtype=np.int32))
                ms = (time.perf_counter() - start) * 1000
                
                sorted_list = result.tolist()
                print(f"{sorted_list} ({ms:.3f}ms)")
                
                auto_save(arr, sorted_list, ms)
                
            except Exception as e:
                print("")
                #预留位置
    
    except ImportError:
        print("")
        #预留位置
if __name__ == "__main__":
    test()
