# burgerking_drawing
肥宅們抽老婆...我是說抽漢堡囉！

---

### 環境需求
- Python 3.10 (我不確定)

---

### 單抽
command line

    python bk.py


---

### 十連抽
 command line

    $counter = 0
    $max_count = 10
    while ($counter -lt $max_count) {
        python bk.py
        $counter++
    }

---


### 已知Issue

- 因為我懶所以我直接用sleep等script載入，如果非洲線可能會失敗，記得去把等待時間調高
    time.sleep("second")

