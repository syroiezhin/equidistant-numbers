# <p id="UP">Want to find a sequence of numbers with the same step between two numbers you specify?</p>

#
<p align="right">
  $$ Step = \left( \frac{Greater - Lower}{Amount - 1} \right
</p>

<p align="left">
  $$ Amount = 1+ \left( \frac{Greater - Lower}{Step} \right) $$
</p>

## <p align="center">Give thanks : <u>5168 7450 1701 5535</u> <a href="https://en.privatbank.ua/all-ways-to-receive-send-an-international-transfer"><img src="https://upload.wikimedia.org/wikipedia/uk/f/ff/%D0%9B%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF_%D0%9F%D1%80%D0%B8%D0%B2%D0%B0%D1%8224.png" width = "25" alt="Privat Bank UA"> </a></p>

> We ask the user to enter two numbers in any order.
- [X] `input("Enter: ")`
> We turn the text into an array of characters using the presence of a space as a delimiter.
- [X] `input("Enter: ").split()`
> We change the data type of the resulting array to int.
- [X] `map(int,input("Enter: ").split())`
> We swap the parameters so that their values match the variable names.
- [X] `if L >= G: L,G = G,L`
> We change the first character of a string to an uppercase letter and all other alphabets to lowercase.
- [X] `Q.capitalize()`
> We check the presence of the received element in the array of possible answers.
- [X] `any(a.capitalize() in urAnswer for urAnswer in ["A","Ab","Abc"])`
> We want to make the array reversible, for this we add [::-1] at the end of the called array.
- [X] `["1","2","3"] ⮕ ["3","2","1"]`
> We want to create a string with array values separated by a comma.
- [X] `', '.join([str(parameter) for parameter in [3,2,1]]) ⮕ 3,2,1`

[⇪](#UP)
