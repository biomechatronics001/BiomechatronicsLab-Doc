Knee Exoskeleton (25 Nm)
========================

Overview
--------

To be filled in...

Setup
-----

To be filled in...

Usage
-----

To be filled in...

Issue Tracker
-------------

Mechanical
^^^^^^^^^^

#. Thigh bar (small size) is still too long for some subjects, causing bad knee alignment. | **Source**: Bronx VA, 04/11/2024.

   .. image:: /resources/robots/knee_exo_25Nm/long_thigh_bar.png
      :align: center
      :width: 500

   **Solution:** ``ToDo``, probably need a even shorter thigh bar.

#. Passive DoF on the shank brace causes the exo shank portion to flip outwards. | **Source**: Bronx VA, 04/11/2024.

   .. raw:: html

    <iframe width="315" height="560"
    src="https://www.youtube.com/embed/PE1g-2u93YM"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;     picture-in-picture; web-share"
    allowfullscreen></iframe>

   **Solution:** ``ToDo``, probably need to limit the range of motion of the passive DoF.

Electrical
^^^^^^^^^^

#. Teensy reset via button does not work. | **Source**: Bronx VA, 02/23/2024.

   **Solution:** ``ToDo``, Ivan suggested that the ground pin of Teensy may be not well connected.

#. Bluetooth communication is not stable. Needs to find a way to re-establish the connection without powering off the entire system then turning them on again. | **Source**: Bronx VA, 02/23/2024.

   **Solution:** ``ToDo``, no good solution now.

#. Motors cannot be controlled sometimes. | **Source**: Bronx VA, 02/23/2024.

   **Solution:** One possibility is that the motor internal control parameters are accidentally wiped when the motor is not properly turned off according to Tmotor support team. If it is the case, open CubeMars GUI and connect the motor to the PC. Access MIT mode, go to setup in the command window (hitting DEBUG in the MIT window), set ``set_band_width`` to 1000 and set ``set_current _limit`` to 60 with the commands shown in the screen, and then run "calibrate" also with the command window. After pressing "setup", the following information should be displayed.

   .. image:: /resources/robots/knee_exo_25Nm/CubeMars_Bandwidth_CurrentLimit.png
      :align: center
      :width: 700

   .. attention:: 
    
    ALWAYS press "exit" in the GUI before powering off the motor.

#. One motor seems to activate later than the other motor. | **Source**: Bronx VA, 02/23/2024.

   .. raw:: html

    <iframe width="315" height="560"
    src="https://www.youtube.com/embed/ejiUhUiGlcg"
    title="YouTube video player"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope;     picture-in-picture; web-share"
    allowfullscreen></iframe>


   **Solution:** This is because the motor CAN communication is not properly initialized. Each time the control box is powered on, please re-upload the control program to Teensy via USB cable so that motor CAN communication is initialized correctly.

#. One motor seems to cause jerky feeling to the subject during walking; one motor is ramping up faster than the other. | **Source**: Bronx VA, 02/23/2024.

   **Solution:** This is because the motor CAN communication is not properly initialized. Each time the control box is powered on, please re-upload the control program to Teensy via USB cable so that motor CAN communication is initialized correctly.

Wearable
^^^^^^^^

#. The participants felt the brackets were uncomfortable, so we ended up adding a relatively dense foam pad to redistribute the pressure. Although since they were not part of the bracket they would occasionally fall out. Is it possible to integrate additional padding into the brackets? | **Source**: Bronx VA, 02/23/2024. 

   **Solution:** Added padding between brace and strap.

#. Upper thigh braces (TU60, TL55) are not large enough for some patients. | **Source**: Bronx VA, 02/23/2024.

   **Solution:** We printed TU65 and TL60 and sent to Bronx VA.

#. The brackets above and below the knee are very close to the joint. The straps for the bracket below the knee push into the popliteal fossa when the users were sitting causing discomfort. If we slide the device down the above knee bracket ends up over the patella causing discomfort. Is there a way to move the brackets further away from the knee joint? | **Source**: Bronx VA, 02/23/2024.

   .. image:: /resources/robots/knee_exo_25Nm/shank_upper_strap_push_into_knee.png
      :align: center
      :width: 700

   **Solution:** New shank pads are shorter and narrower so it does not bump into the knee.


Controller
^^^^^^^^^^

#. Sit2stand controller needs to be improved: stand up without leaning the trunk forward will delay the activation of assistance or does not trigger at all; leg movements during sitting phase will wrongly trigger the assistance. | **Source**: Bronx VA, 02/23/2024.

   **Solution:** ``ToDo``, will try to use only 2 IMUs (one per thigh). Will be implemented in: ``/Dropbox/BiomechatronicsLab/Projects/Knee Osteoarthritis Exoskeleton/Code/Tmotor version - 20240413`` (in progress).

#. Sit2stand controller: separate magnitude for sit2stand and stand2sit. One subject like smaller assistance from stand2sit and larger assistance for sit2stand. | **Source**: Bronx VA, 02/23/2024.

   **Solution:** ``ToDo``, will have separate control of assistance magnitude during stand-up phase and sit-down phase. Will be implemented in: ``/Dropbox/BiomechatronicsLab/Projects/Knee Osteoarthritis Exoskeleton/Code/Tmotor version - 20240413`` (in progress).


Miscellaneous
^^^^^^^^^^^^^

#. Bronx VA is not able to download CubeMars tool on their work laptop or personal laptop. Windows Firewall or Chrome treated it as a virus and deleted the file right after it is downloaded. The CubeMars tool is useful for debugging motor issues.

   **Solution:** ``ToDo``, maybe we will mail an USB drive that contains the tool to Bronx VA.



