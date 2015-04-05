def generate_concept_HTML(concept_title, concept_description):
    html_text_1 = '''
    <div class="concept">
      <div class="concept-title">
        ''' + concept_title
    html_text_2 = '''
      </div>
      <div class="concept-description">
        ''' + concept_description
    html_text_3 = '''
      </div>
    </div>'''
    full_html_text = html_text_1 + html_text_2 + html_text_3
    return full_html_text

def make_HTML(concept):
    concept_title = concept[0]
    concept_description = concept[1]
    return generate_concept_HTML(concept_title, concept_description)

My_Notes = [ 
[
'Programming Language',
'A programming language is what programmers use to tell a computer what to do. Python is one example of a programming language.'
],
[
'Python',
'Python is a programming language. When you write Python code and Run it, a Python Interpreter converts the code you wrote as a set of instructions that the computer itself can understand and execute.'
],
[
'Variables and Strings',
'Variables give programmers a way to give names to values and numbers. A string is just a sequence of characters surrounded by quotes.'
],
[
'Functions',
'A function is something that takes input, does something to that input, and then produces output. For example, a function named square might take a number as input and produce the square of that number as output. The main advantage of functions is avoiding repetition.'
],
[
'If and While Statements',
'If statement is used for making decisions to control which code gets executed when. while loop is used to make code that performs the same task (body of the loop) many times.'
],
[
'Lists and For Loops',
'A list is a structured object to store data.  in a list the elements can be anything you want such as characters, strings, numbers or even other lists! A for Loop is used to iterate over structured data. The For Loop goes through each element of the list in turn,  and evaluating a series of command using that element. Using the for loop, we can use less code than we needed using the while loop.'
]
]


def make_HTML_for_many_concepts(list_of_concepts):
    HTML = ""
    for concept in list_of_concepts:
        concept_HTML = make_HTML(concept)
        HTML = HTML + concept_HTML
    return HTML

print make_HTML_for_many_concepts(My_Notes)
