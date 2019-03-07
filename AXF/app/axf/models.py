from django.db import models

class BaseModel(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    trackid = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Wheel(BaseModel):
    class Meta:
        db_table = 'axf_wheel'

class Nav(BaseModel):
    class Meta:
        db_table = 'axf_nav'

class Mustbuy(BaseModel):
    class Meta:
        db_table = 'axf_mustbuy'

class Shop(BaseModel):
    class Meta:
        db_table = 'axf_shop'


class Mainshow(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=100)
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=100)

    img1 = models.CharField(max_length=100)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=10)
    longname1 = models.CharField(max_length=100)
    price1 = models.CharField(max_length=10)
    marketprice1 = models.CharField(max_length=10)

    img2 = models.CharField(max_length=100)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=10)
    longname2 = models.CharField(max_length=100)
    price2 = models.CharField(max_length=10)
    marketprice2 = models.CharField(max_length=10)

    img3 = models.CharField(max_length=100)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=10)
    longname3 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=10)
    marketprice3 = models.CharField(max_length=10)

    class Meta:
        db_table = 'axf_mainshow'


# insert into axf_foodtypes(typeid,typename,childtypenames,typesort)
# values("104749","热销榜","全部分类:0",1),("104747","新品尝鲜","全部分类:0",2),
# ("103532","优选水果","全部分类:0#进口水果:103534#国产水果:103533",3),
# ("103581","卤味熟食","全部分类:0",4),
# ("103536","牛奶面包","全部分类:0#酸奶乳酸菌:103537#牛奶豆浆:103538#面包蛋糕:103540",5),
# ("103549","饮料酒水","全部分类:0#饮用水:103550#茶饮/咖啡:103554#功能饮料:103553#酒类:103555#果汁饮料:103551#碳酸饮料:103552#整箱购:104503#植物蛋白:104489#进口饮料:103556",6),
# ("103541","休闲零食","全部分类:0#进口零食:103547#饼干糕点:103544#膨化食品:103543#坚果炒货:103542#肉干蜜饯:103546#糖果巧克力:103545",7),
# ("103557","方便速食","全部分类:0#方便面:103558#火腿肠卤蛋:103559#速冻面点:103562#下饭小菜:103560#罐头食品:103561#冲调饮品:103563",8),
# ("103569","粮油调味","全部分类:0#杂粮米面油:103570#厨房调味:103571#调味酱:103572",9),
# ("103575","生活用品","全部分类:0#个人护理:103576#纸品:103578#日常用品:103580#家居清洁:103577",10),
# ("104958","冰激凌","全部分类:0",11);
class Foodtypes(models.Model):
    typeid = models.CharField(max_length=20)
    typename = models.CharField(max_length=20)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtypes'




# insert into axf_goods(isxf,pmdesc,specifics,price,marketprice,categoryid,childcid,childcidname,dealerid,storenums,productnum)
# values(,2.500000,103541,103543,"膨化食品","4858",200,4);


class Goods(models.Model):
    productid=models.CharField(max_length=20)
    productimg=models.CharField(max_length=100)
    productname=models.CharField(max_length=100)
    productlongname=models.CharField(max_length=100)
    isxf=models.IntegerField()
    pmdesc=models.IntegerField()
    specifics=models.CharField(max_length=255)
    price=models.IntegerField()
    marketprice=models.FloatField()
    categoryid=models.IntegerField()
    childcid=models.IntegerField()
    childcidname=models.CharField(max_length=100)
    dealerid=models.CharField(max_length=100)
    storenums=models.IntegerField()
    productnum=models.IntegerField()
