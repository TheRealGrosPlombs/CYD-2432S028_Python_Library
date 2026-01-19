# ESP32 Cheap Yellow Display Board 2432S028
  
Cheap Yellow Display Board 2432S028 python code to manage LCD and touchscreen

> **⚠️ Work in Progress:**  
> Not ready for production

[![Work in Progress](https://img.shields.io/badge/status-in_progress-yellow)](https://github.com/poivronjaune/ESP32-Robot-Ctrl)
![Last Commit](https://img.shields.io/github/last-commit/poivronjaune/ESP32-Robot-Ctrl)

---  

#     
# Introduction  
![image](/images/componentsV3.png)   

This project is divided in two main components.  
- The Robot itself with electronics, camera, motors, battery and blades  
- The External App that acts as the robot Brain to implement high level funtions to control the robot actions    

> Note: We chose to have an RTSP feed independant of the micro-controller for performance reasons. When both the motor controls and ESP32Cam were implemented on a single board too much lag was introduced in the system to work properly.  
> Instead of using an IP Camera, an ESP32CAM can be implemented but we recommend using two different micro-controllers.  

