# Scanner 

### Symbol Table

I had to implement 2 symbol tables, one for the constants and one for de identifiers.
For the representation I used a custom Hash Table that has as methods the following: hash(that generates and returns the
new hashed position for a new element that will be added), contains( a function that verifies if the hashtable contains a certain key), 
remove(removes a key), add( appends a new key to the generated hash pos),
getPos(returns the position of a key as a tuple)

The symbol table is a wrapper for the hashmap.

The Scanner generates tokens that represent either a reserved word, a separator, an operator, an identifier or a constant,
searching char by char, not separating by space.
