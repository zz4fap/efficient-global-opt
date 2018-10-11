import h5py
import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
import pandas as pd

lower = 0
upper = 25

TINIDX = 0
SNDIDX = 7

def fixPAruntime():
    """Set WP index and runtime for timeout jobs (note: leads to lower mean)"""
    wp = h5py.File('../data/wp-small.h5')

    pa = np.copy(hdf['afsnd_PA']['raw_results']).squeeze()
    TO = '14,15,16,17,18,28,29,30,43,84,85,86,112,113,133,134,148,252,253,254,266,267,268,364,365,392,393,394,395,396,397,398,469,470,471,483,484,485,498,525,526,527,528,540,569,588,589,609,610,616,617,644,645,646,647,686,687,688,707,708,709,749,750,784,785,786,787,798,799,800,801,802,833,834,840,841,842,843,844,855,861,862,863,896,897,898,899,903,904,910,911,912,913,973,974,975,980,981,982,987,988,989,994,995,998,1008,1009,1029,1036,1037,1038,1057,1059,1065,1078,1079,1080,1085,1086,1087,1183,1184,1185,1246,1274,1276,1323,1324,1337,1338,1339,1379,1380,1381,1428,1429,1430,1435,1436,1484,1485,1486,1505,1506,1507,1508,1519,1520,1533,1534,1535,1536,1540,1541,1542,1543,1544,1545,1546,1547,1582,1583,1584,1589,1590,1591,1592,1610,1611,1624,1625,1626,1631,1632,1633,1634,1635,1636,1645,1646,1647,1648,1649,1757,1758,1759,1792,1793,1794,1806,1807,1808,1809,1841,1843,1844,1845,1846,1904,1905,1946,1947,1948,1953,1954,1967,1968,1969,1970,1988,1989,1990,2023,2024,2025,2026,2027,2028,2029,2030,2031,2044,2045,2046,2065,2066,2067,2108,2115,2135,2137,2163,2164,2165,2170,2171,2172,2173,2174,2175,2176,2198,2205,2206,2207,2208,2219,2220,2226,2227,2228,2229,2230,2233,2234,2297,2298,2299,2338,2339,2366,2367,2380,2381,2382,2383,2384,2385,2386,2423,2429,2430,2527,2528,2529,2530,2576,2577,2578,2579,2580,2619,2625,2626,2627,2639,2667,2668,2669,2670,2702,2703,2709,2710,2751,2752,2753,2772,2773,2774,2775,2776,2777,2778,2779,2780,2781,2782,2814,2815,2828,2842,2843,2857,2891,2892,2912,2913,2914,2915,2919,2920,3074,3075,3108,3109,3110,3111,3115,3116,3117,3118,3129,3130,3131,3157,3158,3159,3160,3161,3162,3163,3185,3186,3187,3199,3200,3213,3214,3215,3227,3228,3241,3242,3243,3262,3263,3264,3292,3305,3311,3312,3313,3314,3341,3360,3361,3381,3430,3451,3452,3453,3486,3487,3488,3501,3502,3503,3507,3508,3521,3522,3523,3549,3550,3551,3552,3553,3554,3564,3570,3571,3572,3573,3574,3592,3598,3599,3647,3648,3649,3668,3669,3670,3671,3675,3724,3725,3726,3738,3739,3740,3741,3742,3823,3843,3844,3998,3999,4000,4001,4002,4004,4005,4006,4007,4008,4081,4082,4083,4130,4158,4159,4160,4186,4187,4188,4189,4193,4194,4223,4235,4236,4263,4264,4265,4326,4327,4410,4411,4412,4413,4438,4439,4440,4459,4460,4461,4473,4474,4529,4530,4571,4572,4573,4574,4578,4579,4613,4614,4620,4621,4622,4623,4624,4627,4628,4629,4630,4631,4632,4678,4732,4733,4803,4810,4816,4817,4867,4868,4869,4943,4944,4945,4946,4947,4948,4963,4964,4991,4992,4993,5068,5069,5117,5118,5119,5180,5181,5182,5194,5195,5196,5197,5236,5306,5376,5502,5503,5504,5505,5530,5531,5537,5538,5539,5551,5552,5553,5902,6104,6105,6106,6107,6293,6294,6295,6441,6468,6510,6511,6512,6659,6660,6888,6889,6890,6986,1842,2531,2640,3073,3858,3864,3865,3866,3885,3886,3899,3900,3901,3948,3949,3950,3951,3969,3970,3971,3997,4382,4383,4384,4385,5238,5239,5240,5243,5244,5245,5246,5292,5293,5294,5308,5309,5460,5461,5477,5506,5607,5608,5609,5635,5636,5637,5671,5712,5713,5714,5726,5727,5728,5852,5853,5854,5901,5903,5929,5936,5938,5943,5944,5945,5950,5951,6027,6028,6035,6069,6070,6071,6072,6073,6074,6132,6133,6146,6147,6174,6175,6176,6177,6178,6195,6196,6237,6307,6308,6309,6328,6329,6330,6335,6336,6342,6343,6344,6349,6350,6351,6357,6384,6385,6386,6426,6427,6428,6440,6454,6470,6471,6472,6524,6525,6581,6601,6602,6603,6604,6605,6606,6629,6657,6692,6693,6694,6706,6707,6734,6735,6736,6737,6763,6811,6812,6819,6846,6860,6861,6862,6874,6875,6876,6877,6916,6917,6918,6919,6920,6944,6945,6946,6959,6965,6966,6972,6973,6979,6980,6981,6982'
    TO2 = '1277,1842,4824,5238,5239,5240,5241,5242,5243,5244,5245,5246,5279,5292,5293,5294,5295,5308,5309,5310,5311,5341,5342,5343,5355,5356,5357,5358,5390,5391,5404,5406,5432,5434,5446,5447,5460,5461,5462,5474,5475,5476,5477,5481,5482,5483,5506,5507,5516,5523,5524,5525,5572,5573,5574,5575,5586,5587,5588,5589,5607,5608,5609,5610,5635,5636,5637,5638,5649,5652,5663,5664,5665,5670,5671,5672,5698,5705,5706,5707,5712,5713,5714,5715,5716,5720,5726,5727,5728,5740,5742,5782,5783,5784,5810,5811,5817,5818,5819,5831,5832,5833,5834,5845,5846,5847,5852,5853,5854,5855,5859,5860,5861,5862,5882,5901,5903,5904,5922,5923,5924,5929,5930,5936,5937,5938,5939,5943,5944,5945,5946,5950,5951,5952,5985,5986,6000,6013,6014,6015,6020,6027,6028,6029,6030,6034,6035,6036,6057,6069,6070,6071,6072,6073,6074,6075,6083,6084,6085,6091,6125,6126,6127,6132,6133,6134,6135,6146,6147,6148,6174,6175,6176,6177,6178,6179,6180,6189,6195,6196,6197,6225,6237,6238,6258,6259,6296,6307,6308,6309,6310,6328,6329,6330,6335,6336,6337,6338,6342,6343,6344,6345,6349,6350,6351,6352,6356,6357,6358,6377,6378,6384,6385,6386,6387,6405,6406,6412,6413,6414,6426,6427,6428,6429,6440,6454,6455,6470,6471,6472,6473,6474,6475,6476,6489,6490,6517,6518,6524,6525,6526,6532,6547,6559,6560,6561,6580,6581,6582,6587,6588,6589,6590,6594,6601,6602,6603,6604,6605,6606,6607,6615,6616,6617,6618,6619,6629,6630,6636,6637,6650,6651,6653,6657,6658,6678,6692,6693,6694,6695,6699,6700,6706,6707,6708,6709,6710,6713,6714,6734,6735,6736,6737,6738,6739,6741,6743,6756,6762,6763,6764,6805,6811,6812,6813,6818,6819,6820,6846,6847,6860,6861,6862,6863,6868,6874,6875,6876,6877,6878,6879,6916,6917,6918,6919,6920,6921,6922,6923,6925,6926,6930,6931,6937,6938,6939,6944,6945,6946,6947,6959,6960,6965,6966,6967,6972,6973,6974,6979,6980,6981,6982,6983,6986,6987'
    TO3 = '14,15,16,17,18,19,28,29,30,31,42,43,44,57,63,64,65,77,79,80,84,85,86,87,100,112,113,114,115,133,134,135,147,148,149,162,168,169,170,183,189,190,218,252,253,254,255,266,267,268,269,275,294,295,308,311,352,364,365,366,372,392,393,394,395,396,397,398,399,400,401,402,413,414,415,420,422,428,443,449,455,456,457,458,469,470,471,472,483,484,485,486,490,491,492,493,497,498,499,519,520,525,526,527,528,529,539,540,541,567,568,569,570,581,582,583,588,589,590,591,609,610,611,616,617,618,630,632,644,645,646,647,648,652,653,666,669,672,673,674,679,680,681,686,687,688,689,690,691,693,694,707,708,709,710,721,722,723,735,736,737,749,750,751,756,758,784,785,786,787,788,798,799,800,801,802,803,813,814,819,821,833,834,835,836,840,841,842,843,844,845,846,854,855,856,861,862,863,864,875,876,877,884,889,890,891,896,897,898,899,900,901,903,904,905,906,910,911,912,913,914,918,939,953,959,960,973,974,975,976,980,981,982,983,987,988,989,990,994,995,996,998,1002,1008,1009,1010,1015,1016,1017,1022,1023,1024,1029,1030,1036,1037,1038,1039,1043,1044,1045,1050,1051,1052,1053,1057,1058,1059,1064,1065,1066,1071,1072,1073,1078,1079,1080,1081,1082,1085,1086,1087,1088,1100,1101,1113,1114,1115,1116,1129,1135,1155,1156,1170,1171,1177,1183,1184,1185,1186,1220,1225,1226,1227,1232,1233,1234,1246,1247,1248,1254,1274,1275,1276,1281,1282,1283,1288,1289,1290,1302,1303,1304,1323,1324,1325,1330,1331,1332,1337,1338,1339,1340,1374,1379,1380,1381,1382,1393,1394,1395,1396,1421,1422,1428,1429,1430,1431,1435,1436,1437,1450,1477,1478,1480,1484,1485,1486,1487,1492,1493,1499,1505,1506,1507,1508,1509,1519,1520,1521,1533,1534,1535,1536,1537,1540,1541,1542,1543,1544,1545,1546,1547,1548,1569,1582,1583,1584,1585,1586,1589,1590,1591,1592,1593,1603,1610,1611,1612,1613,1617,1618,1619,1624,1625,1626,1627,1631,1632,1633,1634,1635,1636,1637,1645,1646,1647,1648,1649,1650,1674,1694,1696,1701,1702,1744,1750,1751,1752,1757,1758,1759,1760,1785,1786,1787,1792,1793,1794,1806,1807,1808,1809,1810,1827,1828,1829,1836,1841,1843,1844,1845,1846,1847,1876,1877,1879,1898,1900,1901,1904,1905,1906,1919,1920,1932,1933,1934,1941,1946,1947,1948,1949,1953,1954,1955,1962,1967,1968,1969,1970,1971,1974,1975,1976,1982,1988,1989,1990,1991,2023,2024,2025,2026,2027,2028,2029,2030,2031,2032,2038,2044,2045,2046,2047,2052,2058,2059,2060,2065,2066,2067,2068,2088,2093,2094,2095,2096,2103,2107,2108,2109,2114,2115,2116,2135,2136,2137,2138,2144,2163,2164,2165,2166,2170,2171,2172,2173,2174,2175,2176,2178,2179,2198,2199,2205,2206,2207,2208,2209,2212,2213,2214,2219,2220,2221,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2240,2242,2254,2263,2268,2269,2270,2275,2276,2296,2297,2298,2299,2300,2331,2332,2333,2338,2339,2340,2353,2366,2367,2368,2375,2380,2381,2382,2383,2384,2385,2386,2389,2416,2422,2423,2424,2429,2430,2431,2436,2437,2438,2450,2453,2478,2479,2480,2485,2488,2492,2493,2494,2495,2520,2527,2528,2529,2530,2531,2532,2533,2569,2570,2576,2577,2578,2579,2580,2581,2582,2618,2619,2620,2625,2626,2627,2628,2639,2640,2641,2653,2654,2655,2667,2668,2669,2670,2671,2682,2683,2688,2689,2690,2695,2696,2702,2703,2704,2705,2709,2710,2711,2718,2725,2731,2732,2744,2745,2747,2751,2752,2753,2754,2772,2773,2774,2775,2776,2777,2778,2779,2780,2781,2782,2783,2784,2795,2801,2814,2815,2816,2817,2828,2829,2842,2843,2844,2856,2857,2858,2859,2877,2878,2879,2886,2891,2892,2893,2912,2913,2914,2915,2916,2917,2919,2920,2921,2926,2927,2941,2947,2948,2954,2955,2956,2982,2983,2984,2989,2991,3003,3004,3005,3017,3020,3033,3047,3073,3074,3075,3076,3089,3101,3102,3108,3109,3110,3111,3112,3115,3116,3117,3118,3119,3120,3129,3130,3131,3132,3157,3158,3159,3160,3161,3162,3163,3173,3178,3179,3180,3185,3186,3187,3188,3199,3200,3201,3213,3214,3215,3216,3227,3228,3229,3241,3242,3243,3244,3248,3249,3250,3262,3263,3264,3265,3290,3291,3292,3293,3304,3305,3306,3307,3311,3312,3313,3314,3315,3339,3340,3341,3342,3353,3354,3355,3360,3361,3362,3367,3368,3369,3370,3381,3382,3402,3404,3430,3431,3451,3452,3453,3454,3458,3459,3460,3466,3474,3486,3487,3488,3489,3493,3494,3495,3500,3501,3502,3503,3504,3507,3508,3509,3521,3522,3523,3524,3544,3549,3550,3551,3552,3553,3554,3555,3556,3557,3558,3563,3564,3565,3570,3571,3572,3573,3574,3575,3591,3592,3593,3598,3599,3600,3601,3621,3626,3627,3628,3641,3642,3647,3648,3649,3650,3654,3655,3657,3668,3669,3670,3671,3672,3673,3675,3676,3703,3705,3706,3718,3719,3720,3724,3725,3726,3727,3731,3732,3733,3738,3739,3740,3741,3742,3743,3753,3754,3780,3781,3789,3808,3809,3822,3823,3824,3836,3837,3838,3843,3844,3845,3846,3851,3857,3858,3859,3864,3865,3866,3867,3885,3886,3887,3899,3900,3901,3902,3948,3949,3950,3951,3952,3953,3954,3969,3970,3971,3972,3990,3991,3992,3997,3998,3999,4000,4001,4002,4003,4004,4005,4006,4007,4008,4009,4010,4081,4082,4083,4084,4103,4109,4110,4111,4118,4130,4131,4144,4145,4146,4151,4152,4153,4154,4158,4159,4160,4161,4165,4166,4167,4172,4174,4175,4182,4186,4187,4188,4189,4190,4193,4194,4195,4196,4221,4222,4223,4235,4236,4237,4238,4263,4264,4265,4266,4270,4271,4284,4285,4286,4287,4305,4306,4320,4326,4327,4328,4335,4377,4382,4383,4384,4385,4386,4398,4410,4411,4412,4413,4414,4425,4426,4438,4439,4440,4441,4445,4446,4447,4454,4459,4460,4461,4462,4466,4467,4468,4473,4474,4475,4481,4487,4502,4503,4529,4530,4531,4538,4539,4543,4544,4545,4571,4572,4573,4574,4575,4578,4579,4580,4581,4592,4593,4613,4614,4615,4620,4621,4622,4623,4624,4625,4626,4627,4628,4629,4630,4631,4632,4633,4635,4676,4677,4678,4690,4693,4697,4698,4727,4732,4733,4734,4739,4740,4754,4802,4803,4804,4809,4810,4811,4816,4817,4818,4819,4823,4867,4868,4869,4870,4871,4922,4935,4936,4943,4944,4945,4946,4947,4948,4963,4964,4965,4991,4992,4993,4994,5019,5020,5021,5026,5027,5028,5029,5068,5069,5070,5076,5082,5083,5084,5117,5118,5119,5120,5166,5168,5175,5180,5181,5182,5183,5187,5188,5189,5194,5195,5196,5197,5198,5199,5200,5229,5230,5236,5237,5252,5264,5265,5266,5271,5273,5306,5307,5334,5335,5376,5377,5468,5502,5503,5504,5505,5530,5531,5532,5537,5538,5539,5540,5546,5551,5552,5553,5700,5701,5729,5775,5776,5777,5902,6104,6105,6106,6107,6108,6109,6286,6287,6288,6293,6294,6295,6441,6442,6443,6468,6469,6491,6496,6497,6498,6510,6511,6512,6513,6659,6660,6661,6880,6881,6883,6888,6889,6890,6891,6902,6958'

    TO = np.array(TO.split(','),dtype=int) 
    TO2 = np.array(TO2.split(','),dtype=int) 
    TO3 = np.array(TO3.split(','),dtype=int) 

    for a,b in zip(*np.where(np.isnan(pa['Runtime']))):
        idx = np.where(wp['WP'][:]==np.asarray((a,b),dtype=wp['WP'][0].dtype))[0][0]
        pa[a,b]['WP index'] = idx

        if idx in TO:
            pa[a,b]['Runtime'] = 7*24*3600
        elif idx in TO2 or idx in TO3:
            pa[a,b]['Runtime'] = 24*3600

    wp.close()

    return pa['Runtime']

