# SwimScript
SwimScript is an interpreted language that allows you to write and execute programs in a unique, competitive swimming-themed language. This language includes a set of keywords and is designed to manipulate data using a stack-based approach.

| Instruction | Description |
| ---------------------- | -------------------------------------------------------------------------------- |
| START | Initializes the stack with a 0 value. |
| STROKE | Increments by one. |
| COUNTDOWN | Decrements by one. |
| DIVING <number> | Pushes a specified number (representing depth or score) onto the stack. |
| SPLASH | Outputs the top value of the stack as a character. |
| SPLOOSH | Outputs the top value of the stack as an integer. |
| FINISH | Outputs the rest of what's on the stack. |
| LAP | Duplicates the top value of the stack. |
| FINISH | Pops all values from the stack and prints them as characters to produce the final output. This command effectively ends the execution of the program. |
| TAKEOVER | Converts the top value of the stack to an integer and pushes it back. |
| HEAT | Pops the top two values off the stack and pushes the result of their multiplication. |
| DIVE <line_num> | Conditional control to jump to a specified line if the top stack value is not zero. |
| EXIT <line_num> | Conditional control to jump to a specified line if the top stack value is zero. |
| STYLE FREE | Moves the top value to the top of the stack. |
| STYLE BACK | Moves the top value to the bottom (location 0) of the stack. |
| CALL | Prompts the user for input and pushes the character's ASCII value onto the stack. |
| HEAT | Multiplies the top two values of the stack. |
| FALSE START | Pops the top of the stack. |
