 
<p>
  <img src="https://github.com/inspetor/slate/blob/master/source/images/logo-color.png" width="200" height="40" alt="Inspetor Logo"> </img> 
</p>

# Inspetor Antifraud
Developer README for the Inspetor Python SDK. Contains dev setup information and publication instructions.

### Development
Requirements:
- Python (3.7.4)
- pip (19.3.1)

First step:
```
git clone https://github.com/inspetor/inspetor-python.git && cd inspetor-python
```
Install dependencies:
```
pip install -r requirements.txt
```

### TEST YOUR STUFF!
After finishing your changes, it's simple to test:
Unit tests: 
```
python -m pytest tests/unit
```
Integration tests: 
```
python -m pytest tests/integration
```

### Publishing


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
