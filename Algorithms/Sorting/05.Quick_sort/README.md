# 🧮 Sorting Algorithms in Python

A simple and beginner-friendly repository containing popular **sorting algorithms** implemented in **Python**, along with explanations, examples, and time/space complexities.

---

## 📚 Algorithms Covered

- 🫧 Bubble Sort  
- ⚡ Quick Sort  

---

## 🫧 Bubble Sort Algorithm

![Algorithm](https://img.shields.io/badge/Algorithm-Bubble%20Sort-blue)
![Time](https://img.shields.io/badge/Time%20Complexity-O(n²)-red)
![Space](https://img.shields.io/badge/Space%20Complexity-O(1)-green)

### 📌 About
Bubble Sort ek **simple comparison-based sorting algorithm** hai.  
Isme adjacent elements ko compare kiya jata hai aur agar wo galat order mein ho, to swap kar diya jata hai.

Har pass ke baad **largest element end mein bubble up** ho jata hai.

---

### 🧠 How Bubble Sort Works
1. First element se start karo
2. Adjacent element ke saath compare karo
3. Agar current element bada ho, to swap karo
4. End tak repeat karo
5. Jab tak koi swap na ho, process repeat hota rahega

---

### 🪜 Algorithm Steps
1. Loop `i = 0` se `n-1` tak
2. `swapped = False` set karo
3. Adjacent elements compare karo
4. Agar `arr[j] > arr[j+1]`, swap karo
5. Agar ek pass mein koi swap nahi hua, break karo

---

### 📊 Example
**Input:**
```text
nums = [5, 1, 4, 2]
Pass 1: [1, 5, 4, 2]
        [1, 4, 5, 2]
        [1, 4, 2, 5]

Pass 2: [1, 2, 4, 5]
Pass 3: No swaps → Sorted

```

## 🧑‍💻 Implementation
```python 
def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        
        if not swapped:
            break
    
    return nums
