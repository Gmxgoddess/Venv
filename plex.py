from general_stuff import *

###

Shopify_App_API_Url="enter here"
Shopify_App_API_Key="enter here"
Shopify_App_API_Secret="enter here"
class Shop:
  def __init__(self):
    shopify.ShopifyResource.clear_session()
    shopify.ShopifyResource.set_site(Shopify_App_API_Url)
    shopify.Session.setup(api_key=Shopify_App_API_Key, secret=Shopify_App_API_Secret)
    self.shopify = shopify
  ffind = lambda self, **kwargs: self.shopify.Fulfillment.find(**kwargs)
  pfind = lambda self, **kwargs: self.shopify.Product.find(**kwargs)
  ofind = lambda self, **kwargs: self.shopify.Order.find(**kwargs)
  rfind = lambda self, **kwargs: self.shopify.Redirect.find(**kwargs)
  pcount=lambda self: self.shopify.Product.count()
  def hoistproducts(self,**kwargs):
    products = flatten([self.pfind(status='any',limit=250,page=pg,**kwargs) for pg in range(1,(ceil(self.pcount()/250)+1))],1)
    return products

###


##



