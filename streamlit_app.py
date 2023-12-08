import ee
service_account = 'test1-783@openmap-407503.iam.gserviceaccount.com'
credentials = ee.ServiceAccountCredentials(service_account, './openmap-407503-3d2d9c2be1d9.json')
ee.Initialize(credentials)
ee.Initialize()
print(ee.Image("NASA/NASADEM_HGT/001").get("title").getInfo())

