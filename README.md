# burgerking_drawing
肥宅們抽老婆...我是說抽漢堡囉！

---

### 執行檔

#### 單抽 
> pack > bk.exe

#### Powershell 十連抽

    $counter = 0
    $max_count = 10
    while ($counter -lt $max_count) {
        start-process "bk.exe"       
        start-sleep -seconds 2         
    $counter++
    }
    
---

### Command 環境需求
- Python 3.10 (我不確定)
- 安裝 selenium

    ` $pip install selenium `

---

### Python Command Line

#### 單抽

    python bk.py

#### 十連抽
 
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

