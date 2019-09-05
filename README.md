
<p>
  <img src="https://inspetor-assets.s3-sa-east-1.amazonaws.com/images/inspetor-logo.png" width="200" height="40" alt="Inspetor Logo"> </img>
</p>

# Inspetor Antifraud
Inspetor Antifraud library for Python.

## Description
This README file should help you to integrate the Inspetor Python library into your product.

## Setup Guide
This is the step-by-step Inspetor integration:

### PyPI
PyPI is the largest Python package repository there is and it's common to install python libraries with the "pip install" command. To install our library, you need to use the following command:
```
pip install inspetor
```
If you get no errors, you'll be able to see the Inspetor version installed using the "pip freeze" command (which will show every library you've installed in your environment). 

### Library setup
Now, you're almost able to call the library from inside your code. But first, you need to set some **configuration** values (app id, tracker name, and dev env):
```
    inspetor_config = {
        "APP_ID": "123",
        "TRACKER_NAME": "123",
        "DEV_ENV": True
    }
```

The ***APP_ID*** is a unique identifier that the Inspetor Team will provide you when you start the paid integration with us. The ***TRACKER_NAME*** is a name that will help us find your data in our database and we'll provide you a couple of them. Lastly, ***DEV_ENV*** is a boolean statement that you set to inform if you want to use the development or production environment. It's false by default. 

We **strongly** recommend you to create an Inspetor class in your code to start our library. That's where you're going to insert the Inspetor config you wrote and, with that, retrieve our client. Confusing? Relax, we're kind enough to show you how to do it.

```
import inspetor


class InspetorClass:

    def __init__(self):
        """
        Let's instantiate the library!
        """
        self.inspetor = InspetorClient(inspetor_config)

    def get_client(self):
        """
        return object of type InspetorClient
        """
        return self.inspetor
  ...
```

Now, wherever you need to call some Inspetor function, you just need to import this Class and _voilà_.

*P.S.: you can place your inspetor_config dictionary wherever you think is better - it could be just before instantiating InspetorClient or into a config file that you include in this class.*

### Library Calls

If you've already read the [general Inspetor documentation](https://inspetor.github.io/docs-backend/#introduction), you should be aware of all of Inspetor requests and trackers, so our intention here is just to show you how to use the Python version of some of them.

Let's imagine that you want to put a tracker in your *"create transaction"* flow to send data to Inspetor. First, you need to create an `InspetorSale` object (you can find more about Inspetor objects [here](https://inspetor.github.io/docs-backend/#models)) and then pass this object as an argument to the function `track_inspetor_sale_creation`.

Here is the snippet of the example above:

```
from niceCompany.inspetor.inspetor_class import InspetorClass;


class Sale:
  ...

  def some_company_function(self):
      """
      company_sale is an example object you might have in your code, which contains sale data
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

Following this code and assuming you've built your model with all the required parameters (find out each Model's required parameters [here](https://inspetor.github.io/docs-backend/#models)), whenever `some_company_function` runs, the Inspetor code inside will send the information about the transaction to Inspetor.

We're using an auxiliary function `inspetor_sale_builder` to build the *Sale Model object* but you could do it differently and place it where it suits your needs better. You could set this `inspetor_sale_builder` inside your `InspetorClass` that we talked about some lines above, for example. There are some more tips in the [Best Practices & Tips](#best-practices-&-tips) section.

### Models

The last snippet was a simple example to show how you should call our library and use our models. But now we're gonna talk about all of our Models, hoping you understand that some of them are not tracked themselves but they're needed inside others. Take a look!


***Principal models***:
- **Auth**: model you fill with ***login*** or ***logout*** data.
```
  """
  Calling an instance of Model
  """
  inspetor_auth = self.inspetor.get_inspetor_auth()

  """
  Filling model with auth data
  """
  inspetor_auth.account_email = "test@email.com"
  inspetor_auth.account_id = datetime.timestamp(datetime.now())
  inspetor_auth.timestamp = True  # True when login works
