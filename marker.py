import re
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Dane wejściowe dla środków ellips
ellips_data = """
[INFO] [1703202019.747602849] [object_detection]: Pointcloud callback.
[INFO] [1703202019.780682532] [object_detection]: Callback Took: 0.0033094s and found 2 legs. Positions: (1.54902,1.17773,0.37321)    (1.64875,-0.848143,0.380178)
[INFO] [1703202019.781474346] [object_detection]: Pointcloud callback.
[INFO] [1703202019.810409920] [object_detection]: Callback Took: 0.0028945s and found 3 legs. Positions: (1.45112,0.802967,0.365828)  (1.55022,-0.749198,0.329264)    (2.64783,0.70504,0.355194)
[INFO] [1703202019.851258916] [object_detection]: Pointcloud callback.
[INFO] [1703202019.880325981] [object_detection]: Callback Took: 0.0029081s and found 3 legs. Positions: (1.4497,1.18902,0.352947)    (1.55061,-0.751096,0.353322)    (2.59733,1.01248,0.359977)
[INFO] [1703202019.948895183] [object_detection]: Pointcloud callback.
[INFO] [1703202019.974037850] [object_detection]: Callback Took: 0.0025162s and found 2 legs. Positions: (1.55229,-0.855745,0.366501) (1.43352,0.801791,0.349006)
[INFO] [1703202020.050155288] [object_detection]: Pointcloud callback.
[INFO] [1703202020.076244419] [object_detection]: Callback Took: 0.0026104s and found 2 legs. Positions: (1.35013,0.852374,0.359475)  (1.49979,-0.600188,0.351397)
[INFO] [1703202020.145336221] [object_detection]: Pointcloud callback.
[INFO] [1703202020.175008349] [object_detection]: Callback Took: 0.0029692s and found 1 legs. Positions: (1.35039,0.803528,0.365685)
[INFO] [1703202020.247929069] [object_detection]: Pointcloud callback.
[INFO] [1703202020.280068597] [object_detection]: Callback Took: 0.0032152s and found 3 legs. Positions: (1.39937,-0.758255,0.365123) (1.25263,0.851036,0.349356)     (3.06802,-0.949788,0.312017)
[INFO] [1703202020.367822585] [object_detection]: Pointcloud callback.
[INFO] [1703202020.397701279] [object_detection]: Callback Took: 0.0029892s and found 3 legs. Positions: (1.25206,1.20049,0.359485)   (1.35049,-0.749117,0.359585)    (3.05213,-0.799492,0.304974)
[INFO] [1703202020.469974479] [object_detection]: Pointcloud callback.
[INFO] [1703202020.498278796] [object_detection]: Callback Took: 0.0028316s and found 3 legs. Positions: (1.34759,-0.89963,0.348703)  (1.24691,0.802915,0.364768)     (2.35988,0.802232,0.356904)
[INFO] [1703202020.559367365] [object_detection]: Pointcloud callback.
[INFO] [1703202020.586926436] [object_detection]: Callback Took: 0.0027572s and found 1 legs. Positions: (1.15033,0.848677,0.357175)
[INFO] [1703202020.656875750] [object_detection]: Pointcloud callback.
[INFO] [1703202020.702061520] [object_detection]: Callback Took: 0.0045198s and found 2 legs. Positions: (1.15012,0.764437,0.36601)   (2.95015,-0.851592,0.337507)
[INFO] [1703202020.757199725] [object_detection]: Pointcloud callback.
[INFO] [1703202020.785443506] [object_detection]: Callback Took: 0.0028256s and found 4 legs. Positions: (1.0966,1.10069,0.372001)    (1.24823,-0.899843,0.372126)    (2.24857,0.761386,0.341828)     (2.8544,-0.900924,0.33919)
[INFO] [1703202020.856709530] [object_detection]: Pointcloud callback.
[INFO] [1703202020.885312477] [object_detection]: Callback Took: 0.0028613s and found 1 legs. Positions: (2.85234,-0.855664,0.366177)
[INFO] [1703202020.955359866] [object_detection]: Pointcloud callback.
[INFO] [1703202020.985163063] [object_detection]: Callback Took: 0.002982s and found 1 legs. Positions: (2.84943,-0.800656,0.369544)
[INFO] [1703202021.052124687] [object_detection]: Pointcloud callback.
[INFO] [1703202021.077812252] [object_detection]: Callback Took: 0.0025701s and found 1 legs. Positions: (2.75062,-0.898178,0.340163)
[INFO] [1703202021.161164879] [object_detection]: Pointcloud callback.
[INFO] [1703202021.192966431] [object_detection]: Callback Took: 0.0031819s and found 1 legs. Positions: (2.0596,0.805344,0.339881)
[INFO] [1703202021.263320126] [object_detection]: Pointcloud callback.
[INFO] [1703202021.287341626] [object_detection]: Callback Took: 0.0024033s and found 1 legs. Positions: (2.75633,-0.603486,0.356697)
[INFO] [1703202021.366432624] [object_detection]: Pointcloud callback.
[INFO] [1703202021.398440459] [object_detection]: Callback Took: 0.0032026s and found 1 legs. Positions: (2.66529,-0.799452,0.360972)
[INFO] [1703202021.459965769] [object_detection]: Pointcloud callback.
[INFO] [1703202021.490448952] [object_detection]: Callback Took: 0.0030487s and found 0 legs. Positions: 
[INFO] [1703202021.559255836] [object_detection]: Pointcloud callback.
[INFO] [1703202021.583827611] [object_detection]: Callback Took: 0.0024586s and found 0 legs. Positions: 
[INFO] [1703202021.659957382] [object_detection]: Pointcloud callback.
[INFO] [1703202021.682872109] [object_detection]: Callback Took: 0.0022933s and found 0 legs. Positions: 
[INFO] [1703202021.762481717] [object_detection]: Pointcloud callback.
[INFO] [1703202021.782714200] [object_detection]: Callback Took: 0.0020242s and found 1 legs. Positions: (1.8265,0.850889,0.352006)
[INFO] [1703202021.865694035] [object_detection]: Pointcloud callback.
[INFO] [1703202021.887922106] [object_detection]: Callback Took: 0.0022241s and found 1 legs. Positions: (1.79311,0.851769,0.346127)
[INFO] [1703202021.964681213] [object_detection]: Pointcloud callback.
[INFO] [1703202021.990243163] [object_detection]: Callback Took: 0.0025568s and found 1 legs. Positions: (2.46135,-0.813492,0.372392)
[INFO] [1703202022.067912327] [object_detection]: Pointcloud callback.
[INFO] [1703202022.088278232] [object_detection]: Callback Took: 0.0020375s and found 0 legs. Positions: 
[INFO] [1703202022.171912445] [object_detection]: Pointcloud callback.
[INFO] [1703202022.192629817] [object_detection]: Callback Took: 0.0020734s and found 0 legs. Positions: 
[INFO] [1703202022.270520754] [object_detection]: Pointcloud callback.
[INFO] [1703202022.290747974] [object_detection]: Callback Took: 0.0020239s and found 1 legs. Positions: (1.64989,0.69937,0.351838)
[INFO] [1703202022.368072636] [object_detection]: Pointcloud callback.
[INFO] [1703202022.388121257] [object_detection]: Callback Took: 0.0020068s and found 2 legs. Positions: (1.55281,1.20033,0.380903)   (2.2499,-0.898471,0.342654)
[INFO] [1703202022.472596739] [object_detection]: Pointcloud callback.
[INFO] [1703202022.495926203] [object_detection]: Callback Took: 0.0023348s and found 1 legs. Positions: (2.24702,-0.851931,0.367374)
[INFO] [1703202022.581625806] [object_detection]: Pointcloud callback.
[INFO] [1703202022.602775032] [object_detection]: Callback Took: 0.0021165s and found 1 legs. Positions: (2.1542,-0.766678,0.357881)
[INFO] [1703202022.680465700] [object_detection]: Pointcloud callback.
[INFO] [1703202022.701446811] [object_detection]: Callback Took: 0.0021025s and found 1 legs. Positions: (2.1502,-0.89676,0.392669)
[INFO] [1703202022.777559725] [object_detection]: Pointcloud callback.
[INFO] [1703202022.798574389] [object_detection]: Callback Took: 0.0021027s and found 1 legs. Positions: (1.45112,1.19909,0.383315)
[INFO] [1703202022.868135542] [object_detection]: Pointcloud callback.
[INFO] [1703202022.890042853] [object_detection]: Callback Took: 0.002192s and found 2 legs. Positions: (1.45024,0.707575,0.354619)   (2.14934,-0.898981,0.343376)
[INFO] [1703202022.974500370] [object_detection]: Pointcloud callback.
[INFO] [1703202022.997078319] [object_detection]: Callback Took: 0.0022605s and found 1 legs. Positions: (2.05185,-0.705152,0.345369)
[INFO] [1703202023.076884523] [object_detection]: Pointcloud callback.
[INFO] [1703202023.099253558] [object_detection]: Callback Took: 0.0022389s and found 1 legs. Positions: (2.05359,-0.752839,0.362961)
[INFO] [1703202023.172283152] [object_detection]: Pointcloud callback.
[INFO] [1703202023.192847488] [object_detection]: Callback Took: 0.0020575s and found 1 legs. Positions: (1.34992,0.759807,0.347119)
[INFO] [1703202023.279984468] [object_detection]: Pointcloud callback.
[INFO] [1703202023.302178472] [object_detection]: Callback Took: 0.0022205s and found 1 legs. Positions: (1.25042,1.23285,0.372696)
[INFO] [1703202023.379394636] [object_detection]: Pointcloud callback.
[INFO] [1703202023.403608425] [object_detection]: Callback Took: 0.0024235s and found 2 legs. Positions: (1.95104,-0.817685,0.36728)  (2.54757,0.802458,0.361415)
[INFO] [1703202023.475602647] [object_detection]: Pointcloud callback.
[INFO] [1703202023.497918209] [object_detection]: Callback Took: 0.0022335s and found 3 legs. Positions: (1.24935,0.70348,0.35127)    (1.85607,-0.852455,0.347438)    (2.50528,0.750612,0.381891)
[INFO] [1703202023.577481643] [object_detection]: Pointcloud callback.
[INFO] [1703202023.600034029] [object_detection]: Callback Took: 0.0022573s and found 3 legs. Positions: (1.15078,1.15137,0.373661)   (1.85104,-0.756258,0.374378)    (2.45778,0.852621,0.387836)
[INFO] [1703202023.680516380] [object_detection]: Pointcloud callback.
[INFO] [1703202023.705113504] [object_detection]: Callback Took: 0.002461s and found 2 legs. Positions: (1.15032,1.06044,0.347496)    (1.8494,-0.850024,0.367285)
[INFO] [1703202023.779841688] [object_detection]: Pointcloud callback.
[INFO] [1703202023.802366463] [object_detection]: Callback Took: 0.0022545s and found 2 legs. Positions: (1.14999,0.764942,0.35322)   (1.76167,-0.756968,0.345858)
[INFO] [1703202023.881248924] [object_detection]: Pointcloud callback.
[INFO] [1703202023.903903364] [object_detection]: Callback Took: 0.0022674s and found 3 legs. Positions: (1.09637,1.06182,0.382323)   (2.35527,0.849763,0.36981)      (1.7524,-0.705622,0.366076)
[INFO] [1703202023.982340836] [object_detection]: Pointcloud callback.
[INFO] [1703202024.007637798] [object_detection]: Callback Took: 0.0025307s and found 1 legs. Positions: (2.34924,0.84762,0.376052)
[INFO] [1703202024.082696023] [object_detection]: Pointcloud callback.
[INFO] [1703202024.103989817] [object_detection]: Callback Took: 0.0021303s and found 1 legs. Positions: (1.65226,-0.657179,0.362298)
[INFO] [1703202024.188015840] [object_detection]: Pointcloud callback.
[INFO] [1703202024.208724223] [object_detection]: Callback Took: 0.0020729s and found 1 legs. Positions: (1.65183,-0.65648,0.374493)
[INFO] [1703202024.290345273] [object_detection]: Pointcloud callback.
[INFO] [1703202024.311964591] [object_detection]: Callback Took: 0.0021631s and found 1 legs. Positions: (1.64933,-0.649348,0.375474)
[INFO] [1703202024.396410083] [object_detection]: Pointcloud callback.
[INFO] [1703202024.418277125] [object_detection]: Callback Took: 0.0021889s and found 2 legs. Positions: (1.5507,-0.900231,0.32814)   (2.1515,0.801904,0.377386)
[INFO] [1703202024.499478846] [object_detection]: Pointcloud callback.
[INFO] [1703202024.525243084] [object_detection]: Callback Took: 0.0025792s and found 2 legs. Positions: (1.55226,-0.747526,0.346427) (2.15034,0.799771,0.381277)
[INFO] [1703202024.603661603] [object_detection]: Pointcloud callback.
[INFO] [1703202024.628532102] [object_detection]: Callback Took: 0.0024887s and found 2 legs. Positions: (1.54892,-0.753095,0.369423) (2.14765,0.800523,0.398075)
[INFO] [1703202024.695390658] [object_detection]: Pointcloud callback.
[INFO] [1703202024.715202925] [object_detection]: Callback Took: 0.0019832s and found 1 legs. Positions: (1.45,-0.758052,0.357491)
[INFO] [1703202024.794180922] [object_detection]: Pointcloud callback.
[INFO] [1703202024.815739497] [object_detection]: Callback Took: 0.0021579s and found 2 legs. Positions: (1.45055,-0.75233,0.336079)  (2.04965,0.79889,0.363494)
[INFO] [1703202024.898000060] [object_detection]: Pointcloud callback.
[INFO] [1703202024.920796142] [object_detection]: Callback Took: 0.0022807s and found 3 legs. Positions: (1.4499,-0.757453,0.377956)  (2.04448,0.752094,0.366191)     (2.95363,-0.801003,0.330577)
[INFO] [1703202024.993562142] [object_detection]: Pointcloud callback.
[INFO] [1703202025.011268953] [object_detection]: Callback Took: 0.0017725s and found 2 legs. Positions: (1.9528,0.852658,0.378333)   (1.35047,-0.648984,0.353515)
[INFO] [1703202025.098518080] [object_detection]: Pointcloud callback.
[INFO] [1703202025.120521675] [object_detection]: Callback Took: 0.0022013s and found 2 legs. Positions: (1.94913,0.850098,0.380949)  (2.91059,-0.699081,0.31886)
[INFO] [1703202025.202851322] [object_detection]: Pointcloud callback.
[INFO] [1703202025.221838293] [object_detection]: Callback Took: 0.0018998s and found 2 legs. Positions: (1.25013,-0.76304,0.340752)  (1.85579,0.799426,0.390371)
[INFO] [1703202025.289059446] [object_detection]: Pointcloud callback.
[INFO] [1703202025.309620119] [object_detection]: Callback Took: 0.0020572s and found 3 legs. Positions: (1.25,-0.712552,0.343037)    (1.8499,0.803683,0.401367)      (2.79542,-0.607631,0.318542)
[INFO] [1703202025.420875653] [object_detection]: Pointcloud callback.
[INFO] [1703202025.450409729] [object_detection]: Callback Took: 0.0029551s and found 0 legs. Positions: 
[INFO] [1703202025.495448346] [object_detection]: Pointcloud callback.
[INFO] [1703202025.516932942] [object_detection]: Callback Took: 0.0021492s and found 2 legs. Positions: (1.14986,-0.757361,0.341105) (1.75175,0.800952,0.364864)
[INFO] [1703202025.606888622] [object_detection]: Pointcloud callback.
[INFO] [1703202025.630673799] [object_detection]: Callback Took: 0.0023804s and found 3 legs. Positions: (1.14975,-0.758853,0.371768) (1.74714,0.851682,0.380131)     (2.65106,-0.898115,0.334916)
[INFO] [1703202025.706477900] [object_detection]: Pointcloud callback.
[INFO] [1703202025.725021223] [object_detection]: Callback Took: 0.0018555s and found 2 legs. Positions: (1.64933,0.70894,0.370113)   (2.64613,-0.900674,0.341303)
[INFO] [1703202025.798207962] [object_detection]: Pointcloud callback.
[INFO] [1703202025.820032686] [object_detection]: Callback Took: 0.0021841s and found 2 legs. Positions: (1.65185,0.799903,0.382003)  (2.62623,-0.749257,0.352593)
[INFO] [1703202025.900257469] [object_detection]: Pointcloud callback.
[INFO] [1703202025.920672683] [object_detection]: Callback Took: 0.0020431s and found 1 legs. Positions: (1.64668,0.803937,0.389739)
[INFO] [1703202026.001299874] [object_detection]: Pointcloud callback.
[INFO] [1703202026.019094679] [object_detection]: Callback Took: 0.0017817s and found 1 legs. Positions: (2.54919,-0.752318,0.353435)
[INFO] [1703202026.123540121] [object_detection]: Pointcloud callback.
[INFO] [1703202026.143026457] [object_detection]: Callback Took: 0.0019498s and found 1 legs. Positions: (1.54937,0.76871,0.359283)
[INFO] [1703202026.205772860] [object_detection]: Pointcloud callback.
[INFO] [1703202026.225121358] [object_detection]: Callback Took: 0.001937s and found 1 legs. Positions: (1.49339,0.852536,0.374839)
[INFO] [1703202026.316353727] [object_detection]: Pointcloud callback.
[INFO] [1703202026.332609803] [object_detection]: Callback Took: 0.0016276s and found 1 legs. Positions: (1.44926,0.848568,0.367003)
[INFO] [1703202026.414803469] [object_detection]: Pointcloud callback.
[INFO] [1703202026.430015761] [object_detection]: Callback Took: 0.0015228s and found 2 legs. Positions: (1.45042,0.854048,0.363237)  (2.41216,-0.865134,0.337468)
[INFO] [1703202026.529925181] [object_detection]: Pointcloud callback.
[INFO] [1703202026.548071575] [object_detection]: Callback Took: 0.0018158s and found 2 legs. Positions: (1.40383,0.849692,0.370774)  (2.35057,-0.810654,0.352328)
[INFO] [1703202026.611183544] [object_detection]: Pointcloud callback.
[INFO] [1703202026.626562542] [object_detection]: Callback Took: 0.00154s and found 1 legs. Positions: (1.35041,0.777417,0.377833)
[INFO] [1703202026.705146264] [object_detection]: Pointcloud callback.
[INFO] [1703202026.719970832] [object_detection]: Callback Took: 0.0014844s and found 3 legs. Positions: (1.34974,0.849941,0.363538)  (2.4824,0.850912,0.385193)      (2.25182,-0.753756,0.325745)
[INFO] [1703202026.808726370] [object_detection]: Pointcloud callback.
[INFO] [1703202026.823216686] [object_detection]: Callback Took: 0.0014511s and found 3 legs. Positions: (0.899555,1.00743,0.375369)  (2.44461,0.848565,0.400796)     (2.25915,-0.711581,0.360419)
[INFO] [1703202026.905458023] [object_detection]: Pointcloud callback.
[INFO] [1703202026.922154736] [object_detection]: Callback Took: 0.0016716s and found 2 legs. Positions: (1.25026,0.780859,0.371687)  (2.24722,-0.675815,0.366918)
[INFO] [1703202027.009262753] [object_detection]: Pointcloud callback.
[INFO] [1703202027.024121087] [object_detection]: Callback Took: 0.0014885s and found 0 legs. Positions: 
[INFO] [1703202027.110502408] [object_detection]: Pointcloud callback.
[INFO] [1703202027.128401747] [object_detection]: Callback Took: 0.0017913s and found 2 legs. Positions: (1.15012,1.14593,0.386427)   (2.32735,0.999692,0.365975)
[INFO] [1703202027.221383292] [object_detection]: Pointcloud callback.
[INFO] [1703202027.236550501] [object_detection]: Callback Took: 0.0015181s and found 2 legs. Positions: (0.999561,1.24296,0.390723)  (2.25287,0.950999,0.377214)
[INFO] [1703202027.314836153] [object_detection]: Pointcloud callback.
[INFO] [1703202027.331643842] [object_detection]: Callback Took: 0.0016833s and found 3 legs. Positions: (1.06908,1.00288,0.388886)   (2.2445,-0.714321,0.363143)     (2.18937,0.898125,0.396693)
[INFO] [1703202027.413796610] [object_detection]: Pointcloud callback.
[INFO] [1703202027.430912335] [object_detection]: Callback Took: 0.0017125s and found 0 legs. Positions: 
[INFO] [1703202027.513995570] [object_detection]: Pointcloud callback.
[INFO] [1703202027.529613893] [object_detection]: Callback Took: 0.0015632s and found 1 legs. Positions: (2.14632,0.999849,0.390524)
[INFO] [1703202027.616971744] [object_detection]: Pointcloud callback.
[INFO] [1703202027.632154120] [object_detection]: Callback Took: 0.001521s and found 2 legs. Positions: (1.94983,1.29993,0.376721)    (1.94908,-0.751204,0.343743)
[INFO] [1703202027.718833761] [object_detection]: Pointcloud callback.
[INFO] [1703202027.734335566] [object_detection]: Callback Took: 0.0015518s and found 0 legs. Positions: 
[INFO] [1703202027.818851828] [object_detection]: Pointcloud callback.
[INFO] [1703202027.834350767] [object_detection]: Callback Took: 0.0015511s and found 2 legs. Positions: (1.95289,0.953499,0.375455)  (1.8497,-0.800335,0.349983)
[INFO] [1703202027.920619973] [object_detection]: Pointcloud callback.
[INFO] [1703202027.932166802] [object_detection]: Callback Took: 0.0011563s and found 1 legs. Positions: (2.1435,0.99605,0.390402)
[INFO] [1703202028.035320764] [object_detection]: Pointcloud callback.
[INFO] [1703202028.049776717] [object_detection]: Callback Took: 0.0014468s and found 2 legs. Positions: (1.74926,-0.66991,0.341796)  (1.87675,0.902064,0.389084)
[INFO] [1703202028.122429094] [object_detection]: Pointcloud callback.
[INFO] [1703202028.139135417] [object_detection]: Callback Took: 0.0016718s and found 0 legs. Positions: 
[INFO] [1703202028.227775727] [object_detection]: Pointcloud callback.
[INFO] [1703202028.241879544] [object_detection]: Callback Took: 0.0014116s and found 2 legs. Positions: (1.65035,-0.798532,0.349218) (1.79663,0.802731,0.366459)
[INFO] [1703202028.324088586] [object_detection]: Pointcloud callback.
[INFO] [1703202028.336952588] [object_detection]: Callback Took: 0.0012878s and found 1 legs. Positions: (1.73149,1.19822,0.384162)
[INFO] [1703202028.434354637] [object_detection]: Pointcloud callback.
[INFO] [1703202028.446212766] [object_detection]: Callback Took: 0.0011886s and found 0 legs. Positions: 
[INFO] [1703202028.525911984] [object_detection]: Pointcloud callback.
[INFO] [1703202028.537517230] [object_detection]: Callback Took: 0.0011627s and found 2 legs. Positions: (1.65128,0.903469,0.384359)  (1.54094,-0.768286,0.341656)
[INFO] [1703202028.637606358] [object_detection]: Pointcloud callback.
[INFO] [1703202028.655290735] [object_detection]: Callback Took: 0.0017698s and found 2 legs. Positions: (1.64409,0.94709,0.373681)   (1.4623,-0.750224,0.37742)
[INFO] [1703202028.725754041] [object_detection]: Pointcloud callback.
[INFO] [1703202028.741387881] [object_detection]: Callback Took: 0.0015651s and found 2 legs. Positions: (1.4498,-0.678217,0.338844)  (1.54909,0.898857,0.40717)
[INFO] [1703202028.831644954] [object_detection]: Pointcloud callback.
[INFO] [1703202028.845352670] [object_detection]: Callback Took: 0.001372s and found 2 legs. Positions: (1.55122,0.852287,0.381521)   (1.44805,-1.04804,0.299673)
[INFO] [1703202028.936369932] [object_detection]: Pointcloud callback.
[INFO] [1703202028.952326341] [object_detection]: Callback Took: 0.0015976s and found 2 legs. Positions: (1.34961,-0.857312,0.337459) (3.05082,-0.654807,0.303015)
[INFO] [1703202029.029222021] [object_detection]: Pointcloud callback.
[INFO] [1703202029.047437715] [object_detection]: Callback Took: 0.0018228s and found 3 legs. Positions: (1.44984,0.853262,0.374458)  (3.04946,-0.800855,0.315132)    (2.56675,0.849427,0.378698)
[INFO] [1703202029.128965726] [object_detection]: Pointcloud callback.
[INFO] [1703202029.146335899] [object_detection]: Callback Took: 0.001739s and found 3 legs. Positions: (1.25009,-0.853664,0.355115)  (1.44146,0.851253,0.387836)     (2.54216,0.900444,0.400048)
[INFO] [1703202029.222693565] [object_detection]: Pointcloud callback.
[INFO] [1703202029.237977302] [object_detection]: Callback Took: 0.0015293s and found 2 legs. Positions: (1.25015,0.801599,0.373562)  (1.2339,-0.950667,0.334613)
[INFO] [1703202029.324103777] [object_detection]: Pointcloud callback.
[INFO] [1703202029.339755231] [object_detection]: Callback Took: 0.0015663s and found 3 legs. Positions: (1.15122,-0.897875,0.374013) (1.35003,0.89641,0.376098)      (2.85166,-0.847399,0.331847)
[INFO] [1703202029.422827363] [object_detection]: Pointcloud callback.
[INFO] [1703202029.435295728] [object_detection]: Callback Took: 0.0012482s and found 1 legs. Positions: (1.14638,-0.9015,0.360388)
[INFO] [1703202029.527791947] [object_detection]: Pointcloud callback.
[INFO] [1703202029.546412962] [object_detection]: Callback Took: 0.0018633s and found 3 legs. Positions: (1.25019,0.857237,0.366979)  (2.75232,-0.816223,0.367811)    (2.35636,0.998794,0.376707)
[INFO] [1703202029.630694487] [object_detection]: Pointcloud callback.
[INFO] [1703202029.648743831] [object_detection]: Callback Took: 0.0018062s and found 2 legs. Positions: (1.2488,0.902187,0.377401)   (2.34767,0.900682,0.395075)
[INFO] [1703202029.730711761] [object_detection]: Pointcloud callback.
[INFO] [1703202029.750169280] [object_detection]: Callback Took: 0.0019466s and found 1 legs. Positions: (1.15022,0.767833,0.375403)
[INFO] [1703202029.827005517] [object_detection]: Pointcloud callback.
[INFO] [1703202029.840652521] [object_detection]: Callback Took: 0.0013656s and found 1 legs. Positions: (1.09931,0.714876,0.369178)
[INFO] [1703202029.926995321] [object_detection]: Pointcloud callback.
[INFO] [1703202029.943027704] [object_detection]: Callback Took: 0.0016048s and found 2 legs. Positions: (1.05082,0.802272,0.373404)  (2.15092,0.851384,0.374479)
[INFO] [1703202030.035165330] [object_detection]: Pointcloud callback.
[INFO] [1703202030.051509720] [object_detection]: Callback Took: 0.0016357s and found 0 legs. Positions: 
[INFO] [1703202030.133257529] [object_detection]: Pointcloud callback.
[INFO] [1703202030.147094188] [object_detection]: Callback Took: 0.0013855s and found 1 legs. Positions: (2.45454,-0.854896,0.365446)
[INFO] [1703202030.235440561] [object_detection]: Pointcloud callback.
[INFO] [1703202030.253807057] [object_detection]: Callback Took: 0.0018393s and found 1 legs. Positions: (2.44866,-0.899381,0.358002)
[INFO] [1703202030.337432712] [object_detection]: Pointcloud callback.
[INFO] [1703202030.348041730] [object_detection]: Callback Took: 0.0010625s and found 1 legs. Positions: (2.04383,0.751647,0.366733)
[INFO] [1703202030.435506808] [object_detection]: Pointcloud callback.
[INFO] [1703202030.455098129] [object_detection]: Callback Took: 0.0019609s and found 3 legs. Positions: (0.999296,1.10921,0.418495)  (1.95155,0.850215,0.373912)     (2.34914,-0.851812,0.359976)
[INFO] [1703202030.535853162] [object_detection]: Pointcloud callback.
[INFO] [1703202030.548725702] [object_detection]: Callback Took: 0.0012883s and found 1 legs. Positions: (2.26408,-0.917396,0.37866)
[INFO] [1703202030.633045684] [object_detection]: Pointcloud callback.
[INFO] [1703202030.645955058] [object_detection]: Callback Took: 0.001292s and found 1 legs. Positions: (2.25045,-0.917882,0.389418)
[INFO] [1703202030.739266709] [object_detection]: Pointcloud callback.
[INFO] [1703202030.751806203] [object_detection]: Callback Took: 0.0012567s and found 1 legs. Positions: (1.84937,0.75572,0.354568)
[INFO] [1703202030.849285081] [object_detection]: Pointcloud callback.
[INFO] [1703202030.862822802] [object_detection]: Callback Took: 0.001355s and found 2 legs. Positions: (2.14963,-0.959486,0.35493)   (1.75759,0.849219,0.372204)
[INFO] [1703202030.944483454] [object_detection]: Pointcloud callback.
[INFO] [1703202030.956990237] [object_detection]: Callback Took: 0.0012526s and found 2 legs. Positions: (1.92768,0.802335,0.386588)  (2.05696,-0.800195,0.359262)
[INFO] [1703202031.044437068] [object_detection]: Pointcloud callback.
[INFO] [1703202031.056528245] [object_detection]: Callback Took: 0.0012107s and found 2 legs. Positions: (2.05833,-0.913855,0.383484) (1.65756,0.751524,0.348506)
[INFO] [1703202031.146012110] [object_detection]: Pointcloud callback.
[INFO] [1703202031.159906113] [object_detection]: Callback Took: 0.0013911s and found 1 legs. Positions: (1.64987,1.10681,0.377503)
[INFO] [1703202031.253543452] [object_detection]: Pointcloud callback.
[INFO] [1703202031.270045311] [object_detection]: Callback Took: 0.0016515s and found 1 legs. Positions: (1.95859,-0.857675,0.336263)
[INFO] [1703202031.356297943] [object_detection]: Pointcloud callback.
[INFO] [1703202031.369438007] [object_detection]: Callback Took: 0.0013154s and found 2 legs. Positions: (1.55162,0.756528,0.364418)  (1.94616,-0.879343,0.355399)
[INFO] [1703202031.453170849] [object_detection]: Pointcloud callback.
[INFO] [1703202031.467301510] [object_detection]: Callback Took: 0.001415s and found 1 legs. Positions: (1.54965,1.12431,0.374461)
[INFO] [1703202031.553788913] [object_detection]: Pointcloud callback.
[INFO] [1703202031.569760492] [object_detection]: Callback Took: 0.0015983s and found 1 legs. Positions: (1.45135,0.900955,0.371918)
[INFO] [1703202031.644870817] [object_detection]: Pointcloud callback.
[INFO] [1703202031.659706002] [object_detection]: Callback Took: 0.0014846s and found 2 legs. Positions: (1.45069,0.74824,0.37252)    (1.7503,-0.949999,0.364302)
[INFO] [1703202031.747789067] [object_detection]: Pointcloud callback.
[INFO] [1703202031.761677828] [object_detection]: Callback Took: 0.00139s and found 1 legs. Positions: (1.1358,1.15331,0.368466)
[INFO] [1703202031.844631220] [object_detection]: Pointcloud callback.
[INFO] [1703202031.860851409] [object_detection]: Callback Took: 0.0016232s and found 2 legs. Positions: (1.10121,0.847528,0.356842)  (1.74552,-1.15237,0.291752)
[INFO] [1703202031.948895264] [object_detection]: Pointcloud callback.
[INFO] [1703202031.962806391] [object_detection]: Callback Took: 0.0013926s and found 3 legs. Positions: (1.64987,-0.924061,0.369644) (1.29291,0.851384,0.369912)     (2.55524,0.804449,0.359437)
[INFO] [1703202032.051852004] [object_detection]: Pointcloud callback.
[INFO] [1703202032.067715047] [object_detection]: Callback Took: 0.0015884s and found 3 legs. Positions: (1.24977,0.851722,0.351744)  (1.64922,-0.860267,0.379831)    (2.55123,0.79975,0.370415)
[INFO] [1703202032.153733285] [object_detection]: Pointcloud callback.
[INFO] [1703202032.164785638] [object_detection]: Callback Took: 0.0011066s and found 2 legs. Positions: (1.04767,0.950589,0.368857)  (1.54985,-0.768378,0.341254)
[INFO] [1703202032.261075253] [object_detection]: Pointcloud callback.
[INFO] [1703202032.280657546] [object_detection]: Callback Took: 0.0019594s and found 3 legs. Positions: (0.999261,0.901104,0.356628) (1.55017,-0.950287,0.337009)    (2.45194,0.849354,0.380394)
[INFO] [1703202032.354024363] [object_detection]: Pointcloud callback.
[INFO] [1703202032.369969949] [object_detection]: Callback Took: 0.0015958s and found 1 legs. Positions: (0.998756,0.850599,0.360598)
[INFO] [1703202032.451358239] [object_detection]: Pointcloud callback.
[INFO] [1703202032.469670588] [object_detection]: Callback Took: 0.0018325s and found 1 legs. Positions: (0.950082,1.23895,0.369145)
[INFO] [1703202032.555676595] [object_detection]: Pointcloud callback.
[INFO] [1703202032.577580501] [object_detection]: Callback Took: 0.0021918s and found 1 legs. Positions: (1.20366,-0.899863,0.335998)
[INFO] [1703202032.656787312] [object_detection]: Pointcloud callback.
[INFO] [1703202032.676099471] [object_detection]: Callback Took: 0.0019327s and found 1 legs. Positions: (2.95321,-0.847673,0.314258)
[INFO] [1703202032.753544786] [object_detection]: Pointcloud callback.
[INFO] [1703202032.776318083] [object_detection]: Callback Took: 0.0022793s and found 1 legs. Positions: (2.95072,-0.94917,0.317125)
[INFO] [1703202032.853793731] [object_detection]: Pointcloud callback.
[INFO] [1703202032.870401686] [object_detection]: Callback Took: 0.001662s and found 1 legs. Positions: (2.1553,0.849422,0.373558)
[INFO] [1703202032.963642247] [object_detection]: Pointcloud callback.
[INFO] [1703202032.981776581] [object_detection]: Callback Took: 0.0018145s and found 1 legs. Positions: (2.1486,0.901777,0.380286)
[INFO] [1703202033.060100557] [object_detection]: Pointcloud callback.
[INFO] [1703202033.079510952] [object_detection]: Callback Took: 0.0019421s and found 1 legs. Positions: (2.05504,0.902076,0.393536)
[INFO] [1703202033.165471154] [object_detection]: Pointcloud callback.
[INFO] [1703202033.181369853] [object_detection]: Callback Took: 0.0015913s and found 1 legs. Positions: (1.04866,-0.858118,0.381288)
[INFO] [1703202033.270921148] [object_detection]: Pointcloud callback.
[INFO] [1703202033.283090859] [object_detection]: Callback Took: 0.0012189s and found 1 legs. Positions: (1.95162,0.852421,0.3637)
[INFO] [1703202033.364734075] [object_detection]: Pointcloud callback.
[INFO] [1703202033.379179661] [object_detection]: Callback Took: 0.0014459s and found 2 legs. Positions: (1.9468,0.901017,0.383417)   (2.65088,-0.752496,0.364157)
[INFO] [1703202033.476926638] [object_detection]: Pointcloud callback.
[INFO] [1703202033.488216834] [object_detection]: Callback Took: 0.0011304s and found 2 legs. Positions: (2.61485,-0.877577,0.385579) (1.89416,0.801793,0.408803)
[INFO] [1703202033.559560636] [object_detection]: Pointcloud callback.
[INFO] [1703202033.575085486] [object_detection]: Callback Took: 0.0015536s and found 1 legs. Positions: (1.84712,0.759856,0.353412)
[INFO] [1703202033.663017745] [object_detection]: Pointcloud callback.
[INFO] [1703202033.673755939] [object_detection]: Callback Took: 0.0010751s and found 0 legs. Positions: 
[INFO] [1703202033.762333646] [object_detection]: Pointcloud callback.
[INFO] [1703202033.779003807] [object_detection]: Callback Took: 0.0016682s and found 2 legs. Positions: (1.75361,0.759987,0.363496)  (2.45039,-0.801404,0.33993)
[INFO] [1703202033.866119455] [object_detection]: Pointcloud callback.
[INFO] [1703202033.877962282] [object_detection]: Callback Took: 0.0011888s and found 1 legs. Positions: (2.44861,-0.753958,0.349185)
[INFO] [1703202033.967010709] [object_detection]: Pointcloud callback.
[INFO] [1703202033.979176365] [object_detection]: Callback Took: 0.0012186s and found 2 legs. Positions: (1.65572,0.757232,0.360997)  (2.40857,-0.755454,0.360552)
[INFO] [1703202034.068354604] [object_detection]: Pointcloud callback.
[INFO] [1703202034.081563717] [object_detection]: Callback Took: 0.0013232s and found 0 legs. Positions: 
[INFO] [1703202034.170701418] [object_detection]: Pointcloud callback.
[INFO] [1703202034.181268387] [object_detection]: Callback Took: 0.0010589s and found 1 legs. Positions: (1.63055,0.752408,0.365189)
[INFO] [1703202034.275913676] [object_detection]: Pointcloud callback.
[INFO] [1703202034.291263119] [object_detection]: Callback Took: 0.0015361s and found 1 legs. Positions: (1.54998,0.796318,0.372457)
[INFO] [1703202034.380117134] [object_detection]: Pointcloud callback.
[INFO] [1703202034.392906415] [object_detection]: Callback Took: 0.0012795s and found 1 legs. Positions: (1.54962,0.74906,0.350082)
[INFO] [1703202034.478695656] [object_detection]: Pointcloud callback.
[INFO] [1703202034.490372418] [object_detection]: Callback Took: 0.0011698s and found 1 legs. Positions: (1.24907,0.850127,0.401022)
[INFO] [1703202034.580108452] [object_detection]: Pointcloud callback.
[INFO] [1703202034.595321050] [object_detection]: Callback Took: 0.0015225s and found 2 legs. Positions: (1.44974,0.798966,0.372964)  (2.56078,0.753155,0.37582)
[INFO] [1703202034.674414702] [object_detection]: Pointcloud callback.
[INFO] [1703202034.687994865] [object_detection]: Callback Took: 0.0013597s and found 3 legs. Positions: (1.40048,0.974392,0.390739)  (2.0504,-0.802534,0.373235)     (2.53394,0.703614,0.37588)
[INFO] [1703202034.773721135] [object_detection]: Pointcloud callback.
[INFO] [1703202034.788829945] [object_detection]: Callback Took: 0.0015127s and found 3 legs. Positions: (1.3497,1.04764,0.369177)    (2.04685,-0.850311,0.371506)    (2.46544,0.754981,0.378379)
[INFO] [1703202034.875292373] [object_detection]: Pointcloud callback.
[INFO] [1703202034.891231833] [object_detection]: Callback Took: 0.001596s and found 1 legs. Positions: (2.45011,0.751919,0.397122)
[INFO] [1703202034.987245370] [object_detection]: Pointcloud callback.
[INFO] [1703202035.001926030] [object_detection]: Callback Took: 0.0014696s and found 1 legs. Positions: (2.35051,0.753013,0.398723)
[INFO] [1703202035.079148408] [object_detection]: Pointcloud callback.
[INFO] [1703202035.094423163] [object_detection]: Callback Took: 0.0015289s and found 1 legs. Positions: (1.2487,0.800943,0.366236)
[INFO] [1703202035.177652983] [object_detection]: Pointcloud callback.
[INFO] [1703202035.195178607] [object_detection]: Callback Took: 0.0017544s and found 3 legs. Positions: (1.84983,-0.857316,0.378154) (1.15488,0.667934,0.347781)     (2.32235,0.755044,0.34612)
[INFO] [1703202035.278548276] [object_detection]: Pointcloud callback.
[INFO] [1703202035.296984355] [object_detection]: Callback Took: 0.0018449s and found 3 legs. Positions: (1.1515,1.10823,0.381962)    (1.84923,-0.849378,0.381885)    (2.26177,0.75161,0.368445)
[INFO] [1703202035.381310116] [object_detection]: Pointcloud callback.
[INFO] [1703202035.397119457] [object_detection]: Callback Took: 0.0015821s and found 3 legs. Positions: (1.14939,0.671312,0.369922)  (1.75441,-0.899723,0.344305)    (2.24951,0.752089,0.383688)
[INFO] [1703202035.481877836] [object_detection]: Pointcloud callback.
[INFO] [1703202035.498548219] [object_detection]: Callback Took: 0.0016682s and found 2 legs. Positions: (1.10004,1.17319,0.379154)   (1.74935,-0.851603,0.360012)
[INFO] [1703202035.582954633] [object_detection]: Pointcloud callback.
[INFO] [1703202035.601630782] [object_detection]: Callback Took: 0.00187s and found 2 legs. Positions: (2.15652,0.749534,0.372297)    (1.71088,-1.04781,0.371038)
[INFO] [1703202035.680517793] [object_detection]: Pointcloud callback.
[INFO] [1703202035.696540927] [object_detection]: Callback Took: 0.0016036s and found 1 legs. Positions: (2.14133,0.801214,0.379712)
[INFO] [1703202035.785042811] [object_detection]: Pointcloud callback.
[INFO] [1703202035.805902945] [object_detection]: Callback Took: 0.0020872s and found 1 legs. Positions: (1.85264,0.898829,0.388913)
[INFO] [1703202035.883614689] [object_detection]: Pointcloud callback.
[INFO] [1703202035.902352621] [object_detection]: Callback Took: 0.0018746s and found 1 legs. Positions: (1.55355,-0.859862,0.375726)
[INFO] [1703202035.983907882] [object_detection]: Pointcloud callback.
[INFO] [1703202036.000144111] [object_detection]: Callback Took: 0.0016249s and found 1 legs. Positions: (1.55135,-0.909398,0.36045)
[INFO] [1703202036.090449613] [object_detection]: Pointcloud callback.
[INFO] [1703202036.109285865] [object_detection]: Callback Took: 0.0018862s and found 2 legs. Positions: (1.96174,0.703158,0.361597)  (3.05018,-1.05019,0.298633)
[INFO] [1703202036.191342377] [object_detection]: Pointcloud callback.
[INFO] [1703202036.208382554] [object_detection]: Callback Took: 0.0017069s and found 3 legs. Positions: (2.14991,0.799332,0.36951)   (1.45025,-1.049,0.390041)       (3.04525,-1.14644,0.309324)
[INFO] [1703202036.286451483] [object_detection]: Pointcloud callback.
[INFO] [1703202036.302961553] [object_detection]: Callback Took: 0.0016537s and found 3 legs. Positions: (1.45057,-1.05135,0.364729)  (2.14701,0.802434,0.375775)     (2.96896,-0.998729,0.315863)
[INFO] [1703202036.394025558] [object_detection]: Pointcloud callback.
[INFO] [1703202036.411866732] [object_detection]: Callback Took: 0.0017861s and found 3 legs. Positions: (1.45026,-0.904925,0.354396) (2.09368,0.745248,0.384913)     (2.9454,-0.862412,0.314225)
[INFO] [1703202036.498540665] [object_detection]: Pointcloud callback.
[INFO] [1703202036.514147700] [object_detection]: Callback Took: 0.0015628s and found 1 legs. Positions: (1.85237,0.749455,0.391157)
[INFO] [1703202036.588131482] [object_detection]: Pointcloud callback.
[INFO] [1703202036.603635291] [object_detection]: Callback Took: 0.0015515s and found 3 legs. Positions: (1.84986,0.751675,0.387772)  (1.1523,-1.00155,0.359891)      (2.94374,-1.09585,0.310756)
[INFO] [1703202036.693478198] [object_detection]: Pointcloud callback.
[INFO] [1703202036.707535166] [object_detection]: Callback Took: 0.0014071s and found 2 legs. Positions: (2.09159,0.747112,0.395876)  (1.44805,-0.907814,0.330673)
[INFO] [1703202036.785574463] [object_detection]: Pointcloud callback.
[INFO] [1703202036.802261910] [object_detection]: Callback Took: 0.00167s and found 3 legs. Positions: (2.48101,0.902587,0.393354)    (1.44584,-0.907859,0.332921)    (2.94949,-0.904184,0.32191)
[INFO] [1703202036.891982860] [object_detection]: Pointcloud callback.
[INFO] [1703202036.908181225] [object_detection]: Callback Took: 0.0016218s and found 3 legs. Positions: (1.44992,-0.906456,0.346202) (2.09687,0.75305,0.394014)      (2.95287,-0.868969,0.321069)
[INFO] [1703202036.989744461] [object_detection]: Pointcloud callback.
[INFO] [1703202037.005477645] [object_detection]: Callback Took: 0.0015751s and found 2 legs. Positions: (1.19908,-0.905385,0.343886) (2.95123,-0.812895,0.316685)
[INFO] [1703202037.093929990] [object_detection]: Pointcloud callback.
[INFO] [1703202037.110024731] [object_detection]: Callback Took: 0.0016107s and found 2 legs. Positions: (1.44942,-0.904593,0.340892) (2.94971,-0.858767,0.32037)
[INFO] [1703202037.194760420] [object_detection]: Pointcloud callback.
[INFO] [1703202037.209926697] [object_detection]: Callback Took: 0.0015178s and found 3 legs. Positions: (1.44988,-0.904454,0.345642) (2.10071,0.754604,0.391225)     (2.94991,-0.863033,0.317571)
[INFO] [1703202037.293656906] [object_detection]: Pointcloud callback.
[INFO] [1703202037.311415053] [object_detection]: Callback Took: 0.0017779s and found 3 legs. Positions: (2.09739,0.752714,0.389993)  (2.95095,-1.06369,0.322078)     (1.18554,-1.19485,0.333324)
[INFO] [1703202037.393470114] [object_detection]: Pointcloud callback.
[INFO] [1703202037.413411146] [object_detection]: Callback Took: 0.0019961s and found 3 legs. Positions: (1.24894,-0.904917,0.358176) (2.09314,0.746473,0.392749)     (2.94947,-0.858757,0.314983)
[INFO] [1703202037.492684381] [object_detection]: Pointcloud callback.
[INFO] [1703202037.508756687] [object_detection]: Callback Took: 0.0016093s and found 3 legs. Positions: (1.20134,-0.905474,0.334368) (2.0963,0.757225,0.39597)       (2.94999,-0.864044,0.316791)
[INFO] [1703202037.600235459] [object_detection]: Pointcloud callback.
[INFO] [1703202037.616039955] [object_detection]: Callback Took: 0.0015823s and found 3 legs. Positions: (1.44811,-0.903802,0.341279) (2.09355,0.751915,0.391928)     (2.95126,-0.864298,0.317945)
[INFO] [1703202037.696663358] [object_detection]: Pointcloud callback.
[INFO] [1703202037.713701448] [object_detection]: Callback Took: 0.0017053s and found 3 legs. Positions: (1.25135,-0.905037,0.354351) (2.09396,0.755148,0.39222)      (2.94994,-0.862885,0.31493)
[INFO] [1703202037.802659426] [object_detection]: Pointcloud callback.
[INFO] [1703202037.818392636] [object_detection]: Callback Took: 0.0015748s and found 3 legs. Positions: (1.44751,-0.905789,0.341685) (2.081,0.744436,0.389033)       (2.95186,-0.86559,0.317259)
[INFO] [1703202037.902381500] [object_detection]: Pointcloud callback.
[INFO] [1703202037.918232611] [object_detection]: Callback Took: 0.0015861s and found 3 legs. Positions: (1.44945,-0.904144,0.336027) (2.09975,0.755781,0.392297)     (2.94995,-0.865595,0.318918)
[INFO] [1703202038.016200541] [object_detection]: Pointcloud callback.
[INFO] [1703202038.035644724] [object_detection]: Callback Took: 0.0019465s and found 3 legs. Positions: (1.45034,-0.906149,0.339043) (2.1,0.750208,0.391436) (2.94814,-0.862723,0.32218)
[INFO] [1703202038.105137365] [object_detection]: Pointcloud callback.
[INFO] [1703202038.123567693] [object_detection]: Callback Took: 0.0018444s and found 3 legs. Positions: (1.2509,-0.907137,0.356021)  (2.09389,0.751389,0.390134)     (2.95064,-0.86165,0.318371)
[INFO] [1703202038.206926323] [object_detection]: Pointcloud callback.
[INFO] [1703202038.223451104] [object_detection]: Callback Took: 0.0016539s and found 3 legs. Positions: (1.44908,-0.903505,0.344289) (2.09362,0.751359,0.393272)     (2.95018,-0.861756,0.319262)
[INFO] [1703202038.305464334] [object_detection]: Pointcloud callback.
[INFO] [1703202038.322738517] [object_detection]: Callback Took: 0.0017301s and found 3 legs. Positions: (1.24977,-0.957392,0.333998) (2.09478,0.755708,0.392373)     (2.95097,-0.864608,0.317829)
[INFO] [1703202038.404008425] [object_detection]: Pointcloud callback.
[INFO] [1703202038.420934359] [object_detection]: Callback Took: 0.0016942s and found 3 legs. Positions: (1.44913,-0.906368,0.334806) (2.09874,0.751503,0.392729)     (2.95085,-0.863317,0.31965)
[INFO] [1703202038.505902564] [object_detection]: Pointcloud callback.
[INFO] [1703202038.522630018] [object_detection]: Callback Took: 0.001675s and found 3 legs. Positions: (1.45022,-0.905307,0.355534)  (2.09433,0.752622,0.390551)     (2.95024,-0.864349,0.319385)
[INFO] [1703202038.607199306] [object_detection]: Pointcloud callback.
[INFO] [1703202038.624801260] [object_detection]: Callback Took: 0.0017616s and found 3 legs. Positions: (1.44393,-0.904608,0.341348) (2.08741,0.752732,0.376231)     (2.95019,-0.864624,0.31895)
[INFO] [1703202038.709299752] [object_detection]: Pointcloud callback.
[INFO] [1703202038.728347464] [object_detection]: Callback Took: 0.0019076s and found 3 legs. Positions: (1.44972,-0.901501,0.344269) (2.09658,0.752048,0.39214)      (2.9493,-0.862415,0.317644)
"""

