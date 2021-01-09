

Once you have successfully built a machine learning model, one of the first challenges is putting the model into production so that it can be used for realistic purposes. One of the best ways to achieve this is to create a REST API for your model so that the model can be used from any platform which is capable of interacting with REST APIs.

REST APIs allow cross-platform integration, which means your model could be used by a variety of applications such as mobile apps, web-browsers, sales-force apps etc. To create REST APIs in Python there are a number of frameworks available such as Flask and Django. We are going to use the Django Framework and the Django REST API framework. The reason for choosing Django is that both the core Django framework and the REST API framework are continually updated, have good documentation and community, and are expected to remain popular in the future.  

In our environment, we used: 

* Django 2.2.0
* Numpy 1.19.3
* Pandas 1.2.0
* Scikit-learn 0.24.0
