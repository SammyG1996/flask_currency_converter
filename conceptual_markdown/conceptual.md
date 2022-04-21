### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?


  1. There are a few important differences to consider between Python and JavaScript. For example, while semicolons are optional for JavaScript (and encourage in most cases), Python gets rid of them completely.  

  2. Also, another thing to consider is that curly brackets are used in JavaScript to denote the scope of the function. This is not the case with Python. Instead, Python uses indentation to denote scope.  

  3. Another big difference is that in JavaScript you must use the keywords **_const_**, **_let_**, or **_var_** to declare a variable. This once again is not the case with Python. Instead, you can simply say for example “x=foo” to create a variable. 



- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  1.	You could do something like:  
dictionary.get(“c”, 3)

  2.	You could also do:   
if c **_in_** dictionary.keys():  
	return _dictionary_


- What is a unit test?

  * A unit test will test a specific function within an application. It’s best to write your code thinking about unit tests. Therefore, it's better to have small bite-sized units of code that you can test, rather than to have a massive function that is challenging or maybe even impossible to test. 

- What is an integration test?

  * An integration test is a test that will see how individual units of code function together when integrated. It can also test how routes work and so forth. In general, these can be a little harder to write but are still very important, as they can reveal flaws in how the individual units function together, even if the individual functions work fine. An oddity of integration tests is that they still use the unit test module, but these tests are indeed different.  

- What is the role of web application framework, like Flask?
  * The purpose of flask is to allow us to create a web server that will _serve_ the content that is to be loaded on the front end. It also enables us to create _routes_ that direct the request to the server and determine what information to respond with. Flask also does a lot of little things that make creating a web server easier. For example, when you send an HTTP packet _flask_ will automatically fill out the response header. There are also debugging tools that you can use with flask. And it allows for other frameworks like Jinja to be used to make serving HTML easier. 


- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

    * This usually would boil down to whether you are trying to submit information, or if you are trying to direct them to a new route. If I am trying to submit information I would likely use:  
    '/foods/pretzel'  
    If I am trying to submit a search query, or I'm trying to pass in information then I would most likely use:  
    'foods?type=pretzel'


- How do you collect data from a URL placeholder parameter using Flask?

  * You would use:  
    request.args.get('placeholder')

- How do you collect data from the query string using Flask?

  * You would use:  
    request.args.get('query_string')

- How do you collect data from the body of the request using Flask?

  * You would use:  
    request.data.get('example')

- What is a cookie and what kinds of things are they commonly used for? 

  * A cookie holds information about that user and saves it to the server. This can then be used on later occasions within the application. Its data that persists and can be used retrieved at any point. You can store authentication, shopping cart items, whether the user prefers “light” or “dark” mode, and so much more. 

- What is the session object in Flask?

  * A session is like a cookie but is much more versatile. A session can store dictionaries while cookies cannot. Also, while sessions can store any type of primitive data type, cookies can only store strings. And you can also store _more_ data in a session than you can in a cookie (4kb vs 5mb). 


- What does Flask's `jsonify()` do?

  * It will create a JSON version of the data that you pass into it. Also, it will format the information to be sent back with all the appropriate headers to signify to the browser that the response is JSON. 