try:
    h5py.enable_ipython_completer()
except RuntimeError:
    pass

def extractRange(P, l, u):
    return (np.where(np.asarray(P)==l)[0][0], np.where(np.asarray(P)==u)[0][0]+1)

hdf = h5py.File('results.h5')
spawc = sio.loadmat('../../MWRC_SND_RA/src/DC/results/spawc.mat')

# HK
hk1_P = spawc['PdB'].flatten()
sr1 = extractRange(hk1_P, lower, upper)
hk1_P = hk1_P[sr1[0]:sr1[1]]
hk1 = spawc['optval'][:,sr1[0]:sr1[1]]

hk2_P = hdf['hk']['input']['P']
sr2 = extractRange(hk2_P, lower, upper)
hk2_P = hk2_P[sr2[0]:sr2[1]]
hk2 = hdf['hk']['raw_results']['Objective Value'][:,sr2[0]:sr2[1]].squeeze() * np.log2(np.e)

hk_P = hk2_P
hk = np.copy(hk2)
hk[np.isnan(hk2)] = hk1[np.isnan(hk2)]

# fix bad drops 
hk[np.where(hk[:,1:]-hk[:,:-1]<0)[0], -1] = np.nan

hkexclude = ~np.any(np.isnan(hk),axis=1)
hkmean = pd.DataFrame({'HK': np.mean(hk[hkexclude,:],axis=0)}, index=hk_P)

