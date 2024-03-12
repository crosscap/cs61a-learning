# note

## A Guide to Designing Function

- Give each function exactly one job, but make it apply to many related situations
- Don’t repeat yourself (DRY): Implement a process just once, but execute it many times
- Defines function **generally**

## Higher-order functions

- Express general mothods of computation
- Remove repetition from programs
- Separate concerns among functions

## Some benefit of using lambda expression

- Make the name space clean
- Replace a function when it is simple

Notice: lambda don't gave you more power and you do not need to write it at all.

## How to Draw an Environment Diagram

When a function is defined

1. Create a function value: func \<name\>(\<formal parameters\>) \[parent=\<label\>\]
   Its parent is the current frame.
2. Bind \<name\> to the function value in the current frame

When a function is called

1. Add a local frame, titled with the \<name\> of the function being called.
2. Copy the parent of the function to the local frame: \[parent=\<label\>\]
3. Bind the \<formal parameters\> to the arguments in the local frame.
4. Execute the body of the function in the environment that starts with the local frame.

## Choose Function's Name

- Names should convey the meaning or purpose of the values to which they are bound.
- The type of value bound to the name is best documented in a function's docstring.
- Function names typically convey their effect (`print`), their behavior (`triple`), or the value returned (`abs`).
