# AST-Project

## Group Members:

* Jasmine Padhye
* Akash Hulihalli

#### Updates till 17.12.2018:
* Integrated Travis CI platform.
* Solved bugs in code.
* Developed a proper README.md file.
* Integrated CodeFactor for testing code quality.
* Added badges to README.md file. 

#### Updates till 09.12.2018:

- Objects are created for sensor inputs to implement Image matching algorithm or RGB-D Object Detection and Semantic Segmentation for Autonomous Manipulation in Clutter according to the updated requirement.
- Number of objected detected are counted by object number rather than length of list.
This helps to detect correct number of objects in case of separate or repeating objects, like input 5 and 6.
- Merge sensor data module is added to combine all the sensor data into one single list. This helps in creating objects in a simpler manner.
- The objects with same object number are compared and the one with higher percentage is created into object. 
This is done in a single module and no duplicates are created.
- Condition for empty list is also updated.

<br>

#### Submission for 09.12.2018:

| Test function | Description |
|---------------|-------------|
| test_count_number_of_sensors | This test case tests the number of input sensors counted |
| test_detect_number_of_objects | This test case tests the number of objects detected |
| test_merge_sensor_data | This test case tests the length of merged list which is summation of elements of all the input sensors |
| test_create_final_objects | This test case tests if the object names and object percentages are correct and in true sequence |



#### Submission till 02.12.2018:
* The required output met
* It has been taken care of increasing number of sensor inputs in further requirements
* The structure of program was properly discussed and implemented
* The code is divided into small tasks which hopefully should allow us to expand the code for further requirements rather than modifying

#### Report of output till 02.12.2018 with updated requirements:
- Input1: <br>
sensor1 = [(knife,1, 99%), (scissor, 2, 65%), (spoon, 3, 33%), (spoon, 4, 80%), (keys, 5, 95%)]
<br>
sensor2 = [ (keys, 5, 95%), (spoon, 4, 99%),(fork, 3, 99%), (scissor, 2, 95%), (knife,1, 55%)]
<br>
<br>
Output:
These inputs counted the correct number of sensors and objects, 
but object names assigned were in opposite sequence.
<br>
<br>
- Input2:<br>
sensor1 = [(empty list)] <br>
sensor2 = [(empty list)] <br>
<br>
Output: 
These inputs counted the correct number of sensors and objects,
but threw error in detecting and creating objects.
<br>
<br>
- Input3: <br>
sensor1 = [(knife,1, 99%), (scissor, 2, 65%), (spoon, 3, 33%)] <br>
sensor2 = [(empty list)] <br>
<br>
Output:
These inputs did not throw any errors and created the desired output.
<br>
<br>
- Input4: <br>
sensor1 = [(knife,1, 99%), (scissor, 2, 65%), (spoon, 3, 33%)] <br>
sensor2 = [(KNIFE,1, 99%), (SCISSOR, 2, 65%), (SPOON, 3, 33%)] <br>
<br>
Output:
These inputs did not throw any errors and created desired output.
<br>
<br>
- Input5: <br>
sensor1 = [(knife,1, 99%), (scissor, 2, 65%)] <br>
sensor2 = [(fork, 3, 99%), (spoon, 4, 99%)] <br>
<br>
Output:
These inputs counted the correct number of sensors but detected wrong number of objects. And so, gave undesired output.
<br>
<br>
- Input6:<br>
sensor1 = [(knife,1, 94%),(knife,1, 69%),(knife,1, 89%)] <br>
sensor2 = [(knife,1, 99%),(fork, 3, 99%)] <br>
<br>
Output:
These inputs counted correct number of sensors but wrong number of objects and so the output was undesired.
<br>
<br>

