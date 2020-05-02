## Flask Sentiment Analysis Demo
-----------------------------


This is a micro Tutorial on how create API for your sentiment analysis service. It uses the the model we worked on [Transformers for Sentiment Analysis](
https://github.com/AMMI-NLP-Study-Group/pytorch-sentiment-analysis/blob/master/6%20-%20Transformers%20for%20Sentiment%20Analysis.ipynb). Please before playing with this code go through the notebook and save your model.


### Installation
---------------
```
pip install -r requirement.txt
```


###  Model Required
-------------------
please download the model from [Here](https://drive.google.com/file/d/1gqiDBdsIwF41Mc8d1DkA1IfXL1dBEixh/view?usp=sharing) or if the link is not working try running the colab and saving the model by the name ```tut6-model.pt```.

Then Save it in folder called ```checkpoint``` in the working directory.


### Running 
```
$ export FLASK_APP=service.py
$ export FLASK_DEBUG=1


$ flask run --host=0.0.0.0
```




## Additional Tutorials 
-----------------------------
- [Flask](https://www.youtube.com/watch?v=X0dwkDh8kwA)
- [How to build a web app using Python’s Flask and Google App Engine](https://www.freecodecamp.org/news/how-to-build-a-web-app-using-pythons-flask-and-google-app-engine-52b1bb82b221/)
- [HTML, CSS - Lecture 1 - CS50's Web Programming with Python and JavaScript 2018](https://www.youtube.com/watch?v=XQs5KcUj-Do)
- [Flask - Lecture 2 - CS50's Web Programming with Python and JavaScript 2018](https://www.youtube.com/watch?v=j5wysXqaIV8)
- [Deploying a Flask Application to Heroku](https://stackabuse.com/deploying-a-flask-application-to-heroku/)
