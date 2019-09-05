 
<p>
  <img src="https://github.com/inspetor/slate/blob/master/source/images/logo-color.png" width="200" height="40" alt="Inspetor Logo"> </img> 
</p>

# Inspetor Antifraud
Antrifraud Inspetor library for Python. 

## Description
This READ ME file is special! It should help you, my dear developer, on your "*publishing library road*". Let's chat about library development and publishing new versions 'cause the war against fraud never ends.

## Setup Guide
This is a step-by-step Inspetor publication guide:

### Development
Ok, so you decided to make changes in this beautiful library. No worries, I appreciate that.
Well, you should clone this repo:
```
git clone https://github.com/inspetor/inspetor-python.git
```
And when it's done, you can start to code. Every useful information to the development of this library can be found [here](https://github.com/inspetor/inspetor-python/blob/master/README.md), general information about Inspetor [here](https://inspetor.github.io/docs-backend/) and [here](https://github.com/inspetor/libraries) are some libraries definitions (swagger).

### TEST YOUR STUFF!
After finishing your code, it's simple to test:
Locally: 
```
python -m pytest tests/inspetor/model
python -m pytest tests/inspetor/tracker
```
Integration tests: 
```
python -m pytest tests/inspetor/integration
```
P.S.: you'll need pytest installed in your machine/virtualenv. 

### Publishing
Are you done? Nice! It's time to publish. If you had finished a new brilliant version, you must create a **release** to that version.

#### Realeases
The way to keep all active versions alive is creating a new release branch to push this new version.
```
git checkout -b release/[new version] (e.g release/1.2.3-beta)
```
Push your new version there and if everything goes right come back here and publish a new release tagging the branch you just created. You can see how to publish a new release [here](https://help.github.com/en/articles/creating-releases#automatically-creating-releases).

Now that a new release was created, you have to publish this new version in PyPI Repository, so anyone will be able to "pip install inspetor" easily. 
It's possible to publish in a test-version of PyPI before the real repo too. You can find all the instructions [here](https://packaging.python.org/tutorials/packaging-projects/).

### Conclusion
Easy, huh? I hope this small guide has been helpful to anyone who wants to improve our library. Nice job!

And never forget that **STEALING IS BULLSHIT**. 

*DPCL (dope cool)*
