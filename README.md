# `robot_one`

這個資料夾包含了用於在模擬中使用 `uwb_localization` 套件的機器人程式碼和配置文件。

## 套件結構

套件結構如下：

- `launch`: 包含啟動模擬的啟動文件。
- `src`: 包含機器人的源代碼和配置文件。
- `config`: 包含機器人的配置文件。

## 安裝:
**Run following script file**
```bash
# 確認你的檔案路徑在src下
chmod +x clone_repos.sh
./clone_repos.sh
```

The package u need:
```bash
sudo apt-get install ros-foxy-xacro
sudo apt-get install ros-foxy-ros2-control ros-foxy-gazebo-ros2-control
sudo apt-get install ros-foxy-ros2-controllers
sudo apt-get install ros-foxy-twist-mux
```

## USB permission:
若在連接時遇到USB Permission Denied的問題
```bash
sudo usermod -a -G dialout $USER
reboot
```

## 使用方法：
### YOLOv5s human following:
這將啟動 yolo 以及robot_follower，並使用 uwb_localization 進行跟隨。
**Setp 1:攝影機連接**
連接上攝影機。
**Step 2:F710搖桿連接**
接上搖桿的無線接收器，收納在搖桿電池蓋下。
**Setp 3:運行YOLO**
注意：需要特別用venv 建一個虛擬環境給yolo，不然pytorch會更新setuptools，較新版的setuptools會使得foxy沒辦法編譯。
```bash
ros2 launch detection detect.launch.py
```
**Setp 4:機器人launch file**
```bash
ros2 launch robot_one launch_human_bot.launch.py
```
**Setp 5:STM32連接**
接上機器人上連接STM32的USB線，運行：
```bash
ros2 launch robot_one launch_stm32.launch.py
```
若畫面顯示找不到serial poart，就透過
```bash
ls -l /dev/ttyACM*
```
確認一下新接上去的stm32的接口編號，然後去修改`launch_stm32.launch.py`程式。
**Setp 5:Reset STM32**
有連接上後，去按一下STM32上的Reset鍵(塑膠盒上有挖了一個洞方便你按)。

### UWB human following:
這將啟動 uwb_localization 以及robot_follower_cpp，並使用 uwb_localization 進行跟隨。
**Setp 1:UWB連接**
連接上USB Hub，上面包含Arduino以及三個UWB模組，沒意外的話電腦Serial Port的編號會和程式裡面預設的一樣。若有不一樣請去`uwb_localization`這個pakage裡面修改`localization.py`的程式。
**Step 2:F710搖桿連接**
接上搖桿的無線接收器，收納在搖桿電池蓋下。
**Setp 3:機器人launch file**
```bash
ros2 launch robot_one launch_uwb_bot.launch.py
```
**Setp 4:STM32連接**
接上機器人上連接STM32的USB線，運行：
```bash
ros2 launch robot_one launch_stm32.launch.py
```
若畫面顯示找不到serial poart，就透過
```bash
ls -l /dev/ttyACM*
```
確認一下新接上去的stm32的接口編號，然後去修改`launch_stm32.launch.py`程式。
**Setp 5:Reset STM32**
有連接上後，去按一下STM32上的Reset鍵(塑膠盒上有挖了一個洞方便你按)。
