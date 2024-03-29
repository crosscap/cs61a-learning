# note

## A Guide to Designing Function

- Give each function exactly one job, but make it apply to many related situations
- Don’t repeat yourself (DRY): Implement a process just once, but execute it many times
- Defines function *generally*

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

1. Create a function value: func \<name\>(\<formal parameters\>) [parent=\<label\>]
   Its parent is the current frame.
2. Bind \<name\> to the function value in the current frame

When a function is called

1. Add a local frame, titled with the \<name\> of the function being called.
2. Copy the parent of the function to the local frame: [parent=\<label\>]
3. Bind the \<formal parameters\> to the arguments in the local frame.
4. Execute the body of the function in the environment that starts with the local frame.

## Choose Function's Name

- Names should convey the meaning or purpose of the values to which they are bound.
- The type of value bound to the name is best documented in a function's docstring.
- Function names typically convey their effect (`print`), their behavior (`triple`), or the value returned (`abs`).

## What happens when you call Recursion Function

- The same function `fact` is called multiple times
- Different frames keep track of the different arguments in each call
- What `n` evaluates to depends upon the current environment
- Each call to `fact` solves a simpler problem than the last: smaller `n`

## The Recursive Leap of Faith

1. Verify the base case
2. Treat `fact` as a functional abstraction!
3. Assume that `fact(n-1)` is correct
4. Verify that `fact(n)` is correct

## Converting Recursion to Iteration

Can be tricky: Iteration is a special case of recursion.

Idea: Figure out what state must be maintained by the iterative function.

## Converting Iteration to Recursion

More formulaic: Iteration is a special case of recursion.

Idea: The state of an iteration can be passed as arguments.

## Data Abstraction

- Lets us manipulate compound values as units
- Isolate two parts of any program that uses data
    - How data are represented (as parts)
    - How data are manipulated (as units)

## Excellent composition guidline

- *Names*. To a computer, names are arbitrary symbols: "xegyawebpi" and "foo" are just as meaningful as "tally" and "denominator". To humans, comprehensible names aid immensely in comprehending programs. Choose names for your functions and values that indicate their use, purpose, and meaning. See the lecture notes section on choosing names for more suggestions.
- *Functions*. Functions are our primary mechanism for abstraction, and so each function should ideally have a single job that can be used throughout a program. When given the choice between calling a function or copying and pasting its body, strive to call the function and maintain abstraction in your program. See the lecture notes section on composing functions for more suggestions.
- *Purpose*. Each line of code in a program should have a purpose. Statements should be removed if they no longer have any effect (perhaps because they were useful for a previous version of the program, but are no longer needed). Large blocks of unused code, even when turned into comments, are confusing to readers. Feel free to keep your old implementations in a separate file for your own use, but don't turn them in as your finished product.
- *Brevity*. An idea expressed in four lines of code is often clearer than the same idea expressed in forty. You do not need to try to minimize the length of your program, but look for opportunities to reduce the size of your program substantially by reusing functions you have already defined.
