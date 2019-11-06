
<p>
  <img src="https://inspetor-assets.s3-sa-east-1.amazonaws.com/images/inspetor-logo.png" width="200" height="40" alt="Inspetor Logo"> </img>
</p>

# Inspetor Antifraud
Inspetor Antifraud library for Python.

## Description
Inspetor is a product developed to help your company to avoid fraudulent transactions. This repository contains the Python SDK for you to integrate into your company's Python services, which will allow Inspetor to analyze user patterns and prevent fraudulent transactions. This README file, along with our [generalized integration documentation](https://inspetor.github.io/docs-backend) are here to help you to integrate the Inspetor Python library into your product with few easy steps.

## Setup Guide
This is the step-by-step Inspetor integration:

### Installing the Inspetor SDK
Install the Inspetor SDK to your application's Python environment via `pip`:
```
pip install inspetor
```

### Library setup
To instantiate the Inspetor client object within your project, you'll need to perform some minimal configuration. We suggest adding a similar block to your application configuration:
```
    inspetor_config = {
        'APP_ID': <some unique ID, provided by Inspetor>,
        'TRACKER_NAME': <provided by Inspetor, usually of the form company.application_name>,
        'DEV_ENV': <boolean; whether or not results sent from the tracker should be sent to our Dev collection environment>
    }
```

We suggest creating an `Inspetor` class in which to instantiate you `InspetorClient`, then provide the instantiated client object to your various internal clients. This will ensure that your `InspetorClient` object has been properly configured prior to being called:

```
import inspetor


class InspetorClass:

    def __init__(self):
        """
        Let's instantiate the library!
        """
        self.inspetor = inspetor.InspetorClient(inspetor_config)

    def get_client(self):
        """
        return object of type InspetorClient
        """
        return self.inspetor
  ...
```

### Library Calls

Detailed method information and language-specific examples are all available in the [Inspetor integration documentation](https://inspetor.github.io/docs-backend). There you will find definitions, examples, and references for fundamental Inspetor entities. But just to get you started, we'll provide a practical example for interacting with our SDK below.

Let's imagine that you want to put a tracker in your *"create transaction"* flow to send analytic information to Inspetor at sale creation time. As you may have guessed (if you've read the docs), you'll be calling the `inspetorSaleCreation` method.

Naturally, the `inspetorSaleCreation` method requires certain characteristics of the sale creation to be send to Inspetor for analysis. Those attributes are captured in a **model** (specifically, the [InspetorSale](https://inspetor.github.io/docs-backend/#inspetorsale) model). You can find more general information on Inspetor's concept of **models** [here](https://inspetor.github.io/docs-backend/#models).

Here's an example of how you would integrate this into your code base:

```
from niceCompany.inspetor.inspetor_class import InspetorClass;


class Sale:
  ...

  def your_company_create_sale_function(self):
      """
      company_sale is an object you might have in your code, which contains sale data
      """
      inspetor_sale = self.inspetor_sale_builder(company_sale)

      self.inspetor = InspetorClass()

      if inspetor_sale is not None:
          inspetor.get_client.track_sale_creation(inspetor_sale)

  def inspetor_sale_builder(self, company_sale):

      model = inspetor.get_client.get_inspetor_sale()

      model.id(company_sale.get_id());
      model.account_id(company_sale.user_id)
      model.status(company_sale.sale_status);
      model.is_fraud(company_sale.fraud);
      model....

      return model
  ...
```
Note that we are using an auxiliar function *inspetorSaleBuilder* to build the *Sale Model*. This is not strictly necessary, but we imagine you will find such a practice preferable.

## Support

Feel free to reach out to the [Inspetor team](support@useinspetor.com) if you encounter any problems during your integration.