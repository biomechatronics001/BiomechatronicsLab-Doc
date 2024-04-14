Knee Exoskeleton (25 Nm)
========================

Issue Tracker
-------------

Mechanical
^^^^^^^^^^

#. Thigh bar (small size) is still too long for some subjects, causing bad knee alignment. | **Source**: Bronx VA, 04/11/2024.

   **Solution:** 

#. Passive DoF on the shank brace causes the exo shank portion to flip outwards. | **Source**: Bronx VA, 04/11/2024.

   **Solution:**

Electrical
^^^^^^^^^^

#. Teensy reset via button does not work.
#. Bluetooth communication is not stable, find a way to re-establish the connection without powering off the entire system then turning them on again.
#. Motors cannot be controlled sometimes

Wearable
^^^^^^^^

#. Umcomfort due to pressure between shank brace and shank [Solved]: added padding between brace and strap.
#. Upper thigh braces (TU60, TL55) are not large enough. [Solved]: printed TU65 and TL60
#. The brackets above and below the knee are very close to the joint. The straps for the bracket below the knee push into the popliteal fossa when the users were sitting causing discomfort. If we slide the device down the above knee bracket ends up over the patella causing discomfort. Is there a way to move the brackets further away from the knee joint? [Solved]: new shank pads are shorter so it does not bump into the knee

Controller
^^^^^^^^^^

#. Sit2stand controller needs to be improved: stand up without leaning the trunk forward will delay the activation of assistance or does not trigger at all; leg movements during sitting phase will wrongly trigger the assistance
#. Sit2stand controller: separate magnitude for sit2stand and stand2sit. One subject like smaller assistance from stand2sit and larger assistance for sit2stand.
#. Sit2stand controller: one motor seems to activate later than the other motor;
#. Walking controller: one motor seems to cause jerky feeling to the subject; one motor is ramping up faster than the other

