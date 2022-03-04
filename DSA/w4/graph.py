import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox
import numpy as np

# setting the x - coordinates
x = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 6100, 6200, 6300, 6400, 6500, 6600, 6700, 6800, 6900, 7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000, 8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900, 9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900, 10000, 10100, 10200, 10300, 10400, 10500, 10600, 10700, 10800, 10900, 11000, 11100, 11200, 11300, 11400, 11500, 11600, 11700, 11800, 11900, 12000, 12100, 12200, 12300, 12400, 12500, 12600, 12700, 12800, 12900, 13000, 13100, 13200, 13300, 13400, 13500, 13600, 13700, 13800, 13900, 14000, 14100, 14200, 14300, 14400, 14500, 14600, 14700, 14800, 14900, 15000, 15100, 15200, 15300, 15400, 15500, 15600, 15700, 15800, 15900, 16000, 16100, 16200, 16300, 16400, 16500, 16600, 16700, 16800, 16900, 17000, 17100, 17200, 17300, 17400, 17500, 17600, 17700, 17800, 17900, 18000, 18100, 18200, 18300, 18400, 18500, 18600, 18700, 18800, 18900, 19000, 19100, 19200, 19300, 19400, 19500, 19600, 19700, 19800, 19900, 20000, 20100, 20200, 20300, 20400, 20500, 20600, 20700, 20800, 20900, 21000, 21100, 21200, 21300, 21400, 21500, 21600, 21700, 21800, 21900, 22000, 22100, 22200, 22300, 22400, 22500, 22600, 22700, 22800, 22900, 23000, 23100, 23200, 23300, 23400, 23500, 23600, 23700, 23800, 23900, 24000, 24100, 24200, 24300, 24400, 24500, 24600, 24700, 24800, 24900, 25000, 25100, 25200, 25300, 25400, 25500, 25600, 25700, 25800, 25900, 26000, 26100, 26200, 26300, 26400, 26500, 26600, 26700, 26800, 26900, 27000, 27100, 27200, 27300, 27400, 27500, 27600, 27700, 27800, 27900, 28000, 28100, 28200, 28300, 28400, 28500, 28600, 28700, 28800, 28900, 29000, 29100, 29200, 29300, 29400, 29500, 29600, 29700, 29800, 29900, 30000, 30100, 30200, 30300, 30400, 30500, 30600, 30700, 30800, 30900, 31000, 31100, 31200, 31300, 31400, 31500, 31600, 31700, 31800, 31900, 32000, 32100, 32200, 32300, 32400, 32500, 32600, 32700, 32800, 32900, 33000, 33100, 33200, 33300, 33400, 33500, 33600, 33700, 33800, 33900, 34000, 34100, 34200, 34300, 34400, 34500, 34600, 34700, 34800, 34900, 35000, 35100, 35200, 35300, 35400, 35500, 35600, 35700, 35800, 35900, 36000, 36100, 36200, 36300, 36400, 36500, 36600, 36700, 36800, 36900, 37000, 37100, 37200, 37300, 37400, 37500, 37600, 37700, 37800, 37900, 38000, 38100, 38200, 38300, 38400, 38500, 38600, 38700, 38800, 38900, 39000, 39100, 39200, 39300, 39400, 39500, 39600, 39700, 39800, 39900, 40000, 40100, 40200, 40300, 40400, 40500, 40600, 40700, 40800, 40900, 41000, 41100, 41200, 41300, 41400, 41500, 41600, 41700, 41800, 41900, 42000, 42100, 42200, 42300, 42400, 42500, 42600, 42700, 42800, 42900, 43000, 43100, 43200, 43300, 43400, 43500, 43600, 43700, 43800, 43900, 44000, 44100, 44200, 44300, 44400, 44500, 44600, 44700, 44800, 44900, 45000, 45100, 45200, 45300, 45400, 45500, 45600, 45700, 45800, 45900, 46000, 46100, 46200, 46300, 46400, 46500, 46600, 46700, 46800, 46900, 47000, 47100, 47200, 47300, 47400, 47500, 47600, 47700, 47800, 47900, 48000, 48100, 48200, 48300, 48400, 48500, 48600, 48700, 48800, 48900, 49000, 49100, 49200, 49300, 49400, 49500, 49600, 49700, 49800, 49900, 50000, 50100, 50200, 50300, 50400, 50500, 50600, 50700, 50800, 50900, 51000, 51100, 51200, 51300, 51400, 51500, 51600, 51700, 51800, 51900, 52000, 52100, 52200, 52300, 52400, 52500, 52600, 52700, 52800, 52900, 53000, 53100, 53200, 53300, 53400, 53500, 53600, 53700, 53800, 53900, 54000, 54100, 54200, 54300, 54400, 54500, 54600, 54700, 54800, 54900, 55000, 55100, 55200, 55300, 55400, 55500, 55600, 55700, 55800, 55900, 56000, 56100, 56200, 56300, 56400, 56500, 56600, 56700, 56800, 56900, 57000, 57100, 57200, 57300, 57400, 57500, 57600, 57700, 57800, 57900, 58000, 58100, 58200, 58300, 58400, 58500, 58600, 58700, 58800, 58900, 59000, 59100, 59200, 59300, 59400, 59500, 59600, 59700, 59800, 59900, 60000, 60100, 60200, 60300, 60400, 60500, 60600, 60700, 60800, 60900, 61000, 61100, 61200, 61300, 61400, 61500, 61600, 61700, 61800, 61900, 62000, 62100, 62200, 62300, 62400, 62500, 62600, 62700, 62800, 62900, 63000, 63100, 63200, 63300, 63400, 63500, 63600, 63700, 63800, 63900, 64000, 64100, 64200, 64300, 64400, 64500, 64600, 64700, 64800, 64900, 65000, 65100, 65200, 65300, 65400, 65500, 65600, 65700, 65800, 65900, 66000, 66100, 66200, 66300, 66400, 66500, 66600, 66700, 66800, 66900, 67000, 67100, 67200, 67300, 67400, 67500, 67600, 67700, 67800, 67900, 68000, 68100, 68200, 68300, 68400, 68500, 68600, 68700, 68800, 68900, 69000, 69100, 69200, 69300, 69400, 69500, 69600, 69700, 69800, 69900, 70000, 70100, 70200, 70300, 70400, 70500, 70600, 70700, 70800, 70900, 71000, 71100, 71200, 71300, 71400, 71500, 71600, 71700, 71800, 71900, 72000, 72100, 72200, 72300, 72400, 72500, 72600, 72700, 72800, 72900, 73000, 73100, 73200, 73300, 73400, 73500, 73600, 73700, 73800, 73900, 74000, 74100, 74200, 74300, 74400, 74500, 74600, 74700, 74800, 74900, 75000, 75100, 75200, 75300, 75400, 75500, 75600, 75700, 75800, 75900, 76000, 76100, 76200, 76300, 76400, 76500, 76600, 76700, 76800, 76900, 77000, 77100, 77200, 77300, 77400, 77500, 77600, 77700, 77800, 77900, 78000, 78100, 78200, 78300, 78400, 78500, 78600, 78700, 78800, 78900, 79000, 79100, 79200, 79300, 79400, 79500, 79600, 79700, 79800, 79900, 80000, 80100, 80200, 80300, 80400, 80500, 80600, 80700, 80800, 80900, 81000, 81100, 81200, 81300, 81400, 81500, 81600, 81700, 81800, 81900, 82000, 82100, 82200, 82300, 82400, 82500, 82600, 82700, 82800, 82900, 83000, 83100, 83200, 83300, 83400, 83500, 83600, 83700, 83800, 83900, 84000, 84100, 84200, 84300, 84400, 84500, 84600, 84700, 84800, 84900, 85000, 85100, 85200, 85300, 85400, 85500, 85600, 85700, 85800, 85900, 86000, 86100, 86200, 86300, 86400, 86500, 86600, 86700, 86800, 86900, 87000, 87100, 87200, 87300, 87400, 87500, 87600, 87700, 87800, 87900, 88000, 88100, 88200, 88300, 88400, 88500, 88600, 88700, 88800, 88900, 89000, 89100, 89200, 89300, 89400, 89500, 89600, 89700, 89800, 89900, 90000, 90100, 90200, 90300, 90400, 90500, 90600, 90700, 90800, 90900, 91000, 91100, 91200, 91300, 91400, 91500, 91600, 91700, 91800, 91900, 92000, 92100, 92200, 92300, 92400, 92500, 92600, 92700, 92800, 92900, 93000, 93100, 93200, 93300, 93400, 93500, 93600, 93700, 93800, 93900, 94000, 94100, 94200, 94300, 94400, 94500, 94600, 94700, 94800, 94900, 95000, 95100, 95200, 95300, 95400, 95500, 95600, 95700, 95800, 95900, 96000, 96100, 96200, 96300, 96400, 96500, 96600, 96700, 96800, 96900, 97000, 97100, 97200, 97300, 97400, 97500, 97600, 97700, 97800, 97900, 98000, 98100, 98200, 98300, 98400, 98500, 98600, 98700, 98800, 98900, 99000, 99100, 99200, 99300, 99400, 99500, 99600, 99700, 99800, 99900, 100000])
# setting the corresponding y - coordinates
y1 = np.array([0.000019,0.000044,0.000070,0.000102,0.000124,0.000163,0.000195,0.000232,0.000274,0.000178,0.000189,0.000215,0.000243,0.000255,0.000278,0.000345,0.000360,0.000392,0.000369,0.000401,0.000431,0.000439,0.000462,0.000513,0.000524,0.000563,0.000567,0.000595,0.000605,0.000642,0.000711,0.000740,0.000699,0.000721,0.000777,0.000830,0.000805,0.000862,0.000834,0.000913,0.001139,0.000954,0.000953,0.000994,0.001024,0.001069,0.001082,0.001156,0.001118,0.001209,0.001185,0.001250,0.001233,0.001271,0.001305,0.001352,0.001361,0.001361,0.001428,0.001441,0.001485,0.001612,0.001522,0.001731,0.001544,0.001612,0.001598,0.001645,0.001685,0.001670,0.001687,0.001895,0.001834,0.001837,0.001808,0.001924,0.001959,0.001923,0.001926,0.002061,0.002052,0.002518,0.002129,0.002134,0.002125,0.002154,0.002176,0.002262,0.002250,0.002277,0.002368,0.002406,0.002363,0.002417,0.002436,0.002593,0.002520,0.002569,0.002608,0.002654,0.002570,0.002703,0.002909,0.002834,0.002906,0.002802,0.002783,0.002881,0.002793,0.002904,0.002900,0.003031,0.003090,0.003035,0.003085,0.003124,0.003084,0.003233,0.003157,0.003288,0.003320,0.003295,0.004570,0.003584,0.003444,0.003379,0.003426,0.003957,0.003421,0.003504,0.003508,0.003651,0.003623,0.003584,0.003651,0.003691,0.003752,0.003679,0.003771,0.003961,0.003849,0.003846,0.003915,0.004281,0.003999,0.004107,0.004008,0.004103,0.004031,0.004001,0.004129,0.004272,0.004224,0.004494,0.004287,0.004292,0.004350,0.004391,0.004457,0.004675,0.004488,0.004596,0.004512,0.005855,0.005002,0.004843,0.004741,0.004886,0.005276,0.004708,0.004789,0.005006,0.004915,0.005106,0.005029,0.005086,0.004954,0.005077,0.005088,0.005030,0.005049,0.005372,0.005244,0.005399,0.005461,0.006673,0.006186,0.008159,0.008018,0.006120,0.005726,0.007141,0.009546,0.006111,0.005937,0.005721,0.005735,0.006536,0.007105,0.006300,0.006093,0.005969,0.007948,0.006302,0.007359,0.006585,0.006290,0.006502,0.006375,0.006929,0.006312,0.006486,0.007183,0.006545,0.006465,0.007877,0.007139,0.009399,0.007405,0.006588,0.007317,0.006630,0.006555,0.007112,0.006804,0.006940,0.007102,0.007105,0.007586,0.007121,0.011954,0.009248,0.007486,0.007109,0.007019,0.007337,0.007069,0.007157,0.007839,0.007340,0.008207,0.007441,0.007561,0.007466,0.009331,0.010250,0.016297,0.008810,0.007857,0.008393,0.009862,0.007639,0.007717,0.007654,0.007681,0.009847,0.007713,0.013319,0.015891,0.007741,0.008781,0.007791,0.007862,0.008218,0.008115,0.008255,0.008452,0.009405,0.008977,0.010181,0.009420,0.009824,0.009566,0.010967,0.020705,0.013631,0.010728,0.010030,0.009796,0.010046,0.009843,0.012385,0.013512,0.009743,0.009089,0.009674,0.012635,0.012586,0.011954,0.009975,0.009260,0.010487,0.010987,0.010029,0.009065,0.009263,0.011233,0.010202,0.010266,0.010564,0.009869,0.009236,0.011241,0.009967,0.009799,0.010003,0.011541,0.010201,0.009937,0.010019,0.010010,0.020398,0.010958,0.010809,0.017085,0.016064,0.010317,0.010996,0.011412,0.013615,0.010069,0.010581,0.009998,0.010126,0.010410,0.010240,0.010631,0.015291,0.012187,0.015540,0.011071,0.011136,0.012217,0.010529,0.010439,0.010990,0.010701,0.011558,0.010642,0.011400,0.011821,0.011287,0.011351,0.011275,0.011376,0.014239,0.011192,0.012117,0.011832,0.011752,0.011773,0.012273,0.011202,0.012271,0.013759,0.011268,0.011229,0.011449,0.011435,0.017866,0.012311,0.012837,0.014247,0.013956,0.021275,0.013410,0.011698,0.015613,0.014705,0.012353,0.012603,0.012109,0.011894,0.012105,0.012258,0.012101,0.013872,0.015149,0.014410,0.012407,0.012860,0.015350,0.014578,0.017549,0.012559,0.024660,0.013615,0.013117,0.013219,0.013248,0.016539,0.012827,0.013005,0.013923,0.015847,0.013474,0.014125,0.013139,0.013109,0.013524,0.012854,0.013131,0.014807,0.016357,0.013424,0.013647,0.013397,0.013390,0.013582,0.016829,0.014676,0.020955,0.020530,0.013919,0.013632,0.014534,0.013531,0.013886,0.013916,0.015295,0.014124,0.013861,0.013317,0.014243,0.014666,0.013885,0.013667,0.014319,0.014956,0.015051,0.013957,0.017184,0.014315,0.014935,0.016690,0.018193,0.014975,0.014719,0.016588,0.015463,0.016131,0.014402,0.014527,0.017360,0.021725,0.015423,0.014730,0.016110,0.014904,0.015331,0.016300,0.015612,0.015405,0.018920,0.015090,0.015208,0.015235,0.015198,0.015347,0.027838,0.019650,0.017604,0.018411,0.017896,0.015456,0.016046,0.015320,0.016901,0.016032,0.016008,0.015891,0.016628,0.015839,0.015677,0.016112,0.018661,0.016233,0.016025,0.017956,0.020881,0.016426,0.017502,0.016045,0.017020,0.016141,0.020771,0.016248,0.017542,0.017320,0.017009,0.020916,0.022354,0.018199,0.018116,0.017379,0.017891,0.017174,0.030176,0.018151,0.016999,0.017219,0.017501,0.016745,0.018253,0.018830,0.020645,0.017441,0.017031,0.019997,0.018731,0.017990,0.028302,0.026456,0.021607,0.021793,0.027226,0.018481,0.017250,0.017347,0.017747,0.018807,0.021593,0.017984,0.018638,0.019984,0.022753,0.018008,0.017902,0.017522,0.019275,0.023283,0.017953,0.023750,0.018524,0.025455,0.018169,0.020931,0.022430,0.017663,0.017854,0.017667,0.019335,0.018679,0.021252,0.020694,0.017966,0.018621,0.019165,0.017961,0.021837,0.020169,0.019741,0.023638,0.019191,0.020120,0.021260,0.018611,0.021534,0.018739,0.019140,0.018750,0.021441,0.020362,0.020300,0.024103,0.019790,0.019131,0.019955,0.023359,0.022607,0.020158,0.020024,0.019435,0.022928,0.020888,0.024735,0.023660,0.020393,0.021305,0.020384,0.020191,0.020381,0.020598,0.020319,0.020088,0.023509,0.019825,0.019897,0.026858,0.020171,0.021668,0.020749,0.020357,0.023918,0.022747,0.021247,0.019775,0.020101,0.024557,0.024919,0.023361,0.020693,0.020390,0.021202,0.023940,0.021576,0.022710,0.026269,0.021831,0.021488,0.021102,0.022197,0.021975,0.023080,0.023616,0.021851,0.022768,0.021599,0.026501,0.025628,0.021316,0.022993,0.021087,0.023718,0.023691,0.021879,0.027399,0.030057,0.023835,0.021498,0.022330,0.022383,0.022030,0.022660,0.024758,0.022132,0.022435,0.023363,0.022530,0.024956,0.022548,0.022043,0.027011,0.024398,0.022429,0.025637,0.022628,0.022762,0.023027,0.023803,0.024092,0.022892,0.023173,0.028991,0.027006,0.031548,0.029072,0.024730,0.024644,0.029869,0.027453,0.028248,0.023674,0.032705,0.032186,0.026272,0.025198,0.028304,0.023434,0.023227,0.031183,0.028272,0.030232,0.024205,0.023804,0.026658,0.025830,0.023714,0.024300,0.024129,0.026398,0.025135,0.024403,0.030502,0.025377,0.024543,0.035926,0.032554,0.023872,0.027627,0.024527,0.028558,0.027741,0.024474,0.028842,0.025458,0.029416,0.030778,0.031218,0.024280,0.028187,0.025470,0.027499,0.028411,0.024487,0.029165,0.025162,0.029396,0.026917,0.022340,0.021694,0.029034,0.025225,0.023013,0.019724,0.020802,0.025510,0.026145,0.026006,0.017354,0.026605,0.017663,0.016507,0.021744,0.020520,0.016789,0.017786,0.017647,0.018441,0.018903,0.019530,0.016899,0.020584,0.021137,0.023861,0.022965,0.026796,0.035605,0.030991,0.034346,0.028565,0.026513,0.028082,0.026516,0.028510,0.028938,0.026794,0.029278,0.032378,0.034664,0.026732,0.027340,0.029304,0.029919,0.027464,0.027594,0.042004,0.028612,0.030464,0.029635,0.027575,0.028897,0.032301,0.028456,0.035467,0.027442,0.026909,0.045370,0.031150,0.032078,0.026842,0.027894,0.034054,0.042927,0.033639,0.031715,0.028412,0.027889,0.034459,0.035105,0.028693,0.028651,0.034716,0.032825,0.027689,0.035719,0.043919,0.028448,0.035638,0.033741,0.035271,0.028758,0.040766,0.029918,0.028289,0.035346,0.028923,0.030527,0.040079,0.032526,0.028858,0.035084,0.031124,0.029189,0.028120,0.029277,0.045812,0.031842,0.032489,0.029490,0.036463,0.030537,0.037538,0.036994,0.030603,0.044502,0.031795,0.033829,0.037755,0.035841,0.037713,0.037619,0.032885,0.031813,0.042180,0.034945,0.033165,0.030618,0.031979,0.032729,0.030092,0.033145,0.030118,0.030323,0.030984,0.038153,0.036325,0.031017,0.038479,0.040945,0.030698,0.033906,0.030974,0.033868,0.031383,0.030766,0.030210,0.043347,0.039586,0.041520,0.040494,0.037105,0.038652,0.033647,0.037151,0.031935,0.033773,0.031904,0.036705,0.044182,0.044186,0.037891,0.037920,0.036827,0.039396,0.035942,0.031077,0.040398,0.033283,0.038170,0.031246,0.039648,0.033385,0.031210,0.034625,0.036667,0.032425,0.033414,0.031718,0.039755,0.040755,0.032287,0.032134,0.036597,0.041181,0.033978,0.033576,0.037355,0.036810,0.037440,0.039253,0.033733,0.033137,0.042431,0.036217,0.042238,0.043031,0.038093,0.043733,0.034044,0.038549,0.043083,0.040115,0.034479,0.034255,0.044720,0.032888,0.033098,0.039105,0.034800,0.040700,0.038677,0.033173,0.039013,0.033537,0.039910,0.044162,0.035681,0.035134,0.042623,0.040645,0.039582,0.036301,0.041186,0.033090,0.037939,0.042225,0.042373,0.039310,0.039963,0.033881,0.029978,0.028642,0.028656,0.037006,0.044744,0.041152,0.035555,0.038312,0.034554,0.035172,0.039535,0.043227,0.050668,0.044377,0.036374,0.036189,0.045193,0.034149,0.046648,0.041293,0.041388,0.040314,0.035054,0.037816,0.040114,0.035868,0.047734,0.048149,0.048425,0.035622,0.035833,0.044237,0.041212,0.046165,0.048729,0.039511,0.037998,0.043522,0.035911,0.038721,0.036744,0.038150,0.037570,0.036845,0.044744,0.040136,0.037657,0.045457,0.038425,0.037353,0.037246,0.038018,0.066280,0.055088,0.046202,0.051385,0.040607,0.038745,0.048398,0.038752,0.041857,0.038332,0.036948,0.041782,0.050636,0.036586,0.046691,0.041439,0.037345,])
y2= np.array([0.000001,0.000002,0.000003,0.000008,0.000029,0.000033,0.000037,0.000041,0.000044,0.000010,0.000011,0.000032,0.000033,0.000035,0.000037,0.000045,0.000048,0.000057,0.000051,0.000054,0.000056,0.000063,0.000065,0.000067,0.000070,0.000072,0.000075,0.000071,0.000074,0.000076,0.000079,0.000086,0.000088,0.000090,0.000092,0.000141,0.000102,0.000100,0.000101,0.000049,0.000049,0.000103,0.000100,0.000102,0.000103,0.000105,0.000106,0.000109,0.000110,0.000161,0.000163,0.000165,0.000168,0.000169,0.000172,0.000174,0.000024,0.000026,0.000026,0.000028,0.000028,0.000029,0.000029,0.000030,0.000031,0.000032,0.000032,0.000033,0.000034,0.000034,0.000035,0.000036,0.000037,0.000038,0.000040,0.000041,0.000049,0.000039,0.000041,0.000041,0.000042,0.000044,0.000043,0.000043,0.000044,0.000045,0.000045,0.000047,0.000049,0.000049,0.000049,0.000048,0.000048,0.000048,0.000054,0.000053,0.000051,0.000051,0.000051,0.000052,0.000052,0.000053,0.000054,0.000054,0.000054,0.000056,0.000056,0.000056,0.000057,0.000056,0.000058,0.000058,0.000058,0.000059,0.000061,0.000060,0.000060,0.000060,0.000062,0.000062,0.000063,0.000063,0.000063,0.000064,0.000066,0.000066,0.000065,0.000066,0.000070,0.000067,0.000068,0.000069,0.000070,0.000075,0.000072,0.000070,0.000071,0.000071,0.000071,0.000084,0.000073,0.000073,0.000074,0.000075,0.000076,0.000076,0.000078,0.000076,0.000077,0.000077,0.000077,0.000077,0.000079,0.000079,0.000080,0.000081,0.000080,0.000081,0.000081,0.000085,0.000083,0.000083,0.000084,0.000092,0.000086,0.000085,0.000087,0.000090,0.000088,0.000088,0.000090,0.000089,0.000088,0.000088,0.000091,0.000089,0.000092,0.000092,0.000093,0.000093,0.000092,0.000099,0.000098,0.000096,0.000095,0.000143,0.000146,0.000148,0.000110,0.000175,0.000115,0.000111,0.000114,0.000105,0.000134,0.000102,0.000102,0.000129,0.000177,0.000108,0.000129,0.000106,0.000159,0.000147,0.000109,0.000109,0.000110,0.000110,0.000111,0.000115,0.000116,0.000113,0.000114,0.000163,0.000129,0.000119,0.000169,0.000116,0.000121,0.000120,0.000118,0.000117,0.000117,0.000120,0.000117,0.000158,0.000123,0.000120,0.000121,0.000123,0.000151,0.000123,0.000127,0.000124,0.000133,0.000124,0.000128,0.000159,0.000144,0.000128,0.000127,0.000126,0.000141,0.000128,0.000130,0.000136,0.000211,0.000130,0.000213,0.000182,0.000135,0.000135,0.000132,0.000132,0.000135,0.000136,0.000137,0.000384,0.000561,0.000139,0.000182,0.000142,0.000138,0.000139,0.000193,0.000144,0.000149,0.000143,0.000149,0.000193,0.000184,0.000215,0.000185,0.000149,0.000311,0.000221,0.000283,0.000151,0.000183,0.000150,0.000154,0.000213,0.000226,0.000225,0.000153,0.000190,0.000167,0.000152,0.000536,0.000161,0.000151,0.000181,0.000160,0.000156,0.000164,0.000166,0.000160,0.000205,0.000165,0.000170,0.000268,0.000159,0.000229,0.000167,0.000196,0.000165,0.000238,0.000162,0.000162,0.000174,0.000181,0.000348,0.000168,0.000184,0.000241,0.000166,0.000168,0.000169,0.000171,0.000172,0.000166,0.000238,0.000171,0.000171,0.000177,0.000175,0.000172,0.000177,0.000181,0.000447,0.000174,0.000178,0.000234,0.000178,0.000178,0.000181,0.000175,0.000176,0.000192,0.000456,0.000185,0.000200,0.000192,0.000196,0.000238,0.000268,0.000181,0.000263,0.000185,0.000198,0.000186,0.000190,0.000187,0.000187,0.000186,0.000188,0.000184,0.000190,0.000188,0.000311,0.000213,0.000246,0.000191,0.000211,0.000191,0.000190,0.000192,0.000194,0.000200,0.000206,0.000206,0.000198,0.000195,0.000195,0.000207,0.000196,0.000197,0.000321,0.000207,0.000200,0.000336,0.000201,0.000201,0.000202,0.000201,0.000204,0.000203,0.000203,0.000207,0.000237,0.000299,0.000207,0.000205,0.000230,0.000208,0.000321,0.000225,0.000208,0.000220,0.000218,0.000205,0.000206,0.000215,0.000226,0.000213,0.000211,0.000211,0.000210,0.000209,0.000223,0.000212,0.000407,0.000346,0.000214,0.000213,0.000216,0.000214,0.000219,0.000219,0.000220,0.000226,0.000219,0.000217,0.000216,0.000219,0.000219,0.000223,0.000221,0.000223,0.000226,0.000224,0.000222,0.000221,0.000255,0.000230,0.000226,0.000227,0.000231,0.000234,0.000244,0.000392,0.000231,0.000230,0.000229,0.000359,0.000235,0.000235,0.000235,0.000234,0.000236,0.000235,0.000232,0.000236,0.000317,0.000233,0.000239,0.000247,0.000390,0.000257,0.000246,0.000249,0.000242,0.000246,0.000244,0.000257,0.000242,0.000242,0.000267,0.000258,0.000247,0.000292,0.000253,0.000251,0.000249,0.000247,0.000275,0.000253,0.000245,0.000253,0.000253,0.000440,0.000258,0.000250,0.000255,0.000253,0.000358,0.000253,0.000255,0.000253,0.000420,0.000262,0.000255,0.000255,0.000261,0.000259,0.000258,0.000262,0.000571,0.000264,0.000382,0.000390,0.000261,0.000259,0.000275,0.000530,0.000264,0.000261,0.000263,0.000326,0.000263,0.000268,0.000266,0.000429,0.000264,0.000271,0.000269,0.000275,0.000270,0.000267,0.000270,0.000281,0.000272,0.000271,0.000276,0.000277,0.000437,0.000296,0.000275,0.000276,0.000274,0.000287,0.000277,0.000279,0.000280,0.000476,0.000284,0.000280,0.000286,0.000279,0.000287,0.000282,0.000299,0.000288,0.000279,0.000380,0.000286,0.000286,0.000285,0.000289,0.000317,0.000285,0.000284,0.000295,0.000286,0.000298,0.000390,0.000300,0.000298,0.000289,0.000289,0.000290,0.000296,0.000423,0.000295,0.000308,0.000297,0.000295,0.000296,0.000298,0.000301,0.000302,0.000300,0.000296,0.000294,0.000298,0.000302,0.000409,0.000301,0.000307,0.000304,0.000307,0.000377,0.000304,0.000303,0.000305,0.000447,0.000308,0.000307,0.000434,0.000340,0.000430,0.000306,0.000306,0.000308,0.000314,0.000324,0.000310,0.000312,0.000311,0.000325,0.000342,0.000315,0.000326,0.000316,0.000320,0.000351,0.000324,0.000325,0.000323,0.000320,0.000319,0.000319,0.000320,0.000323,0.000318,0.000319,0.000322,0.000327,0.000329,0.000931,0.000325,0.000325,0.000341,0.000328,0.000324,0.000364,0.000326,0.000331,0.000334,0.000324,0.000327,0.000493,0.000330,0.000331,0.000327,0.000334,0.000334,0.000337,0.000358,0.000330,0.000334,0.000335,0.000333,0.000505,0.000348,0.000340,0.000338,0.000337,0.000339,0.000383,0.000337,0.000339,0.000335,0.000337,0.000342,0.000342,0.000481,0.000352,0.000344,0.000342,0.000346,0.000347,0.000344,0.000341,0.000507,0.000354,0.000375,0.000348,0.000344,0.000347,0.000369,0.000356,0.000352,0.000350,0.000351,0.000359,0.000359,0.000353,0.000356,0.000351,0.000356,0.000354,0.000356,0.000358,0.000355,0.000552,0.000583,0.000362,0.000365,0.000510,0.000358,0.000362,0.000356,0.000364,0.000364,0.000380,0.000406,0.000363,0.000370,0.000364,0.000525,0.000363,0.000374,0.000366,0.000364,0.000376,0.000365,0.000538,0.000346,0.000335,0.000323,0.000315,0.000408,0.000298,0.000290,0.000283,0.000270,0.000450,0.000326,0.000254,0.000257,0.000242,0.000244,0.000242,0.000248,0.000246,0.000255,0.000257,0.000751,0.000253,0.000249,0.000249,0.000248,0.000255,0.000253,0.000333,0.000382,0.000379,0.000387,0.000416,0.000401,0.000386,0.000398,0.000384,0.000394,0.000393,0.000387,0.000389,0.000548,0.000473,0.000394,0.000387,0.000384,0.000397,0.000418,0.000395,0.000551,0.000397,0.000396,0.000401,0.000400,0.000401,0.000410,0.000400,0.000396,0.000404,0.000400,0.000397,0.000408,0.000399,0.000410,0.000407,0.000409,0.000616,0.000432,0.000412,0.000404,0.000400,0.000407,0.000401,0.000408,0.000414,0.000423,0.000410,0.000403,0.000409,0.000414,0.000413,0.000409,0.000419,0.000468,0.000408,0.000775,0.000420,0.000418,0.000414,0.000409,0.000418,0.000422,0.000417,0.000421,0.000416,0.000416,0.000431,0.000429,0.000434,0.000434,0.000421,0.000494,0.000421,0.000426,0.000427,0.000420,0.000429,0.000428,0.000425,0.000425,0.000427,0.000440,0.000428,0.000426,0.000429,0.000431,0.000426,0.000786,0.000604,0.000439,0.000430,0.000432,0.000476,0.000450,0.000435,0.000435,0.000448,0.000441,0.000440,0.000442,0.000430,0.000443,0.000452,0.000444,0.000447,0.000439,0.000437,0.000444,0.000447,0.000449,0.000687,0.000441,0.000436,0.000442,0.000442,0.000441,0.000451,0.000437,0.000449,0.000617,0.000452,0.000448,0.000453,0.000447,0.000461,0.000462,0.000444,0.000456,0.000445,0.000445,0.000446,0.000452,0.000447,0.000450,0.000670,0.000447,0.000450,0.000464,0.000474,0.000450,0.000458,0.000451,0.000457,0.000455,0.000452,0.000516,0.000782,0.000458,0.000458,0.000464,0.000464,0.000461,0.000466,0.000761,0.000462,0.000460,0.000461,0.000465,0.000462,0.000489,0.000462,0.000464,0.000485,0.000469,0.000469,0.000465,0.000475,0.000510,0.000470,0.000475,0.000472,0.000476,0.000659,0.000474,0.000474,0.000478,0.000585,0.000475,0.000471,0.000477,0.000476,0.000481,0.000483,0.000479,0.000482,0.000486,0.000478,0.000480,0.000691,0.000481,0.000489,0.000474,0.000692,0.000434,0.000422,0.000404,0.000376,0.000545,0.000481,0.000553,0.000484,0.000481,0.000483,0.000487,0.000482,0.000488,0.000500,0.000491,0.000516,0.000528,0.000489,0.000486,0.000489,0.000488,0.000488,0.000487,0.000605,0.000490,0.000489,0.000496,0.000575,0.000499,0.000493,0.000502,0.000498,0.000540,0.000512,0.000491,0.000496,0.000512,0.000507,0.000496,0.000519,0.000503,0.000501,0.000503,0.000511,0.000542,0.000505,0.000502,0.000502,0.000891,0.000505,0.000507,0.000514,0.000552,0.000511,0.000504,0.000955,0.000511,0.000513,0.000504,0.000508,0.000522,0.000511,0.000507,0.000509,0.000515,0.000512,0.000513,0.000517,0.000749,0.000524,])
y3 =np.array([0.000021,0.000039,0.000066,0.000088,0.000110,0.000135,0.000158,0.000177,0.000210,0.000134,0.000151,0.000166,0.000181,0.000198,0.000213,0.000232,0.000246,0.000270,0.000273,0.000284,0.000306,0.000327,0.000342,0.000359,0.000366,0.000382,0.000426,0.000416,0.000427,0.000442,0.000456,0.000473,0.000490,0.000514,0.000562,0.000553,0.000560,0.000571,0.000602,0.000631,0.000615,0.000654,0.000658,0.000681,0.000700,0.000721,0.000733,0.000757,0.000770,0.000830,0.000824,0.000831,0.000850,0.000869,0.000891,0.000899,0.000926,0.000924,0.000937,0.000953,0.000965,0.000984,0.000995,0.001036,0.001037,0.001060,0.001080,0.001102,0.001121,0.001159,0.001170,0.001186,0.001208,0.001210,0.001261,0.001260,0.001278,0.001270,0.001291,0.001297,0.001323,0.001328,0.001353,0.001383,0.001404,0.001434,0.001450,0.001502,0.001540,0.001561,0.001961,0.001584,0.001567,0.001596,0.001644,0.001666,0.001656,0.001690,0.001704,0.001710,0.001722,0.001802,0.002115,0.002116,0.001805,0.001814,0.001865,0.001846,0.001877,0.001899,0.001918,0.001923,0.001951,0.001982,0.002009,0.002006,0.002028,0.002037,0.002035,0.002053,0.002073,0.002084,0.002097,0.002125,0.002171,0.002164,0.002214,0.002247,0.002407,0.002401,0.002366,0.002181,0.002201,0.002398,0.002363,0.002374,0.002423,0.002739,0.002964,0.002374,0.002537,0.002554,0.002548,0.002565,0.002626,0.002583,0.002590,0.002625,0.002637,0.002688,0.002659,0.002670,0.002728,0.002719,0.002756,0.002635,0.002823,0.002752,0.002669,0.002693,0.002729,0.002705,0.002880,0.002946,0.002920,0.002934,0.002993,0.003026,0.003058,0.003010,0.003040,0.003071,0.003064,0.003088,0.003163,0.003133,0.003189,0.003208,0.003305,0.003321,0.003260,0.003349,0.003362,0.003353,0.003386,0.004250,0.005305,0.005101,0.004373,0.004655,0.003764,0.003667,0.004878,0.004796,0.003835,0.003754,0.003847,0.003937,0.003777,0.003858,0.003817,0.003770,0.006670,0.004127,0.003977,0.004412,0.003858,0.003822,0.003894,0.004041,0.003953,0.003921,0.004022,0.005908,0.004136,0.004089,0.006244,0.004605,0.004092,0.004132,0.004327,0.004749,0.004175,0.004213,0.005492,0.004616,0.004506,0.005023,0.004255,0.004677,0.005433,0.004777,0.004825,0.004445,0.004332,0.004385,0.004484,0.004471,0.004767,0.004804,0.004569,0.004510,0.004562,0.004454,0.004673,0.004588,0.004914,0.004552,0.005457,0.005704,0.004720,0.004659,0.004669,0.004684,0.004699,0.004927,0.004914,0.011726,0.011057,0.005960,0.005032,0.004903,0.004886,0.005056,0.004952,0.005776,0.005080,0.005062,0.005494,0.007088,0.005765,0.006642,0.007437,0.005491,0.009714,0.007703,0.006679,0.006843,0.006510,0.005917,0.006738,0.007443,0.007281,0.006559,0.006112,0.006029,0.006033,0.006586,0.007703,0.005596,0.005548,0.006848,0.006816,0.006037,0.006178,0.005775,0.008305,0.005912,0.005919,0.005680,0.006180,0.006836,0.007862,0.006088,0.005775,0.005802,0.007478,0.006067,0.006503,0.006022,0.006173,0.008722,0.006928,0.009782,0.007291,0.006035,0.006027,0.006253,0.006653,0.006751,0.008358,0.007677,0.006118,0.006552,0.006171,0.007362,0.006408,0.007986,0.006312,0.009718,0.007712,0.006607,0.006440,0.006318,0.006358,0.006475,0.006498,0.007063,0.006652,0.006762,0.006754,0.008540,0.007398,0.007563,0.007167,0.007966,0.006912,0.007925,0.007858,0.008206,0.007714,0.006916,0.006853,0.007218,0.007581,0.006847,0.007120,0.007796,0.007294,0.011730,0.007484,0.008744,0.007346,0.008702,0.007513,0.007073,0.007155,0.007188,0.008386,0.007420,0.008339,0.007206,0.007218,0.007569,0.007584,0.007269,0.007389,0.009264,0.008301,0.007883,0.010751,0.008051,0.007668,0.007613,0.007674,0.008891,0.008189,0.007609,0.007915,0.008722,0.007951,0.007473,0.007600,0.009283,0.008559,0.007782,0.007885,0.008060,0.007738,0.007922,0.007971,0.007981,0.008066,0.010816,0.007912,0.007894,0.007813,0.008333,0.007912,0.007910,0.009201,0.013405,0.012570,0.012312,0.007827,0.009030,0.008573,0.008008,0.010555,0.008775,0.008594,0.009465,0.008825,0.008557,0.008231,0.008216,0.008452,0.008572,0.009427,0.008390,0.008375,0.008897,0.007899,0.010547,0.008298,0.008923,0.009998,0.008781,0.008599,0.008747,0.008712,0.008621,0.008789,0.010488,0.010520,0.008776,0.008724,0.008952,0.009021,0.008820,0.008877,0.008825,0.009119,0.008825,0.009493,0.009972,0.009825,0.009414,0.009841,0.009004,0.009449,0.009178,0.009539,0.009390,0.009117,0.008849,0.009124,0.010007,0.009318,0.009046,0.009139,0.010050,0.009143,0.009122,0.009320,0.011164,0.010473,0.010873,0.009355,0.009311,0.009749,0.012766,0.009718,0.010923,0.009747,0.009941,0.009412,0.010118,0.009821,0.010532,0.009758,0.014192,0.009560,0.009483,0.009701,0.009538,0.010051,0.017435,0.009899,0.009872,0.009676,0.009997,0.011150,0.010042,0.013017,0.009716,0.009834,0.009796,0.009810,0.011247,0.011437,0.012402,0.013891,0.010193,0.012546,0.014582,0.011464,0.010118,0.010025,0.010211,0.015632,0.010127,0.011005,0.011264,0.010181,0.018021,0.010274,0.010309,0.010354,0.010994,0.010727,0.010719,0.010765,0.009920,0.010687,0.010524,0.011377,0.011032,0.010457,0.010509,0.010570,0.010937,0.011403,0.010798,0.011679,0.010692,0.011200,0.011071,0.010793,0.012112,0.012764,0.011374,0.012722,0.010611,0.013245,0.012134,0.012196,0.011865,0.011076,0.011015,0.011036,0.011151,0.015222,0.011848,0.011594,0.011215,0.011592,0.011253,0.011553,0.012204,0.011327,0.011608,0.011338,0.011823,0.011435,0.012198,0.011471,0.011886,0.011908,0.011460,0.011702,0.012805,0.013254,0.012027,0.011579,0.011642,0.011070,0.012510,0.013188,0.011686,0.012440,0.011923,0.011631,0.012243,0.013020,0.012576,0.012370,0.011759,0.012884,0.013867,0.012432,0.012273,0.011793,0.011812,0.012411,0.012085,0.015697,0.013082,0.012184,0.012021,0.011977,0.013437,0.012455,0.012550,0.012473,0.012187,0.013962,0.012350,0.013244,0.012387,0.012394,0.012268,0.012501,0.012469,0.015096,0.014999,0.012375,0.012470,0.013427,0.014378,0.012425,0.014933,0.012936,0.012755,0.012952,0.012517,0.013703,0.012685,0.013356,0.012566,0.012469,0.012507,0.012617,0.012950,0.013737,0.012962,0.014408,0.012626,0.013021,0.012797,0.013208,0.012682,0.012698,0.012699,0.013945,0.014991,0.013847,0.012835,0.013936,0.012895,0.014894,0.013200,0.012965,0.014235,0.013442,0.014974,0.014479,0.013901,0.013217,0.013135,0.013933,0.015803,0.014682,0.013332,0.013173,0.013617,0.014093,0.013475,0.018187,0.015241,0.016145,0.013659,0.013588,0.013557,0.013592,0.017640,0.014520,0.015697,0.013637,0.017799,0.014115,0.013989,0.013998,0.015022,0.014312,0.014543,0.014399,0.013928,0.014134,0.013949,0.015867,0.014798,0.015782,0.013994,0.013678,0.014101,0.017228,0.013794,0.013298,0.012876,0.012470,0.015483,0.013085,0.011307,0.012080,0.011206,0.010599,0.020731,0.010023,0.011615,0.009823,0.009982,0.009505,0.010089,0.010297,0.009974,0.011624,0.010833,0.015736,0.009609,0.009665,0.009562,0.009673,0.010487,0.010238,0.010007,0.014893,0.016177,0.016689,0.016310,0.015295,0.015075,0.015226,0.015996,0.016345,0.015382,0.014937,0.023539,0.027070,0.018110,0.015064,0.015208,0.015202,0.015205,0.015459,0.015567,0.016341,0.015532,0.015204,0.018450,0.015526,0.015344,0.015716,0.017029,0.015426,0.015550,0.015380,0.015785,0.015511,0.015750,0.015488,0.016546,0.015594,0.018170,0.016646,0.017078,0.015625,0.015918,0.016095,0.016335,0.016301,0.017431,0.015737,0.015895,0.019261,0.017456,0.029086,0.015804,0.016449,0.016775,0.017004,0.015891,0.031801,0.016667,0.016368,0.015437,0.016472,0.016293,0.017000,0.018457,0.016775,0.017650,0.016862,0.016350,0.016238,0.016191,0.016471,0.019562,0.016751,0.016171,0.020323,0.017839,0.016230,0.016264,0.016911,0.016887,0.016804,0.016542,0.017480,0.016778,0.017196,0.017271,0.016444,0.016382,0.022546,0.017749,0.016530,0.016585,0.016932,0.021606,0.016693,0.016151,0.016804,0.018473,0.017354,0.016819,0.016942,0.017093,0.018713,0.017047,0.017152,0.016931,0.017622,0.017151,0.017192,0.017136,0.016646,0.032317,0.018136,0.017602,0.017180,0.022565,0.018824,0.017318,0.017630,0.018126,0.018980,0.017216,0.017251,0.019342,0.018737,0.017560,0.017396,0.018814,0.017907,0.017567,0.017722,0.018164,0.017578,0.017502,0.017682,0.021959,0.017815,0.017869,0.017694,0.021714,0.018315,0.017762,0.018733,0.018001,0.019670,0.017294,0.018749,0.020054,0.019884,0.018209,0.018522,0.017963,0.020362,0.018358,0.018873,0.017961,0.019152,0.018828,0.018001,0.019856,0.018218,0.019250,0.018148,0.018059,0.019020,0.018670,0.018240,0.018703,0.019971,0.019167,0.018953,0.017835,0.019915,0.019489,0.019454,0.018510,0.018900,0.019798,0.018385,0.018893,0.018669,0.018880,0.020951,0.018607,0.018588,0.019719,0.020170,0.018600,0.018106,0.019494,0.018902,0.019234,0.018712,0.018291,0.019714,0.016127,0.022713,0.015629,0.022258,0.019073,0.029366,0.019037,0.020523,0.018885,0.018674,0.019984,0.019216,0.019781,0.019116,0.019935,0.020037,0.019268,0.019526,0.020830,0.020465,0.019655,0.019234,0.020250,0.019766,0.019715,0.021694,0.019487,0.020225,0.019611,0.019498,0.020846,0.023825,0.020713,0.019274,0.020721,0.020693,0.020572,0.019853,0.020472,0.020858,0.019373,0.019578,0.020230,0.019903,0.020958,0.020556,0.035095,0.027756,0.019705,0.020035,0.020244,0.022617,0.020094,0.019988,0.020933,0.020798,0.020103,0.020091,0.020197,0.020356,0.021025,0.020467,0.019689,0.022038,0.020171,0.021376,0.025379,0.021738,0.021053,])

plt.xlabel('Input Size')
plt.ylabel('Time in seconds')

# plotting the points
plt.plot(x, y1,'r-')
plt.plot(x,y2,'b-')
plt.plot(x,y3,'g-')
# plt.scatter(x, y1)
# plt.scatter(x,y2)
# plt.scatter(x,y3)
plt.legend(["Shell", "Merge", "Insertion"])

plt.title('Time Complexiety :')

# function to show the plot
# plt.text(900,2200,'insert',bbox=dict(facecolor='red'),color="white")
# plt.text(700,300,'delete',bbox=dict(facecolor='blue'),color="white")
# plt.text(1400,300,'search',bbox=dict(facecolor='green'),color="white")
plt.show()