# PA AFSND
pa_P = hdf['afsnd_PA']['input']['P']
sr3 = extractRange(pa_P, lower, upper)
pa_P = pa_P[sr3[0]:sr3[1]]
pa = hdf['afsnd_PA']['raw_results']['Objective Value'][:,sr3[0]:sr3[1]].squeeze() * np.log2(np.e)

paexclude = ~np.any(np.isnan(pa),axis=1)
pamean = pd.DataFrame({'PA': np.mean(pa[np.logical_and(hkexclude, paexclude),:], axis=0)}, index=pa_P)

part = fixPAruntime()

paruntime = pd.DataFrame({
        'PA_mean': np.nanmean(part, axis=0),
        'PA_median': np.nanmedian(part, axis=0),
        'PA_NaNs': np.sum(np.isnan(hdf['afsnd_PA']['raw_results']['Runtime'].squeeze()), axis=0), # these are the 'raw' NaNs, i.e., the uncorrected values
}, index=hdf['afsnd_PA']['input']['P'][:])

del part

# pa exclude for all plots
#hkexclude = np.logical_and(hkexclude, paexclude)
#hkmean = np.mean(hk[hkexclude,:],axis=0)

# AFSND
afsnd_P = hdf['afsnd']['input']['P']
sr0 = extractRange(afsnd_P, lower, upper)
afsnd_P = afsnd_P[sr0[0]:sr0[1]]
afsnd = hdf['afsnd']['joint_results']['Objective Value'][:,sr0[0]:sr0[1]].squeeze() * np.log2(np.e)

