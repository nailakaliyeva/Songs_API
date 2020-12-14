
# Welcome to SONGS API

This is a simple API that will let you ***GET***, ***UPDATE***, ***POST*** and ***DELETE*** songs and their singers to/from our API

To run the API make sure you have pipenv installed

![songs_one_to_many_API](https://user-images.githubusercontent.com/42359973/102143003-48c32400-3e31-11eb-9139-8b95cb1d4f48.gif)


Then activate your virtual environment by running:

```
pipenv shell
```

Then install all the packages and/or dependencies needed from Pipfile by running:

```
pipenv install
```

Once it's done installing, run the API with this command:

```
pipenv run python app.py
```

where *app.py* is the name of the file

⚠️ Make sure you change port mode from private to public when using the API in Gitpod

The API is only meant for educational purposes and requires information that already exists in the Internet


Here is the body to ***POST*** information about a ***SINGER*** in JSON format using **/singers** endpoint:

{

"ethnicity": "",

"first_name": "",

"last_name": "",

"race": "",

"religion": "",

"zodiac_sign": ""

}

Here is the body to ***POST*** information about a ***SONG*** in JSON format using **/songs** endpoint:

⚠️ Keep in mind when writing lyrics that JSON does not allow real line-breaks. You need to replace all the line breaks with \n.

⚠️ Also, if you don't know your "singer_id", just go to **/singers** endpoint to look it up

{

"album": "",

"date_released": "mm/dd/yyyy",

"lyrics": "",

"singer_id": #,

"song_name": ""

}

To ***GET*** information about posted singers and songs use the same endpoints

To ***UPDATE*** posted singers or songs use the same JSON body as shown above and use ***PUT*** method in POSTMAN using **/singers/update-#** or **/songs/update-#**
endpoint, where you put your singer's or song's id instead of the #

To ***DELETE*** posted singers or songs use ***DELETE*** method in POSTMAN using **/singers/delete-#** or **/songs/delete-#** endpoint, 
where you put your singer's or song's id instead of the #
