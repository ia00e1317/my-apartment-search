from django.db import models

class Article(models.Model):

    bknNumber = models.CharField('物件番号', max_length=20, blank=True)
    bknName = models.CharField('建物名', max_length=60, blank=True)
    price = models.CharField('価格', max_length=20, blank=True)
    priceTsubo = models.CharField('坪単価', max_length=20, blank=True)
    priceSquare = models.CharField('㎡単価', max_length=20, blank=True)
    planType = models.CharField('間取タイプ＋間取部屋数', max_length=10, blank=True)
    planRoom = models.CharField('間取りその他（1）', max_length=30, blank=True)
    address1 = models.CharField('都道府県名+所在地名1', max_length=40, blank=True)
    address2 = models.CharField('所在地名2', max_length=100, blank=True)
    railwayLine = models.CharField('沿線略称（1）', max_length=20, blank=True)
    station1 = models.CharField('駅名（1）', max_length=20, blank=True)
    walkMin1 = models.CharField('徒歩（分）1（1）', max_length=10, blank=True)
    walkMet1 = models.CharField('徒歩（m）2（1）', max_length=20, blank=True)
    station2 = models.CharField('その他交通手段', max_length=200, blank=True)
    walkMin2 = models.CharField('交通（分）1', max_length=10, blank=True)
    walkMet2 = models.CharField('交通（m）2', max_length=20, blank=True)
    environment = models.CharField('周辺環境1（フリー）', max_length=200, blank=True)
    environmentMet = models.CharField('距離1', max_length=20, blank=True)
    environmentMin = models.CharField('時間1', max_length=10, blank=True)

    status = models.CharField('現況', max_length=20, blank=True)
    bknTrade = models.CharField('物件種別', max_length=20, blank=True)
    bknType = models.CharField('物件種目', max_length=20, blank=True)
    exclusiveArea = models.CharField('専有面積', max_length=20, blank=True)
    balArea = models.CharField('バルコニー（テラス）面積', max_length=20, blank=True)
    associationFlag = models.CharField('管理組合有無', max_length=10, blank=True)
    associationType = models.CharField('管理形態', max_length=20, blank=True)
    administrative = models.CharField('管理費', max_length=20, blank=True)
    repairReserve = models.CharField('修繕積立金', max_length=20, blank=True)
    structure = models.CharField('建物構造', max_length=20, blank=True)
    stairs = models.CharField('所在階/地上階層', max_length=10, blank=True)
    balDirection = models.CharField('バルコニー方向（1）', max_length=10, blank=True)
    constructionDate = models.CharField('築年月（西暦）', max_length=10, blank=True)
    extensionDate1 = models.CharField('増改築年月1', max_length=10, blank=True)
    extensionHistory1 = models.CharField('増改築履歴1', max_length=200, blank=True)
    extensionDate2 = models.CharField('増改築年月2', max_length=10, blank=True)
    extensionHistory2 = models.CharField('増改築履歴2', max_length=200, blank=True)
    extensionDate3 = models.CharField('増改築年月3', max_length=10, blank=True)
    extensionHistory3 = models.CharField('増改築履歴3', max_length=200, blank=True)

    pictureFlag = models.CharField('写真有無', max_length=10, blank=True)
    soldout = models.CharField('契約済み', max_length=2, blank=True)

    def __str__(self):
        return self.bknNumber


#画像
class SimplePhoto(models.Model):
    img = models.ImageField(upload_to='images/')
