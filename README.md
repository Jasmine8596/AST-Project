# AST-Project

## Group Members:

* Jasmine Padhye
* Akash Hulihalli

#### Submission till 02.01.2018:
* The required output met
* It has been taken care of increasing number of sensor inputs in further requirements
* The structure of program was properly discussed and implemented
* The code is divided into small tasks which hopefully should allow us to expand the code for further requirements rather than modifying

#### Report of output till 02.01.2018 with updated requirements:
- Input: <br>
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
- Input:<br>
sensor1 = [(empty list)] <br>
sensor2 = [(empty list)] <br>
<br>
Output: 
These inputs counted the correct number of sensors and objects,
but threw error in detecting and creating objects.
<br>
<br>
- Input: <br>
sensor1 = [(knife,1, 99%), (scissor, 2, 65%), (spoon, 3, 33%)] <br>
sensor2 = [(empty list)] <br>
<br>
Output:
These inputs did not throw any errors and created the desired output.
<br>
<br>
- Input: <br>
sensor1 = [(knife,1, 99%), (scissor, 2, 65%), (spoon, 3, 33%)] <br>
sensor2 = [(KNIFE,1, 99%), (SCISSOR, 2, 65%), (SPOON, 3, 33%)] <br>
<br>
Output:
These inputs did not throw any errors and created desired output.
<br>
<br>
- Input: <br>
sensor1 = [(knife,1, 99%), (scissor, 2, 65%)] <br>
sensor2 = [(fork, 3, 99%), (spoon, 4, 99%)] <br>
<br>
Output:
These inputs counted the correct number of sensors but detected wrong number of objects. And so, gave undesired output.
<br>
<br>
- Input:<br>
sensor1 = [(knife,1, 94%),(knife,1, 69%),(knife,1, 89%)] <br>
sensor2 = [(knife,1, 99%),(fork, 3, 99%)] <br>
<br>
Output:
These inputs counted correct number of sensors but wrong number of objects and so the output was undesired.

