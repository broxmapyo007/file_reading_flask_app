# file_reading_flask_app
Task project for file reading in flask app with task rules.

#Task Completed
    
   Create Flask application.
    
##Application details:
    
    1. Application should have single GET route.
    2. On call to this route application need to read content of given file (see file1.txt.. file4.txt)
    and render properly it in HTML page. Any markup should be preserved.
             files are in English
             file 4 contains some Chinese
    3. Endpoint should accept target file name as optional variable part of URL and default to
    file1.txt.
    4. Endpoint should accept optional URL query parameters to specify start line number and
    end line number. If those parameters present – return only part of file between specified line
    numbers. If parameters absent – return all lines.
    5. All most likely exceptions in application logic should be handled gracefully. When
    exception happens error page should be displayed with exception details.


#usage:

    Example of url query

        default file1.txt > url :"http://127.0.0.1:5000"
        url :"http://127.0.0.1:5000/file1"
        url :"http://127.0.0.1:5000/file4?start=0&end=10"


##Requirement

    1.Flask
    2.chardet

##vitualenv

    python
    pip install -r .\requirement.txt

##run:

    python app.py

##Explanation

    After app.py runing on localserver,visit url :http://127.0.0.1:5000/
    default file1.txt data will be fetche and displayed
    
    controls:
    By adding file(1,2,3,4) at end of url/ will fetch and display that full data
      http://127.0.0.1:5000/file2
      http://127.0.0.1:5000/file3
    
    by adding query ? start= <line number to start reading from> & end = <line number to stop reading on>
     http://127.0.0.1:5000/file1?start=5&end=10
    

#Task done by

    Adesh Dangi
