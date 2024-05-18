# note

## A Guide to Designing Function

- Give each function exactly one job, but make it apply to many related situations
- Don’t repeat yourself (DRY): Implement a process just once, but execute it many times
- Defines function *generally*

## Excellent composition guidline

- *Names*. To a computer, names are arbitrary symbols: "xegyawebpi" and "foo" are just as meaningful as "tally" and "denominator". To humans, comprehensible names aid immensely in comprehending programs. Choose names for your functions and values that indicate their use, purpose, and meaning. See the lecture notes section on choosing names for more suggestions.
- *Functions*. Functions are our primary mechanism for abstraction, and so each function should ideally have a single job that can be used throughout a program. When given the choice between calling a function or copying and pasting its body, strive to call the function and maintain abstraction in your program. See the lecture notes section on composing functions for more suggestions.
- *Purpose*. Each line of code in a program should have a purpose. Statements should be removed if they no longer have any effect (perhaps because they were useful for a previous version of the program, but are no longer needed). Large blocks of unused code, even when turned into comments, are confusing to readers. Feel free to keep your old implementations in a separate file for your own use, but don't turn them in as your finished product.
- *Brevity*. An idea expressed in four lines of code is often clearer than the same idea expressed in forty. You do not need to try to minimize the length of your program, but look for opportunities to reduce the size of your program substantially by reusing functions you have already defined.

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

## Objects

- Objects represent information
- They consist of data and behavior, bundled together to create abstractions
- Objects can represent things, but also properties, interactions, & processes
- A type of object is called a class; *classes* are first-class values in Python

## Object-oriented programming

- A metaphor for organizing large programs
- Special syntax that can improve the composition of programs

## Classes

A class serves as a template for its instances.

## The relationship between class and object

- A class combines (and abstract) data and functions
- A obiect is an instantation of a class

## The relationship between date abstraction and object oriented programming

- data
- functions
    - constructor (`__init__`)
        - allocate memory for the object
        - initializes the object with values
        - returns address of the object
    - selectors
    - methods (functions)

## When a class is called

1. A new instance of the class is created
2. The `__init__` method is called with the instance as its first argument (named `self`), along with any additional arguments provided in the call expression.

## Methods and Functions

- Functions, which we have been creating since the beginning of the course, and
- Bound methods, which couple together a function and the object on which that method will be invoked
    > object + function = bound method

## Looking Up Attribute Names on Classe

1. If the object is an instance, then assignment sets an instance attribute
2. If it names an attribute in the class, return the attribute value.
3. Otherwise, look up the name in the base class, if there is one.
4. If the attribute is a function, return a bound method.

## Designing for Inheritance

- Don't repeat yourself; use existing implementations
- Attributes that have been overridden are still accessible via class objects
- Look up attributes on instances whenever possible

## Inheritance and Composition

- Inheritance is best for representing is-a relationships
- Composition is best for representing has-a relationships

## Bilid Generic Functions Skills

- Type Dispatching
- Type Coercion

## Scheme Expressions

Scheme programs consist of expressions, which can be:

- Primitive expressions
- Combinations

Numbers are self-evaluating; symbols are bound to values

Call expressions include an operator and 0 or more operands in parentheses

## Multiple try statements

Control jumps to the except suite of the most recent try statement that handles that type of exception

## Pure Functions

- No re-assignment and no mutable data types
- Name-value bindings are permanent

## Advantages of functional programming

- The value of an expression is independent of the order in which sub-expressions are
evaluated
- Sub-expressions can safely be evaluated in parallel or only on demand (lazily)
- Referential transparency: The value of an expression does not change when we substitute
one of its subexpression with the value of that subexpression

## Tail Call

A tail call is a call expression in a tail context:

- **The last body sub-expression in a lambda expression**
- **Sub-expressions 2 (consequent) & 3 (alternative) in a tail context if expression**
- All non-predicate sub-expressions in a tail context cond
- The last sub-expression in a tail context and, or, begin, or let

## How to Design Programs

### From Problem Analysis to Data Definitions

Identify the information that must be represented and how it is represented in the chosen programming language. Formulate data definitions and illustrate them with examples.

### Signature, Purpose Statement, Header

State what kind of data the desired function consumes and produces. Formulate a concise answer to the question what the function computes. Define a stub that lives up to the signature.

### Functional Examples

Work through examples that illustrate the function’s purpose.

### Function Template

Translate the data definitions into an outline of the function.

### Function Definition

Fill in the gaps in the function template. Exploit the purpose statement and the examples.

### Testing

Articulate the examples as tests and ensure that the function passes all. Doing so discovers mistakes. Tests also supplement examples in that they help others read and understand the definition when the need arises—and it will arise for any serious program.
