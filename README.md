<a href="https://chrome.google.com/webstore/detail/mathjax-plugin-for-github/ioemnmodlmafdkllaclgeombjnmnbima/related?hl=en-GB">
  <img src="https://lh3.googleusercontent.com/1L5qSmHCxs8ZD0wEVvj3J3GjUFRxSuYHfKjcp7K1PR3_kmRLT-RSSTYDmEh1LnSm3un9zwH8VnEQgaJ43G3ZiWq7Na-vR99o_TJ86DTCsFNiP9ugLTPoA_4eDO-PyEhts_WFX6QxPT0e8PA_u2J8aGm4vWITmrax9yHKdfedn1lbmM7gn5S_hsa2IQOX9d0WCXKYMRKCWRmTymIcRI9PF9MOLJx1-oIGhl4gLOG9nih_d8UoNNWaXrNaLI-Tr6KnCmh6B_jdcUtwwblmMmBMv4EjzJgjYhssZ3uRu0kdV42IQXVLUQObE0WC0ZRsfXmq_huhdb7nA-ed3Jay8HDv9XFg2L447bSd_wB4U2lG6G6mTYU7IjwpxXZLllzAsdqjP2740gD7p7tVKo0-NLRDnczhOSkdDtTHeCIjMwamkA2L60JN6ULiVur0TSVdpFaTPVPwUcaIBC6O3lB4bCKSbzOmssqhkqNk_njR8Ee0DyAyfkSx9uSltmA6MmDfnzncoyWVR7QKIIh1bx1G_8nDaFUbNIDGRS6E3o-7AseEycFaVgh0nBcgVfGQWmvHTdlScBHqolKrAIjBIlF2vcBdbkiNvX9TjV1KwK05i8JHBMcWcZSbaiwK5DFKlCNQUd65BRH7hbhIHSKKiZHNF52PHY9UwSJqAVHW9W6pX6BsLM37o6imtk75ZLbjzcPbWzXnoE21KrlfugBn701E1fRtQfODoRq0kq7m-rGVNAsEGXRU6LC2U3fIzO_FCgUBW-s4DEOfkof34Uhu4nmfQfbrl9oZiezDFCbe1PY6vsguKFhpV3jsBzAUmimvRtU5AfI=w893-h722-no?authuser=0" alt="MathJax Plugin for Github"> 
</a>

# Let's find a sequence of numbers with the same Step between them knowing two numbers.

# <p align="right"> $ Step = {{Greater - Lower}\over{Amount - 1}} $ </p> <p align="center"><b>`&`</b></p> <p align="left"> $ Amount = 1 + {{Greater - Lower} \over Step} $ </p>

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
