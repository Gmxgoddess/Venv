from general_stuff import *
from plex import *
url1='https://app.oberlo.com/import'


url2='https://app.oberlo.com/ajax/import/save-title'


url3='https://app.oberlo.com/ajax/import/save-type'
url4='https://app.oberlo.com/ajax/import/save-description'
url5='https://app.oberlo.com/ajax/import/save-option-value'
url6='https://app.oberlo.com/import?status[]=0&status[]=1&keywords=&source=1&page=%s'
url7='https://app.oberlo.com/ajax/products/ali-url?id=%s'
url8='https://app.oberlo.com/my-products'
url9='https://app.oberlo.com/my-products?page={}'
url10='https://app.oberlo.com/ajax/import/ready-to-push'
url11='https://app.oberlo.com/ajax/explore/addtoimportlist'
os.makedirs('headers',exist_ok=True)
headerdict1={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'max-age=0', 'Connection': 'keep-alive', 'Cookie': None, 'Host': 'app.oberlo.com', 'Referer': 'https://app.oberlo.com/my-products?page=1&filters%5Bkeywords%5D=&filters%5Bsync_prices_status%5D=0&filters%5Bgone_status%5D=0&filters%5Bsource%5D=0', 'Sec-Fetch-Dest': 'document', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'same-origin', 'Sec-Fetch-User': '?1', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
headers1=Headers().verifyheaders(headers=or_list(lambda:Pickles().loadpickles('headers/headers1.pkl',default={}),lambda:[Pickles().savepickles({},'headers/headers1.pkl'),Pickles().loadpickles('headers/headers1.pkl')][1]),url='https://app.oberlo.com/import',text='app.oberlo.com/import by making a random change to a product',savefile='headers/headers1.pkl',minimal_headers=copy.deepcopy(headerdict1))
headers2=Headers().verifyheaders(or_list(lambda:Pickles().loadpickles('headers/headers2.pkl',default={}),lambda:[Pickles().savepickles({},'headers/headers2.pkl'),Pickles().loadpickles('headers/headers2.pkl')][1]),'https://app.oberlo.com/my-products','app.oberlo.com/my-products by clicking open original for a product',savefile='headers/headers2.pkl')
headers3=[[setitem(headerdict1,i,headers1[i]) for i in headerdict1.keys() if i in headers1.keys()],headerdict1][1]
rgx1='importProducts: (.*),'
rgx2='window.App.payload.pagination = (.*);'
import argparse
parser = argparse.ArgumentParser(description="a")
parser.add_argument("-i",help="Id",dest="i",required=False)
parser.add_argument("-t",help="Title",dest="t",required=False)
parser.add_argument("-p",help="Type",dest="p",required=False)
parser.add_argument("-d",help="Desc",dest="d",required=False)
parser.add_argument("-v",help="Vnames",dest="v",required=False)
parser.add_argument("-vnamefire",help="vnamefire",dest="vnamefire",required=False)
parser.add_argument("-c",help="c",dest="c",default=False,action="store_true",required=False)
parser.add_argument("-u",help="Updates",dest="u",required=False)
parser.add_argument("-delete",help="delete",dest="delete",required=False)
args=parser.parse_args()
args=type('',(object,),dict(v='1,2,3,4,5,6,7,8',t='title%s'%(random.randrange(222)),p='new',d='<p>desc</p>',c=True,vnamefire=None))
#


args=AD(dict(i=4000538721635,t='A',p='A',d='A',v=None,vnamefire=True,c=False,u=False,delete=None))
args=AD(dict(i=33022389035,t='Arr',p='A',d='A',v=None,vnamefire=True,c=False,u=False))
class ForgotTheName:
  def __init__(self):
    return
  def click(self):
    """
    if args.i:
      id = args.i
      requests.post(url11,headers=headers1,json={"id":"","url":"https://www.aliexpress.com/item/%s.html"%(id)})
      time.sleep(10)
    """


    # here, scan the amount of existing items,
    # scan the first page item name
    # holy shit,
    # scan the first page item name
    # scan all the pages
    # do it again.
    txt=requests.get(url1,headers=headers3,timeout=5).text
    pgs=json.loads(findall(txt,1,rgx2))['last_page']
    txts=pool(lambda i:requests.get(url6%(i),headers=headers3,timeout=5).text,lrange(1,pgs+1),nodes=8).result()
    r=flatten(lmap(lambda i:json.loads(findall(i,1,rgx1)),txts),1)
    c=r[0]['id']
    id = args.i
    requests.post(url11,headers=headers1,json={"id":"","url":"https://www.aliexpress.com/item/%s.html"%(id)})
    while True:
      txt=requests.get(url1,headers=headers3,timeout=5).text
      pgs=json.loads(findall(txt,1,rgx2))['last_page']
      txts=pool(lambda i:requests.get(url6%(i),headers=headers3,timeout=5).text,lrange(1,pgs+1),nodes=8).result()
      r=flatten(lmap(lambda i:json.loads(findall(i,1,rgx1)),txts),1)
      cc=r[0]['id']
      if cc != c:
        break



    
    # you provide the id, do you always update it immediately? no.
    # how do you know if you do.
    if args.i:
      self.run_more(id=args.i)
    elif not args.i:
      self.run_more(id=None)
  def run_more(self,**kwargs):
    self.i_want_to_have_the_import_json_data(id=kwargs.get('id'))
    ifdo(lambda:args.t,lambda:self.i_want_to_edit_the_title())
    ifdo(lambda:args.p,lambda:self.i_want_to_edit_the_product_type())
    ifdo(lambda:args.d,lambda:self.i_want_to_edit_the_product_description())
    ifdo(lambda:args.v or args.vnamefire,lambda:self.i_want_to_edit_the_variant_names())
    self.post_it()
    saved = self.next
    saved=self.i_want_to_refresh_the_stocks_and_prices(saved)
    saved=ifelseget(lambda:saved['excessdata']['i_want_to_edit_the_ships_from_options_for_the_item']==True,lambda:self.i_want_to_edit_the_ships_from_options_for_the_item(saved),lambda:saved)
    saved=ifelseget(lambda:saved['excessdata']['i_want_to_order_the_product_images_based_on_the_variants']==True,lambda:self.i_want_to_order_the_product_images_based_on_the_variants(saved),lambda:saved)
    saved=ifelseget(lambda:saved['excessdata']['i_want_to_put_the_product_variants_in_order']==True,lambda:self.i_want_to_put_the_product_variants_in_order(saved),lambda:saved)
    saved=ifelseget(lambda:saved['excessdata']['i_want_to_use_photofinish_on_the_product']==True,lambda:self.i_want_to_use_photofinish_on_the_product(saved),lambda:saved)
    return saved
  def i_want_to_have_the_import_json_data(self,id=None):
    txt=requests.get(url1,headers=headers3,timeout=5).text
    pgs=json.loads(findall(txt,1,rgx2))['last_page']
    txts=pool(lambda i:requests.get(url6%(i),headers=headers3,timeout=5).text,lrange(1,pgs+1),nodes=8).result()
    r=flatten(lmap(lambda i:json.loads(findall(i,1,rgx1)),txts),1)
    def roll(x):
      new = {}
      new['ext_id'] = x['product']['ext_id']
      new['id'] = x['id']
      def roll(x):
        new = {}
        new['sku'] = x['sku']
        new['option1'] = x['option1']
        new['option2'] = x['option2']
        new['option3'] = x['option3']
        new['options123'] = [x['option1'],x['option2'],x['option3']] # save off bat cuz u can change it and it wont be there
        new['id'] = x['id']
        new['stock'] = x['stock']
        new['price'] = x['price']
        new['compare_price'] = x['compare_price']
        return new
      new['variants'] = lmap(roll,x['variants']['data'])
      new['description'] = x['description']
      new['original_title'] = x['original_title']
      new['title'] = x['title']
      new['product_type'] = x['product_type']
      new['product_id'] = None #
      new['excessdata']=dict(i_want_to_edit_the_ships_from_options_for_the_item=True,i_want_to_order_the_product_images_based_on_the_variants=True,i_want_to_put_the_product_variants_in_order=True,i_want_to_use_photofinish_on_the_product=ifelseget(lambda:args.c,lambda:True,lambda:False),)
      def x(new):
        new['url']=json.loads(requests.get(url7%new['id'],headers=headers2,).text)['url'] # save too
        return new
      new = x(new)
      return new
    payload = lmap(roll,r)


    next=None
    if id:
      next = [i for i in payload if str(id) in i['url']][0]
    else:
      next = [i for i in payload if i['product_type'] == None][0]
      print(next)
    self.next = next
  def i_want_to_edit_the_title(self):
    self.next['title'] = args.t
    requests.post(url2,headers=headers1,json={"id":self.next['id'],"title":self.next['title']})
  def i_want_to_edit_the_product_type(self):
    self.next['product_type'] = args.p
    requests.post(url3,headers=headers1,json={"product_type":args.p,"id":self.next['id']})
  def i_want_to_edit_the_product_description(self):
    body_x = findall(self.next['description'],"<strong.*?<br />")
    for i in body_x:
      accountable_descriptions = ["Material","Pattern Type","item Type","Style","Feature"]
      found = 'no'
      for j in accountable_descriptions:
        if j in i:
          found = 'yes'
      if found == 'no':
        self.next['description'] = self.next['description'].replace(i,"")
      if found == 'yes':
        sys.stdout = open(os.devnull,"w")
        new = re_substitute_function(i,'</strong> (.*?)<br />',lambda i:i.title())
        sys.stdout = sys.__stdout__
        self.next['description'] = self.next['description'].replace(i,new)
      self.next['description'] = self.next['description'].replace("<p><br>","<p>")
    self.next['description'] = re_substitute(self.next['description'],["(<br>)+","<br>"])
    self.next['description'] = args.d + self.next['description']
    requests.post(url4,headers=headers1,json={"id":self.next['id'],"description":self.next['description']})
  def i_want_to_edit_the_variant_names(self):
    on,v=or_list(lambda:[args.v.split(';')[0],args.v.split(';')[1]],lambda:[None,args.v.split(',')],lambda:[None,None])
    if on == None:
      on = 1
    if args.vnamefire:
      v = ['Style %s'%(i+1) for i in lrange(len(set(sud('option%s'%(on),self.next['variants']))))]  
    requests_to_make = []

    for v_number_count, i in enum(v):
      opt = 'option%s'%on
      quas = [i for i in self.next['variants'] if i[opt] == oset(sud(opt,self.next['variants']))[v_number_count]]
      lmap(lambda j:setitem(j,opt,i),quas)
      news = lmap(lambda j:type('',(object,),dict(args=[url5],kws=dict(json={"id":self.next['id'],"variant_id":j['id'],"option":int(opt[-1]),"value":i},headers=headers1)))(), quas)
      requests_to_make.extend(news)

    def request_it(i):
      new = requests.post(i.args[0],headers=i.kws['headers'],json=i.kws['json'])
      print(new)
      ifdo(lambda:new.status_code!=200,lambda:input("Status code is not 200, press Enter"))
    pool(request_it,requests_to_make,nodes=8).result()
  def post_it(self):
    requests.post('https://app.oberlo.com/ajax/import/ready-to-push',json={"id":self.next['id']},timeout=5,headers=headers1).text
    

    c=len(Shop().hoistproducts())
    while True:
      cc=len(Shop().hoistproducts())
      if len(cc) != c:
        break
    



    def i_want_to_update_the_product_id(saved):
      if saved['product_id']==None:
        rng=lrange(1,json.loads(findall(requests.get(url8,headers=headers2,timeout=5).text,1,'pagination: (.*),'))['last_page']+1)
        v=pool(lambda i:requests.get(url9.format(i),headers=headers2).text,rng).result()
        vv=flatten(lmap(lambda i:json.loads(findall(i,1,'myProducts: (\[.*),')),v),1)
        j = [i for i in vv if i['id']==saved['id']][0]
        saved['product_id']=j['ext_id']
        return saved
    i_want_to_update_the_product_id(self.next)
  def i_want_to_refresh_the_stocks_and_prices(self,saved):
    self.saved=saved
    self.url = saved['url']
    txt = requests.get(self.url).text
    skudata=json.loads(findall(txt,1,'data: ({"actionModule.*),',))
    self.skus=skuds=skudata["skuModule"]["productSKUPropertyList"]
    self.prices=skudata["skuModule"]["skuPriceList"]

    txt = requests.get(self.url).text
    id = findall(txt,'(?s)window.runParams.*productIds: "(.*?)"')[0]
    headers={'accept-encoding': 'gzip, deflate, br', 'referer': 'https://www.aliexpress.com/item/%s.html'%(id), 'sec-fetch-dest': 'empty', 'sec-fetch-site': 'same-origin', 'accept': 'application/json, text/plain, */*', 'authority': 'www.aliexpress.com', 'method': 'GET', 'scheme': 'https', 'sec-fetch-mode': 'cors', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36', 'accept-language': 'en-US,en;q=0.9'}
    txt2=requests.get("https://www.aliexpress.com/aeglodetailweb/api/logistics/freight?productId=%s&count=1&country=US&provinceCode=&cityCode=&tradeCurrency=USD&userScene=PC_DETAIL_SHIPPING_PANEL&displayMultipleFreight=false"%(id.replace("en","")),headers=dictupdate(headers,) ).text
    data=json.loads(txt2)["body"]["freightResult"]
    sorted_companies_list = ["SunYou Economic Air Mail","Yanwen Economic Air Mail","China Air Post","China Post Registered Air Mail","ePacket","AliExpress Standard Shipping"]
    data2 = sorted([{"price":i['freightAmount']['value'],"company":i["company"]} for i in data if i['company'] in sorted_companies_list],key=lambda i:sorted_companies_list.index(i['company']))
    self.pick = data2[0]
    print("picked shipping data: %s"%(self.pick))

    price = self.pick
    skus = flatten(key("skuPropertyValues",self.skus))
    def roll(x):
      new = {}
      new['propertyValueDisplayName'] = x['propertyValueDisplayName']
      new['skuPropertyTips'] = x['skuPropertyTips']
      new['propertyValueName'] = x['propertyValueName']
      new['skuPropertyValueTips'] = x['skuPropertyValueTips']
      new['name'] = or_list(lambda:new['propertyValueDisplayName'],) #5
      #name=new['skuPropertyTips'] # 6
      #name=new['propertyValueName'] # 56
      #name=new['skuPropertyValueTips'] # 5
      new['id'] = str(x['propertyValueIdLong'])
      return new
    skus = lmap(roll,skus)
    data = []
    for i in self.prices:
      new = {}
      new['quantity'] = i['skuVal']['availQuantity']
      new['options123'] = i['skuPropIds'].split(',')
      new['optioons123']=listplus(new['options123'],3,None)
      for j in skus:
        ifdo(lambda:j['id'] in new['options123'],lambda:
        [setitem(new['options123'],idx,j['name']) for idx,k in enum(new['options123']) if k==j['id'] ] )

      new['price'] = or_list(lambda:i['skuVal']['actSkuCalPrice'],lambda:i['skuVal']['skuCalPrice'])
      old_price=new['price']
      new['price'] = round(float(new['price']) + price['price'],2)
      print('|%s %s'%(old_price,new['price']),end="")
      data.append(new)
    self.data = data
    # above is the ali data for the SKU's for the item includes the options123 and price and stock, above you specified the saved
    # here, you match the the variants and it updates.
    p=Shop().pfind(id_=saved['product_id'])
    def themoneybagpricing(price):
      moneybag = {'price':price,'new_price':None}

      ifdo(lambda:moneybag['price'] >   0 and moneybag['price'] <=   2,lambda:setitem(moneybag,'new_price',  ceil(moneybag['price']  +    8)-0.05  )  )
      ifdo(lambda:moneybag['price'] >   2 and moneybag['price'] <=   4,lambda:setitem(moneybag,'new_price',  ceil(moneybag['price']  +    6)-0.05  )  )
      ifdo(lambda:moneybag['price'] >   4 and moneybag['price'] <=   6,lambda:setitem(moneybag,'new_price',  ceil(moneybag['price']  +    4)-0.05  )  )
      ifdo(lambda:moneybag['price'] >   6 and moneybag['price'] <=   8,lambda:setitem(moneybag,'new_price',  ceil(moneybag['price']  +    4)-0.05  )  )
      ifdo(lambda:moneybag['price'] >   8 and moneybag['price'] <=  10,lambda:setitem(moneybag,'new_price',  ceil(moneybag['price']  +    6)-0.05  )  )
      ifdo(lambda:moneybag['price'] >  10 and moneybag['price'] <=  20,lambda:setitem(moneybag,'new_price',  ceil(moneybag['price']  *  1.7)-0.05  )  )
      ifdo(lambda:moneybag['price'] >  20 and moneybag['price'] <=  40,lambda:setitem(moneybag,'new_price',  ceil(moneybag['price']  *  1.8)-0.05  )  )
      ifdo(lambda:moneybag['price'] >  40 and moneybag['price'] <= 100,lambda:setitem(moneybag,'new_price',  ceil(moneybag['price']  *  1.9)-0.05  )  )
      ifdo(lambda:moneybag['price'] > 100                                 ,lambda:setitem(moneybag,'new_price',  ceil(moneybag['price']  *    2)-0.05  )  )

      moneybag['compare_at'] = ceil(moneybag['new_price'] * ((2)))-0.05
      return moneybag
    s = lambda q: [q.option1,q.option2,q.option3]
    for i in self.data:
      v = [x for x in saved['variants'] if x['options123']==i['options123']][0]
      r = [x for x in p.variants if x.sku==v['sku']][0]
      r.price=themoneybagpricing(round(flt(v['price']),2) )['new_price']
      r.compare_at=themoneybagpricing(round(flt(v['price']),2) )['compare_at']
      r.inventory_quantity = v['stock']
    p.save()
    return saved
  def i_want_to_edit_the_ships_from_options_for_the_item(self,saved):
    p=Shop().pfind(id_=saved['product_id'])
    '''
    p = shop.pfind(id_=4518536937515)
    '''
    if "Ships From" not in key("name",p.options):
      saved['excessdata']['i_want_to_edit_the_ships_from_options_for_the_item']='not required'
      return saved
    if "Ships From" in key("name",p.options):
      idx = [idx+1 for idx,i in enum(p.options) if i.name == "Ships From"][0]
      p.variants = [i for i in p.variants if getattr(i,"option%s"%(idx)).lower()=="china"]
      for i in p.variants:
        setattr(i,"option%s"%(idx),None)
      p.options = [i for i in p.options if i.name != "Ships From"]
    lmap(lambda i:[setitem(globals(),'choices',listminus(getattrs(['option1','option2','option3'],i),None,minus_once=True) ),
                    setattrs(i,'option1',None,'option2',None,'option3',None),
                    setattrs(i,'option1',or_list(lambda:globals()['choices'][0],None),'option2',or_list(lambda:globals()['choices'][1],None),'option3',or_list(lambda:globals()['choices'][2],None))
                    ],p.variants)
    p.save()
    saved['excessdata']['i_want_to_edit_the_ships_from_options_for_the_item']='editted'
    '''
    p = shop.pfind(id_=4518537068587)
    (
    ("Ships From" in sud("name",p.options)) and 
    (setitem(globals(),'number',[(idx+1) for idx,i in enum(p.options) if i.name=="Ships From"][0]) or
     setattr(p,'variants',sudby(lambda i:getattr(i,"option%s"%(number)).lower()=='china',p.variants)) or
     lmap(lambda i:setattr(i,"option%s"%(number),None),p.variants)) and
    setattr(p,'options',sudby(lambda i:i.name!="Ships From",p.options))
    )
    lmap(lambda i:[setitem(globals(),'choices',listminus(getattrs(['option1','option2','option3'],i),None,minus_once=True) ),
                    setattrs(i,'option1',None,'option2',None,'option3',None),
                    setattrs(i,'option1',or_list(lambda:globals()['choices'][0],None),'option2',or_list(lambda:globals()['choices'][1],None),'option3',or_list(lambda:globals()['choices'][2],None))
                    ],p.variants)
    p.save()
    '''
    return saved
  def i_want_to_order_the_product_images_based_on_the_variants(self,saved,op=1):
    p = Shop().pfind(id_=saved['product_id'])
    todes = p.variants
    op = 1
    opt = 'option%s'%(op)
    names=oset(sud(opt,todes))
    candy=[[j for j in todes if getattr(j,opt)==i] for i in names]
    imich_idz=oset(sud('image_id',flatten(candy,1)))
    evil=sud('id',p.images)

    """
    In [77]: imich_idz
    Out[77]: [16512509214763, 16512509116459, 16512509313067]
    In [78]: evil
    Out[78]: [16512509181995, 16512509214763, 16512509313067, 16512509116459]
    """


    old_evil=deepcopy(evil)
    marked=[]
    for number,e in enumerate(evil):
      if e in imich_idz:
        new_mark=[i for i in imich_idz if i not in marked][0]
        marked.append(new_mark)
        evil[number]=new_mark
    images = []
    for number,i in enumerate(evil):
      lol=[j for j in p.images if j.id == i][0]
      lol.position = number + 1
      images.append(lol)
    p.save()


    """
    In [78]: evil
    Out[78]: [16512509181995, 16512509214763, 16512509116459, 16512509313067]
    """
    saved['excessdata']['i_want_to_order_the_product_images_based_on_the_variants']='editted'
    return saved
  def i_want_to_put_the_product_variants_in_order(self,saved,op=1):
    p=Shop().pfind(id_=saved['product_id'])
    op = op
    opt = 'option%s'%op
    nms=oset(sud(opt,p.variants))
    f=[]
    for i in nms:
      q=keyby(lambda j:getattr(j,opt)==i,p.variants)
      f.extend(q)
    p.variants=f
    p.save()
    saved['excessdata']['i_want_to_put_the_product_variants_in_order']='editted'
    return saved
  def i_want_to_use_photofinish_on_the_product(self,saved):
    # at oberlo, you specify wm. save the data.
    import cv2,numpy as np
    rm("photofinish")
    os.makedirs("photofinish")
    p=Shop().pfind(id_=saved['product_id'])

    fns=pool(lambda idx,i:Images().download(i.src,'dataset/%s.png'%idx),lrange(len(p.images)),p.images).result()
    imgs=pool(lambda i:Images().img_binary(i),fns)

    ###
    imagematch=None
    dimensions=None
    for i in imgs:
      dimensions=list(tcer(lmap(int,i.shape)[:2]))
      y,x=ceil(dimensions[0]*0.0625),ceil(dimensions[1]*0.0625)
      if list(i[y-25:y+25,x-25:x+25,:,].flatten())!=[255]:
        imagematch=i
        break
    # here, work on the gotten imagematch
    # after that, you should after you download the images, open them with cv2 and edit them. use the percentage factor 
    ###

    cv2.imwrite(os.path.expanduser('~/venv/venv/phot.png'),imagematch)

    screenshot = cv2.imread(os.path.expanduser('~/venv/venv/phot.png'))
    dimensions = list(tcer(lmap(int,screenshot.shape)[:2]))
    start = ceil(dimensions[1]*0.0625)
    star = ceil(dimensions[0]*0.0625)

    desired_top = 1
    increment=1
    while True:
      l=screenshot[star-increment-1:star-increment,start-25:start+25,:,]
      f=oset(list(l.flatten()))
      print(star-increment)
      if f==[255]:
        desired_top=star-increment-1
        break
      increment+=1
      h=screenshot[star-increment-1:star-increment+10,start-25:start+25,:,]

    desired_bottom = 1
    increment=1
    while True:
      l=screenshot[star+increment:star+increment+1,start-25:start+25,:,]
      f=oset(list(l.flatten()))
      print(star+increment+1)
      if f==[255]:
        desired_bottom=star+increment+1
        break
      increment+=1
      h=screenshot[star+increment-10:star+increment+10,start-25:start+25,:,]
    h = screenshot[desired_top:desired_bottom,start-25:start+25,:,]

    desired_left = 1
    increment = 1
    while True:
      l=screenshot[desired_top:desired_bottom,start-increment-10:start-increment,:,]
      f=oset(list(l.flatten()))
      print(start-increment)
      if f==[255]:
        desired_left=start-increment-10
        break
      increment+=1
      h=screenshot[desired_top:desired_bottom,start-increment-10:start-increment+10,:,]

    desired_right = 1
    increment = 1
    while True:
      l=screenshot[desired_top:desired_bottom,start+increment:start+increment+10,:,]
      f=oset(list(l.flatten()))
      print(start+increment+10)
      if f==[255]:
        desired_right=start+increment+10
        break
      increment+=1
      h=screenshot[desired_top:desired_bottom,start+increment:start+increment+10,:,]


    new_desired_top = 1
    increment = 1
    while True:
      l = screenshot[desired_top-increment-1:desired_top-increment,desired_left:desired_right,:,]
      f=oset(list(l.flatten()))
      print(desired_top-increment-1)
      if f==[255]:
        new_desired_top=desired_top-increment-1
        break
      increment+=1
      h=screenshot[desired_top-increment-10:desired_top-increment+10,desired_left:desired_right,:,]

    new_desired_bottom = 1
    increment = 1
    while True:
      l = screenshot[desired_bottom+increment:desired_bottom+increment+1,desired_left:desired_right,:,]
      f=oset(list(l.flatten()))
      print(desired_bottom+increment+1)
      if f==[255]:
        new_desired_bottom=desired_bottom+increment+1
        break
      increment+=1
      h=screenshot[desired_bottom+increment-10:desired_bottom+increment+10,desired_left:desired_right,:,]

    new_desired_left = 1
    increment = 1
    while True:
      l = screenshot[new_desired_top:new_desired_bottom,desired_left-increment-1:desired_left-increment,:,]
      f=oset(list(l.flatten()))
      print(desired_left-increment-1)
      if f==[255]:
        new_desired_left=desired_left-increment-1
        break
      increment+=1
      h=screenshot[new_desired_top:new_desired_bottom,desired_left-increment-10:desired_left-increment+10,:,]

    new_desired_right = 1
    increment = 1
    while True:
      l = screenshot[new_desired_top:new_desired_bottom,desired_right+increment:desired_right+increment+1,:,]
      f=oset(list(l.flatten()))
      print(desired_right+increment+1)
      if f==[255]:
        new_desired_right=desired_right+increment+1
        break
      increment+=1
      h=screenshot[new_desired_top:new_desired_bottom,desired_right+increment-10:desired_right+increment+10,:,]


    h=screenshot[desired_top:desired_bottom,desired_left:desired_right,:,]
    h=screenshot[new_desired_top:new_desired_bottom,new_desired_left:new_desired_right,:,]

    cv2.imwrite(os.path.expanduser('~/venv/venv/photfin.png'),h)

    total_top = dimensions[0]
    total_width=dimensions[1]
    associated_top_percentage=ceil(new_desired_top/total_top)
    associated_bottom_percentage=ceil(new_desired_bottom/total_top)
    associated_left_percentage=ceil(new_desired_left/total_width)
    associated_right_percentage=ceil(new_desired_right/total_width)


    # 2 urls: https://www.aliexpress.com/item/4000630685968.html?
    # https://www.aliexpress.com/item/4000785012684.html?
    # https://www.aliexpress.com/item/32684479974.html?

    new = {}
    for idx,i in enum(p.images):
      new[i.id]={'position':idx,'variant_numbers':[j for j in p.variants if j.image_id == i.id]}
    rm('dataset')
    os.makedirs('dataset')
        
    fns=pool(lambda idx,i:Images().download(i.src,'dataset/%s.png'%idx),lrange(len(p.images)),p.images).result()
    # edit it here. the wms
    def edit(fn):
      import cv2
      screenshot = cv2.imread(fn)
      dimensions = list(tcer(lmap(int,screenshot.shape)[:2]))
      top=ceil(dimensions[0]*associated_top_percentage)
      bottom=ceil(dimensions[0]*associated_bottom_percentage)
      left=ceil(dimensions[0]*associated_left_percentage)
      right=ceil(dimensions[0]*associated_right_percentage)
      screenshot[top:bottom,left:right,:,]=[255,255,255]
      cv2.imwrite(fn,screenshot)
      return fn
    fns = pool(lambda i:edit(i),fns)

    pool(lambda i:i.destroy(),p.images,nodes=4).result()
    p = shop.pfind(id_=p.id)

    fnames = ['dataset/%s.png'%(idx) for idx in lrange(len(new))]
    x = pool(lambda i: Images().image_base64(i).decode(), fnames).result()
    images = lmap(lambda i: {"attachment":i},x)
    print(p.images)
    while True:
      if not p.images:
        print('no images')
        p.images = images
        time.sleep(5)
        p.save()
        p=shop.pfind(id_=p.id)
        time.sleep(5)
        print('saving')
      else:
        break
    p=shop.pfind(id_=p.id)

    for idx,i in enum(p.images):
      match = [new[i] for i in new if new[i]['position'] == idx][0]
      i.variant_ids = sud('id',match['variant_numbers'])
      print('mfoun')
    sud('variant_ids',p.images)

    p.save()
    p=shop.pfind(id_=p.id)

    print(sud('variant_ids',p.images))
    saved['excessdata']['i_want_to_use_photofinish_on_the_product']='editted'
    return saved
  def varied_update(self):
    shop = Shop()
    saveditems=Pickles().loadpickles('items.pkl')
    def update(saved):
      saved=self.i_want_to_refresh_the_stocks_and_prices(saved)
    saveditems = lmap(lambda i:update(i),saveditems)
    Pickles().savepickles(saveditems,'items.pkl',copypickles='store/%sitems.pkl'%str(Time()).replace(':',''))
args=AD(dict(i=33022389035,t='Arr',p='A',d='A',v=None,vnamefire=True,c=False,u=False))
saveditemsargs=AD(dict(i=4000019569219,t=None,p=None,d=None,v=None,vnamefire=None,c=None,u=None))


args=AD(dict(i=4000538721635,t='A',p='A',d='A',v=None,vnamefire=True,c=False,u=False,delete=None))
args=AD(dict(i=33022389035,t='Arr',p='A',d='A',v=None,vnamefire=True,c=False,u=False))
self=ForgotTheName()
Rl=self.click()

args=AD(dict(i=None,t='A',p='A',d='A',v=None,vnamefire=True,
c=False,u=False))
self=ForgotTheName()
Rl=self.click()
