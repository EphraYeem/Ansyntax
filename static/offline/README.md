first copy all the files from this folder to "static" folder

then load the json file to your mongo using the following command:
mongoimport --db=test --collection=modules --file=sample.json

after that change the following lines:
<link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css"/>
<script type="text/javascript" src="https://raw.githack.com/SortableJS/Sortable/master/Sortable.js"></script>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
 to 
<link rel="stylesheet" href="{{ url_for('static', filename='bootstrap.min.css') }}"/>
<script type="text/javascript" src="{{ url_for('static', filename='Sortable.js') }}"></script>
<script type="text/javascript" src="{{ url_for('static', filename='jquery.min.js') }}"></script>

and you are set

the docker zip is for test runs