```

- **Account**: model you fill with your ***user*** data. Account has `address` and `billing_address` as two non-required values and both are built with an object of the `InspetorAddress` Model type.
```
  """
  Calling an instance of Model
  """
  inspetor_account = self.inspetor.get_inspetor_account();

  """
  Filling model with account data
  """
  inspetor_account.id = "123"
  inspetor_account.name = "Test"
  inspetor_account.email = "test@email.com"
  inspetor_account.document = "12312312312"
  inspetor_account.phoneNumber = "112345678"
  inspetor_account.address = inspetor_account_address
  inspetor_account.timestamp = datetime.timestamp(datetime.now())
```

- **Event**: model you fill with your ***event*** data (e.g. a party or forum info). The `address` is required here, so you **must** instantiate an `InspetorAddress` Model object for an Event.
```
  """
  Calling an instance of Model
  """
  inspetor_event = self.inspetor.get_inspetor_event()

  """
  Filling the model with event data
  """
  inspetor_event.id = "123"
  inspetor_event.name = "Name Test"
  inspetor_event.description = "Description Test"
  inspetor_event.sessions = [
      inspetor_event_session1,
      inspetor_event_session1
  ]
  inspetor_event.status = "private"
  inspetor_event.slug = "slug-test"
  inspetor_event.creator_id = "124"
  inspetor_event.is_physical = True
  inspetor_event.categories = [
      inspetor_event_category1,
      inspetor_event_category2
  ]
  inspetor_event.address = inspetor_event_address
  inspetor_event.admins_id = ["123"]
  inspetor_event.seating_options = ["Seating Option"]
  inspetor_event.timestamp = datetime.timestamp(datetime.now())
```

- **PassRecovery**: model that must contain data from a ***password recovery*** or ***password reset*** request in your API.
```
  """
  Calling an instance of Model
  """
  inspetor_pass = self.inspetor.get_inspetor_pass_recovery()

  """
  Filling model with password recovery data
  """
  inspetor_pass.recovery_email = "test@email.com"
  inspetor_pass.timestamp = datetime.timestamp(datetime.now())
```

- **Sale**: model that should be filled with ***sale*** data. The sale status has a fixed list of allowed values:
  - "accepted"
  - "rejected"
  - "pending"
  - "refunded"
  - "manual_analysis"
```

  """
  Calling an instance of Model
  """
  inspetor_sale = self.inspetor.get_inspetor_sale()

  """
  Filling model with sale data
  """
  inspetor_sale.id = "123"
  inspetor_sale.account_id = "456"
  inspetor_sale.total_value = "123,00"
  inspetor_sale.status = "pending"
  inspetor_sale.timestamp = datetime.timestamp(datetime.now())
  inspetor_sale.items = [
      self.get_default_item()
  ]
  inspetor_sale.payment = inspetor_payment
```

- **Transfer**: model you fill with the ***transference*** data of an item (e.g. transfer of a ticket). The transfer status has fixed allowed values:
  - "accepted"
  - "rejected"
  - "pending"
```
  """
  Calling an instance of Model
  """
  inspetor_transfer = self.inspetor.get_inspetor_transfer()

  """
  Filling model with transfer data
  """
  transfer.id = "123"
  transfer.timestamp = datetime.timestamp(datetime.now())
  transfer.item_id = "123"
  transfer.sender_account_id = "123"
  transfer.receiver_email = "test@email.com"
  transfer.status = "pending"
```

***Auxiliar models***:
- **Address**: this model appears inside `InspetorAccount` and `InspetorEvent` models and should be filled with data for a ***user***, a ***credit card*** or an ***event***.
```
  """
  Calling an instance of Model
  """
  inspetor_address = self.inspetor.get_inspetor_address()

  """
  Filling model with address data
  """
  inspetor_address.street = "Test Street"
  inspetor_address.number = "123"
  inspetor_address.zip_code = "123456"
  inspetor_address.city = "Test City"
  inspetor_address.state = "Test State"
  inspetor_address.country = "Test Country"
  inspetor_address.latitude = "123"
  inspetor_address.longitude = "123"
```
- **CreditCard**: when your API processes a payment done with a credit card, this model will be used. It should be filled with the ***buyer's creditcard*** secure data. 
```
  """
  Calling an instance of Model
  """
  inspetor_cc = self.inspetor.get_inspetor_card()

  """
  Filling model with credit card data
  """
  credit_card.first_six_digits = "123456"
  credit_card.last_four_digits = "1234"
  credit_card.holder_name = "Holder Name Test"
  credit_card.holder_cpf = "Holder CPF Test"
  credit_card.billing_address = inspetor_billing_address
