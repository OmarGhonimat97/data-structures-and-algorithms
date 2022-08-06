# Hashtables
<!-- Short summary or background information -->
Hashtables are a data structure that utilize key value pairs. This means every Node or Bucket has both a key, and a value.


## Challenge
<!-- Description of the challenge -->
Implement a Hashtable Class with the following methods:
- set 
- get
- contains
- keys
- hash


## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->

Time Complexity: O(1)

## API
<!-- Description of each method publicly available in each of your hashtable -->

- set : This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
- get : Returns Value associated with key received in the table
- contains: Returns Boolean, indicating if the key exists in the table already.
- keys: Returns Collection of keys
- hash: Returns Index in the collection for that key