afjoint = hdf['afsnd']['raw_results']['Objective Value'][:,sr0[0]:sr0[1],SNDIDX].squeeze() * np.log2(np.e)
aftin = hdf['afsnd']['raw_results']['Objective Value'][:,sr0[0]:sr0[1],TINIDX].squeeze() * np.log2(np.e)

afsndmean = pd.DataFrame(
        {
            'SND': np.mean(afsnd[hkexclude,:], axis=0),
            'Joint': np.mean(afjoint[hkexclude,:], axis=0),
            'TIN': np.mean(aftin[hkexclude,:], axis=0),
        }, index=afsnd_P)

afsndruntime = pd.DataFrame(
        {
            'SND_NaNs': np.sum(np.isnan(hdf['afsnd']['joint_results']['Runtime']), axis=0),
            'SND_mean': np.nanmean(hdf['afsnd']['joint_results']['Runtime'], axis=0),
            'SND_median': np.nanmedian(hdf['afsnd']['joint_results']['Runtime'], axis=0),
            'Joint_NaNs': np.sum(np.isnan(hdf['afsnd']['raw_results']['Runtime'][:,:,TINIDX]), axis=0),
            'Joint_mean': np.nanmean(hdf['afsnd']['raw_results']['Runtime'][:,:,TINIDX], axis=0),
            'Joint_median': np.nanmedian(hdf['afsnd']['raw_results']['Runtime'][:,:,TINIDX], axis=0),
            'TIN_NaNs': np.sum(np.isnan(hdf['afsnd']['raw_results']['Runtime'][:,:,TINIDX]), axis=0),
            'TIN_mean': np.nanmean(hdf['afsnd']['raw_results']['Runtime'][:,:,TINIDX], axis=0),
            'TIN_median': np.nanmedian(hdf['afsnd']['raw_results']['Runtime'][:,:,TINIDX], axis=0),
            }, index = hdf['afsnd']['input']['P'][:])

objval = pd.concat([afsndmean,hkmean,pamean],axis=1)
runtime = pd.concat([afsndruntime, paruntime],axis=1)


avg_gain = pd.concat(((
        pd.concat([objval['SND']/objval['TIN'], objval['SND']/objval['Joint'], pd.DataFrame(np.nanmean(hk / afsnd, axis=0), index = afsnd_P)], axis=1, keys=['SND vs TIN [%]', 'SND vs Joint [%]', 'HK vs SND [%]'])-1)*100,
        pd.concat([objval['SND']-objval['TIN'], objval['SND']-objval['Joint'], pd.DataFrame(np.nanmean(hk - afsnd, axis=0), index = afsnd_P)], axis=1, keys=['SND vs TIN [bpcu]', 'SND vs Joint [bpcu]', 'HK vs SND [bpcu]'])
    ), axis=1)

max_gain = pd.DataFrame({'HK vs SND [%]': np.nanmax(hk / afsnd, axis=0)*100-100, 'HK vs SND [bpcu]': np.nanmax(hk - afsnd, axis=0)}, index = afsnd_P)


objval.to_csv('sumrate.dat', index_label='snr')
runtime.to_csv('sumrate_runtime.dat', index_label='snr')