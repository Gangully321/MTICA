diff b/w return and yield:
return:
    1.return  the the result to the caller.
    2.Destroys the variables once exexution is complete.
    3.There is usualy one return statement per function.

        4.If you execute a function again it starts from begining.

yield:
    1.used to convert a function to a generator.
    Suspends the function preserving its state
    2.yield does not destroy the functions local variables.
    preserve the state
    3.There can be one or more yield statements,which is quite commom.
    4.The execution begins from where it was previously paused/freezed
