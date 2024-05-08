# `robot_one`

這個資料夾包含了用於在模擬中使用 `uwb_localization` 套件的機器人程式碼和配置文件。

## 套件結構

套件結構如下：

- `launch`: 包含啟動模擬的啟動文件。
- `src`: 包含機器人的源代碼和配置文件。
- `config`: 包含機器人的配置文件。

## 依賴性

`robot_one` 套件依賴以下套件：

- `uwb_localization`: 提供超廣頻定位功能。

## 安裝
The package u need:
```bash
sudo apt-get install ros-foxy-xacro
sudo apt-get install ros-foxy-ros2-control
sudo apt-get install ros-foxy-ros2-controllers
sudo apt-get install ros-foxy-twist_mux
```
- For gazebo sim:
```bash
sudo apt install ros-foxy-ros2-control ros-foxy-ros2-controllers ros-foxy-gazebo-ros2-control
```
## 使用方法
要啟動模擬，請執行以下命令：
```bash
ros2 launch robot_one launch_uwb_bot.launch.py
```
這將啟動 robot_one 套件，並使用 uwb_localization 套件進行模擬。

## 啟動文件
套件包含以下啟動文件：

`launch_uwb_bot.launch.py`: 啟動模擬，並使用 `uwb_localization` 套件。
配置文件
套件包含以下配置文件：
- `config/robot_one.yaml: `機器人的配置文件。
您可以根據需要修改這些文件