# Przetwarzanie danych
timestamps_ellips = []
durations_ellips = []
legs_counts_ellips = []
positions_ellips = []

for line in ellips_data.split('\n'):
    if 'Callback Took' in line:
        timestamp_ellips = float(re.search(r'\[([\d.]+)\]', line).group(1))
        duration_ellips = float(re.search(r'Callback Took: ([\d.]+)s', line).group(1))
        legs_count_ellips = int(re.search(r'found (\d+) legs', line).group(1))
        timestamps_ellips.append(timestamp_ellips - 1703007741.740538357)
        durations_ellips.append(duration_ellips)
        legs_counts_ellips.append(legs_count_ellips)

        if re.search(r'Positions: \((.+)\)', line) != None:
            positions_str = re.search(r'Positions: \((.+)\)', line).group(1)
            positions_ellips.append([tuple(map(float, pos.strip('()').split(','))) for pos in positions_str.split()])

# Rysowanie wykresu środków ellips
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(111, projection='3d')
for i, positions in enumerate(positions_ellips):
    xs, ys, zs = zip(*positions)
    ax.scatter(xs, ys, zs, label=f'Callback {i+1}')

ax.set_title('Środki ellips')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.set_xlim3d(left=0, right=5)
ax.set_ylim3d(bottom=2, top=-2) 
ax.set_zlim3d(bottom=0, top=1.5) 

# Rysowanie wykresu długości callbacku od czasu
plt.figure(figsize=(10, 5))
plt.plot(timestamps_ellips, durations_ellips, marker='o', linestyle='-', color='r')
plt.title('Długość trwania callbacku od czasu')
plt.xlabel('Czas [s]')
plt.ylabel('Długość trwania callbacku [s]')
plt.grid(True)

# Rysowanie wykresu ilości nóg od czasu
plt.figure(figsize=(10, 5))
plt.plot(timestamps_ellips, legs_counts_ellips, marker='o', linestyle='-', color='b')
plt.title('Ilość nóg od czasu')
plt.xlabel('Czas [s]')
plt.ylabel('Ilość sklasyfikowanych nóg')
plt.grid(True)
plt.show()
