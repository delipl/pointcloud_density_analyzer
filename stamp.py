import matplotlib.pyplot as plt
import re

# Dane wejściowe
log_data = """
[INFO] [1702984137.807152395] [object_detection]: Pointcloud callback.
[INFO] [1702984137.827952002] [object_detection]: Callback Took: 0.0020813s
[INFO] [1702984137.898247762] [object_detection]: Pointcloud callback.
[INFO] [1702984137.915497482] [object_detection]: Callback Took: 0.001726s
[INFO] [1702984138.000514433] [object_detection]: Pointcloud callback.
[INFO] [1702984138.011466226] [object_detection]: Callback Took: 0.0010966s
[INFO] [1702984138.098293739] [object_detection]: Pointcloud callback.
[INFO] [1702984138.117388942] [object_detection]: Callback Took: 0.0019108s
[INFO] [1702984138.199022997] [object_detection]: Pointcloud callback.
[INFO] [1702984138.213914530] [object_detection]: Callback Took: 0.0014903s
[INFO] [1702984138.296144469] [object_detection]: Pointcloud callback.
[INFO] [1702984138.310067584] [object_detection]: Callback Took: 0.0013935s
[INFO] [1702984138.402033312] [object_detection]: Pointcloud callback.
[INFO] [1702984138.416094992] [object_detection]: Callback Took: 0.0014074s
[INFO] [1702984138.501387536] [object_detection]: Pointcloud callback.
[INFO] [1702984138.516408555] [object_detection]: Callback Took: 0.0015034s
[INFO] [1702984138.607472773] [object_detection]: Pointcloud callback.
[INFO] [1702984138.621198377] [object_detection]: Callback Took: 0.0013739s
[INFO] [1702984138.707398298] [object_detection]: Pointcloud callback.
[INFO] [1702984138.721085350] [object_detection]: Callback Took: 0.0013699s
[INFO] [1702984138.808889173] [object_detection]: Pointcloud callback.
[INFO] [1702984138.824954806] [object_detection]: Callback Took: 0.0016079s
[INFO] [1702984138.916349582] [object_detection]: Pointcloud callback.
[INFO] [1702984138.933241715] [object_detection]: Callback Took: 0.0016904s
[INFO] [1702984139.018819141] [object_detection]: Pointcloud callback.
[INFO] [1702984139.032143858] [object_detection]: Callback Took: 0.0013337s
[INFO] [1702984139.115706646] [object_detection]: Pointcloud callback.
[INFO] [1702984139.129873297] [object_detection]: Callback Took: 0.0014179s
[INFO] [1702984139.216694315] [object_detection]: Pointcloud callback.
[INFO] [1702984139.238118441] [object_detection]: Callback Took: 0.0021439s
[INFO] [1702984139.307712368] [object_detection]: Pointcloud callback.
[INFO] [1702984139.322883405] [object_detection]: Callback Took: 0.0015185s
[INFO] [1702984139.410473654] [object_detection]: Pointcloud callback.
[INFO] [1702984139.423925970] [object_detection]: Callback Took: 0.0013467s
[INFO] [1702984139.517597708] [object_detection]: Pointcloud callback.
[INFO] [1702984139.533786121] [object_detection]: Callback Took: 0.0016201s
[INFO] [1702984139.611635832] [object_detection]: Pointcloud callback.
[INFO] [1702984139.626721174] [object_detection]: Callback Took: 0.0015098s
[INFO] [1702984139.714613695] [object_detection]: Pointcloud callback.
[INFO] [1702984139.731753346] [object_detection]: Callback Took: 0.0017151s
[INFO] [1702984139.816481503] [object_detection]: Pointcloud callback.
[INFO] [1702984139.828459822] [object_detection]: Callback Took: 0.0011991s
[INFO] [1702984139.912908894] [object_detection]: Pointcloud callback.
[INFO] [1702984139.933507149] [object_detection]: Callback Took: 0.002061s
[INFO] [1702984140.016453798] [object_detection]: Pointcloud callback.
[INFO] [1702984140.032941970] [object_detection]: Callback Took: 0.00165s
[INFO] [1702984140.113320350] [object_detection]: Pointcloud callback.
[INFO] [1702984140.133522046] [object_detection]: Callback Took: 0.0020215s
[INFO] [1702984140.217791906] [object_detection]: Pointcloud callback.
[INFO] [1702984140.240994677] [object_detection]: Callback Took: 0.0023216s
[INFO] [1702984140.319048952] [object_detection]: Pointcloud callback.
[INFO] [1702984140.336189441] [object_detection]: Callback Took: 0.0017151s
[INFO] [1702984140.416171612] [object_detection]: Pointcloud callback.
[INFO] [1702984140.437651541] [object_detection]: Callback Took: 0.0021491s
[INFO] [1702984140.516663758] [object_detection]: Pointcloud callback.
[INFO] [1702984140.533566856] [object_detection]: Callback Took: 0.0016904s
[INFO] [1702984140.626419287] [object_detection]: Pointcloud callback.
[INFO] [1702984140.646297549] [object_detection]: Callback Took: 0.0019892s
[INFO] [1702984140.733404148] [object_detection]: Pointcloud callback.
[INFO] [1702984140.753611641] [object_detection]: Callback Took: 0.002022s
[INFO] [1702984140.828279877] [object_detection]: Pointcloud callback.
[INFO] [1702984140.844729148] [object_detection]: Callback Took: 0.0016463s
[INFO] [1702984140.933047490] [object_detection]: Pointcloud callback.
[INFO] [1702984140.945585306] [object_detection]: Callback Took: 0.001255s
[INFO] [1702984141.027216357] [object_detection]: Pointcloud callback.
[INFO] [1702984141.042033090] [object_detection]: Callback Took: 0.0014829s
[INFO] [1702984141.139593025] [object_detection]: Pointcloud callback.
[INFO] [1702984141.151227236] [object_detection]: Callback Took: 0.0011646s
[INFO] [1702984141.222167770] [object_detection]: Pointcloud callback.
[INFO] [1702984141.239018417] [object_detection]: Callback Took: 0.0016863s
[INFO] [1702984141.325712324] [object_detection]: Pointcloud callback.
[INFO] [1702984141.336247584] [object_detection]: Callback Took: 0.001055s
[INFO] [1702984141.424456416] [object_detection]: Pointcloud callback.
[INFO] [1702984141.439769301] [object_detection]: Callback Took: 0.0015325s
[INFO] [1702984141.528658665] [object_detection]: Pointcloud callback.
[INFO] [1702984141.540909573] [object_detection]: Callback Took: 0.0012263s
[INFO] [1702984141.629399864] [object_detection]: Pointcloud callback.
[INFO] [1702984141.641219434] [object_detection]: Callback Took: 0.0011833s
[INFO] [1702984141.731175202] [object_detection]: Pointcloud callback.
[INFO] [1702984141.744084294] [object_detection]: Callback Took: 0.0012922s
[INFO] [1702984141.833101956] [object_detection]: Pointcloud callback.
[INFO] [1702984141.843067173] [object_detection]: Callback Took: 0.0009979s
[INFO] [1702984141.938550730] [object_detection]: Pointcloud callback.
[INFO] [1702984141.953605482] [object_detection]: Callback Took: 0.0015077s
[INFO] [1702984142.042804940] [object_detection]: Pointcloud callback.
[INFO] [1702984142.055516032] [object_detection]: Callback Took: 0.0012725s
[INFO] [1702984142.141238448] [object_detection]: Pointcloud callback.
[INFO] [1702984142.153480627] [object_detection]: Callback Took: 0.0012256s
[INFO] [1702984142.242205025] [object_detection]: Pointcloud callback.
[INFO] [1702984142.257944570] [object_detection]: Callback Took: 0.0015752s
[INFO] [1702984142.336889669] [object_detection]: Pointcloud callback.
[INFO] [1702984142.349317206] [object_detection]: Callback Took: 0.0012442s
[INFO] [1702984142.436185017] [object_detection]: Pointcloud callback.
[INFO] [1702984142.451110144] [object_detection]: Callback Took: 0.0014938s
[INFO] [1702984142.537693003] [object_detection]: Pointcloud callback.
[INFO] [1702984142.555411637] [object_detection]: Callback Took: 0.0017731s
[INFO] [1702984142.639353941] [object_detection]: Pointcloud callback.
[INFO] [1702984142.654724585] [object_detection]: Callback Took: 0.0015386s
[INFO] [1702984142.741492104] [object_detection]: Pointcloud callback.
[INFO] [1702984142.757420709] [object_detection]: Callback Took: 0.0015941s
[INFO] [1702984142.840161117] [object_detection]: Pointcloud callback.
[INFO] [1702984142.857614144] [object_detection]: Callback Took: 0.0017465s
[INFO] [1702984142.941068049] [object_detection]: Pointcloud callback.
[INFO] [1702984142.959526510] [object_detection]: Callback Took: 0.0018473s
[INFO] [1702984143.043983475] [object_detection]: Pointcloud callback.
[INFO] [1702984143.059905025] [object_detection]: Callback Took: 0.0015933s
[INFO] [1702984143.144589532] [object_detection]: Pointcloud callback.
[INFO] [1702984143.161132878] [object_detection]: Callback Took: 0.0016548s
[INFO] [1702984143.245621969] [object_detection]: Pointcloud callback.
[INFO] [1702984143.264049490] [object_detection]: Callback Took: 0.0018445s
[INFO] [1702984143.343289040] [object_detection]: Pointcloud callback.
[INFO] [1702984143.360445452] [object_detection]: Callback Took: 0.0017171s
[INFO] [1702984143.447756475] [object_detection]: Pointcloud callback.
[INFO] [1702984143.470462257] [object_detection]: Callback Took: 0.0022706s
[INFO] [1702984143.546135228] [object_detection]: Pointcloud callback.
[INFO] [1702984143.565531725] [object_detection]: Callback Took: 0.0019417s
[INFO] [1702984143.646730948] [object_detection]: Pointcloud callback.
[INFO] [1702984143.663461190] [object_detection]: Callback Took: 0.0016741s
[INFO] [1702984143.752757867] [object_detection]: Pointcloud callback.
[INFO] [1702984143.772525920] [object_detection]: Callback Took: 0.0019777s
[INFO] [1702984143.853882774] [object_detection]: Pointcloud callback.
[INFO] [1702984143.875859763] [object_detection]: Callback Took: 0.0021991s
[INFO] [1702984143.948968865] [object_detection]: Pointcloud callback.
[INFO] [1702984143.967530970] [object_detection]: Callback Took: 0.0018574s
[INFO] [1702984144.056496531] [object_detection]: Pointcloud callback.
[INFO] [1702984144.075295746] [object_detection]: Callback Took: 0.0018814s
[INFO] [1702984144.160564614] [object_detection]: Pointcloud callback.
[INFO] [1702984144.175517887] [object_detection]: Callback Took: 0.0014974s
[INFO] [1702984144.250670681] [object_detection]: Pointcloud callback.
[INFO] [1702984144.268890145] [object_detection]: Callback Took: 0.0018228s
[INFO] [1702984144.355661296] [object_detection]: Pointcloud callback.
[INFO] [1702984144.370192937] [object_detection]: Callback Took: 0.0014545s
[INFO] [1702984144.448332489] [object_detection]: Pointcloud callback.
[INFO] [1702984144.465848024] [object_detection]: Callback Took: 0.0017527s
[INFO] [1702984144.554205687] [object_detection]: Pointcloud callback.
[INFO] [1702984144.571427401] [object_detection]: Callback Took: 0.0017233s
[INFO] [1702984144.652390141] [object_detection]: Pointcloud callback.
[INFO] [1702984144.669248052] [object_detection]: Callback Took: 0.0016867s
[INFO] [1702984144.756549088] [object_detection]: Pointcloud callback.
[INFO] [1702984144.773636218] [object_detection]: Callback Took: 0.0017098s
[INFO] [1702984144.857164644] [object_detection]: Pointcloud callback.
[INFO] [1702984144.873937139] [object_detection]: Callback Took: 0.0016786s
[INFO] [1702984144.956326874] [object_detection]: Pointcloud callback.
[INFO] [1702984144.980529072] [object_detection]: Callback Took: 0.0024214s
[INFO] [1702984145.056121796] [object_detection]: Pointcloud callback.
[INFO] [1702984145.079286015] [object_detection]: Callback Took: 0.0023177s
[INFO] [1702984145.155214814] [object_detection]: Pointcloud callback.
[INFO] [1702984145.172554908] [object_detection]: Callback Took: 0.0017352s
[INFO] [1702984145.262500130] [object_detection]: Pointcloud callback.
[INFO] [1702984145.278466589] [object_detection]: Callback Took: 0.001598s
[INFO] [1702984145.358920327] [object_detection]: Pointcloud callback.
[INFO] [1702984145.376068707] [object_detection]: Callback Took: 0.001716s
[INFO] [1702984145.465063112] [object_detection]: Pointcloud callback.
[INFO] [1702984145.481119386] [object_detection]: Callback Took: 0.0016069s
[INFO] [1702984145.564868510] [object_detection]: Pointcloud callback.
[INFO] [1702984145.583476501] [object_detection]: Callback Took: 0.0018622s
[INFO] [1702984145.668066861] [object_detection]: Pointcloud callback.
[INFO] [1702984145.690395151] [object_detection]: Callback Took: 0.0022341s
[INFO] [1702984145.767538418] [object_detection]: Pointcloud callback.
[INFO] [1702984145.785989336] [object_detection]: Callback Took: 0.0018464s
[INFO] [1702984145.869760181] [object_detection]: Pointcloud callback.
[INFO] [1702984145.887460516] [object_detection]: Callback Took: 0.0017712s
[INFO] [1702984145.967699842] [object_detection]: Pointcloud callback.
[INFO] [1702984145.987056320] [object_detection]: Callback Took: 0.0019369s
[INFO] [1702984146.066634390] [object_detection]: Pointcloud callback.
[INFO] [1702984146.084694966] [object_detection]: Callback Took: 0.0018072s
[INFO] [1702984146.168117931] [object_detection]: Pointcloud callback.
[INFO] [1702984146.185381130] [object_detection]: Callback Took: 0.0017274s
[INFO] [1702984146.269920227] [object_detection]: Pointcloud callback.
[INFO] [1702984146.290422241] [object_detection]: Callback Took: 0.0020513s
[INFO] [1702984146.371582283] [object_detection]: Pointcloud callback.
[INFO] [1702984146.393609417] [object_detection]: Callback Took: 0.0022037s
"""

# Przetwarzanie danych
timestamps = []
durations = []

for line in log_data.split('\n'):
    if 'Callback Took' in line:
        timestamp = float(re.search(r'\[([\d.]+)\]', line).group(1))
        duration = float(re.search(r'Callback Took: ([\d.]+)s', line).group(1))
        timestamps.append(timestamp - 1702984137.807152395)
        durations.append(duration)

# Rysowanie wykresu
plt.plot(timestamps, durations, marker='o')
plt.title('Czas trwania callbacku w zależności od callbacku')
plt.xlabel('Timestamp')
plt.ylabel('Czas trwania (s)')
plt.grid(True)
plt.show()