```

- **Item**: when someone buys a ***ticket***, for instance, this Model will be instantiated and filled with that ticket data.
```
  """
  Calling an instance of Model
  """
  inspetor_item = self.inspetor.get_inspetor_item()

  """
  Filling model with item data
  """
  inspetor_item.id = "123"
  inspetor_item.event_id = "123"
  inspetor_item.session_id = "123"
  inspetor_item.seating_option = "Seating Option Test"
  inspetor_item.price = "10"
  inspetor_item.quantity = "123"
```

- **Payment**: this Model holds the ***transaction*** data (e.g. payment method or installments). The payment status has fixed allowed values:
  - "credit_card" but you can use the Payment const like Payment.CREDIT_CARD
  - "boleto" but you can use the Payment const like Payment.BOLETO
  - "other" but you can use the Payment const like Payment.OTHER_METHOD
```
  """
  Calling an instance of Model
  """
  inspetor_payment = self.inspetor.get_inspetor_payment()

  """
  Filling model with payment data
  """
  payment.id = "123"
  payment.method = "credit_card"
  payment.installments = "1"
  payment.credit_card = inspetor_credit_card
```

 - **Session**: model you fill with ***event date session*** data.
```
  """
  Calling an instance of Model
  """
  inspetor_session = self.inspetor.get_inspetor_session()

  """
  Filling model with session data
  """
  inspetor_session.id = "123"
  inspetor_session.datetime = int(1562934682)  # it's the date of that event session in unix timestamp format
```

 - **Category**: model you fill with ***event category*** data. In an event context it could be, for instance, "Show", "Lecture", "Art Exposition", etc.
```
  """
  Calling an instance of Model
  """
  inspetor_category = self.inspetor.get_inspetor_category()

  """
  Filling model with category data
  """
  category.id = "123"
  category.name = "Cooltegory"
```

### What you should notice
Not all of the Model's attributes are required but we deeply recommend you try to pass them all. On the other hand, some of them are **super important** and you should pass it correctly. Let's talk about some of them.
 - Sale:
   - ***is_fraud***: it's an attribute that you **must** pass to indicate if a sale is fraudulent or not, even if it's something that we're providing to you (as part of postback process).
 - Event:
   - ***sessions***: it's an attribute that you **must** pass even if you don't use the session's context. If that is the case, you just need to replicate some of your Event attributes, such as *event_id* and *event_date*, for example.
 - Address:
   - ***almost all fields***: address is **only required** when you try to track an Event, but exists in the Account model as well. 
 - CreditCard:
   - ***all fields***: all of them are requested if you set the `payment_method` as "credit_card", so pay attention to that.
 - Common requests:
   - ***timestamp***: some Models have setters and getters for this, as you can see in the general files, and you must provide us a UTC Unix timestamp.

### Best Practices & Tips
In this part, we decided to share some nice practices we've discovered during development time and should help you with a cleaner integration.

  - **InspetorClass**: we already told you about that but we think it's important for a cleaner integration. With this class, you don't need to pass your config every time and it creates a layer between our application and yours, where you can, for instance, create functions as *model builders* (we've already talked about that too) to keep all builders in one place. Here's a snippet of an `InspetorClass` with an example of *builder*.
```
import inspetor

class InspetorClass:

    def __init__(self):
        """
        Let's instantiate this awesome library!
        """
        self.inspetor = InspetorClient(inspetor_config)

    def get_client(self):
        """
        return object of type InspetorClient
        """
        return self.inspetor

    def inspetor_auth_builder(self, auth_data) {
    """
    param  array auth_data
    return object of type Inspetor.Model.Auth
    """
        inspetor_auth = self.get_client.get_inspetor_auth()
        inspetor_auth.account_email = auth_data.user_email
        inspetor_auth.account_id = auth_data.account_id_login
        inspetor_auth.timestamp = datetime.timestamp(datetime.now())

        return inspetor_auth
  ...
```

### Conclusion
WOW! It was lovely to work with you, my friend. We truly hope that our instructions were clear and effective. If you have any suggestions or find any bugs please feel free to contact us [here](mailto:dev@useinspetor.com).

Now you're invited to join our army against fraud 'cause ***STEALING IS BULLSHIT***!

*DPCL (dope cool)*
