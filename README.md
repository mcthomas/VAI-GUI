<img src="static/temp.PNG" width="300"/>

# V.A.I. - Visual Aided Interface | HackMIT 2020 

##### Backend - Robotics led by [Gokulraj K.S](mailto:gokulrajks@pesu.pes.edu)
##### Frontend - GUI and design led by [Matt Thomas](mailto:mcthomas4@wisc.edu) / API implementations led by [Ipshita Joshi](mailto:ipshitameghal.joshi2017@vitstudent.ac.in) 

## Contents

  - [Introduction](#Introduction "Introduction")
  - [Additonal GUI Server Dependencies](#Additonal-GUI-Server-Dependencies "Additional GUI Server Dependencies")
  - [Usage](#Usage "Usage")
  
  ## Introduction
  
In order to assist those who are restricted to wheelchairs or otherwise impaired by paralysis, we are aiming to assist their daily life through gesture controls, image processing, and voice command features.  Interfacing in this way allows the user to move between rooms, make emergency calls, and order food and transportation services.  This project serves as the frontend GUI aid for remotely controlling the simulated robotics, written in HTML, CSS, JS, and wrapped with Python via a [flask](https://github.com/pallets/flask) server.  Made for the HackMIT 2020 Health Tech.
  
  ## Additional GUI Server Dependencies
  
  ```
$ pip install -U Flask
$ pip install twilio
$ pip install pizzaapy
$ pip install xmltodict
```
  
  ## Usage

Intended for use with eye blink tracking software such as [OpenCV](https://github.com/opencv/opencv) w/ [dlib](https://github.com/davisking/dlib), with simulated robotics via [gazebo](https://github.com/osrf/gazebo), [rviz](https://github.com/ros-visualization/rviz), [tinkercad](https://www.tinkercad.com), and [ROS packages](https://github.com/ros/ros).  Some functions are purely hypothetical without configuration, so footage of backend simulated robotics is included in their place.  The server can be demoed (without the automated tabbing) with mouse clicks by simply cloning the project and running:
```
$ python app.py
```

  #### Footage:
