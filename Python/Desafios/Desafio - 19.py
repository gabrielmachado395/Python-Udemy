# Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.

# For instance:

# camelcase("hello case") => HelloCase
# camelcase("camel case word") => CamelCaseWord
# Don't forget to rate this kata! Thanks :)

def camel_case(string):
    return ''.join(string.title().replace(" ", ''))