# emailing with python
the index.html can be used to create an email template
using $varible in the template, we can be able to customize the email for specific targets
e.g
in index.html
-----------------
<h1>my name is $name <h1/>
-----------------
you can set 
  msg.set_content(html.substitute(name='peter'), 'html') 
to add an attribute 'peter' to the name variable


