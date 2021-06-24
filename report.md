# Problem report

We seem to have a problem that some courses are sometimes missing
from a response.
Tests shows that sometimes some courses are duplicated, but the total
number of courses included the duplicates stays the same, so when some
courses are duplicated, others are missing.

Is this a bug that could and should be fixed in cavas, or is there
something we might do wrong that causes the problem?

Some test code for this: https://github.com/KTH/test-canvas-usercourses

There never seeems to be duplicates _inside_ a page.  Instead, there
is often an overlap so that a sub-sequence of courses is repated in
another page (often pages close to the end of one page is repated at
the beginning of the next page, but variations occur).

An example of a run with duplicates follows.  Page 4 starts with
"16620, 20563, 26763" from the middle of page 3, then comes "16748,
20260, 26767, 2643, 6447, 8381, 30102, 3603, 6448, 16626, 20612,
26612, 8358, 19191" from the end of page 3, and then some courses
unique to page 4.

Other runs for the same user sometimes give 198 distinct courses, and
sometimes a slightly different set of overlaps and sometimes the exact
same set of overlaps. (Maybe there is a round robin among a few
servers, and when I get the same server again the results are cached?
Or maybe whatever is causing this gives few possible results).
Running the test 20 times for the same user I got four different sets
of results.

```
Checking courses for u1t0l5al (Johnny Öberg)
Page 1: [1586, 1, 24691, 25579, 19871, 31986, 24788, 32089, 30249, 31978, 24731, 25578, 19875, 19901, 30373, 31979, 24951, 19872, 31987, 24354, 32115, 19879, 31992, 25434, 170, 171, 24781, 30187, 31988, 19874, 24789, 19880, 19904, 31982, 19870, 31977, 25563, 19881, 31993, 173, 172, 5191, 1585, 32145, 32144, 8356, 5733, 24914, 25435, 19884]
Page 2: [19885, 22156, 31989, 19877, 28693, 32083, 16634, 20230, 26753, 6423, 6425, 16631, 20229, 26756, 6424, 16628, 22946, 6426, 16637, 20231, 26760, 4941, 11190, 4940, 18110, 4946, 18118, 8781, 19274, 24794, 4947, 7680, 17205, 17208, 21501, 21497, 31587, 31167, 8782, 19735, 25421, 26377, 26393, 21511, 4908, 7681, 17211, 22309, 31588, 4910]
Page 3: [18112, 8681, 19219, 4948, 11183, 20664, 30246, 8804, 19972, 4914, 11185, 20667, 8783, 19220, 25561, 4950, 11186, 17218, 9091, 19453, 4911, 18172, 2434, 6445, 16620, 20563, 26763, 8784, 19382, 25067, 4917, 7692, 17261, 22476, 21531, 31171, 16748, 20260, 26767, 2643, 6447, 8381, 30102, 3603, 6448, 16626, 20612, 26612, 8358, 19191]
Page 4: [16620, 20563, 26763, 16748, 20260, 26767, 2643, 6447, 8381, 30102, 3603, 6448, 16626, 20612, 26612, 8358, 19191, 22349, 1964, 4931, 19749, 29035, 4518, 23771, 1750, 5696, 7701, 17283, 21541, 31598, 4924, 11151, 19526, 4925, 11184, 20666, 12192, 8989, 17839, 25898, 25895, 30770, 24622, 25326, 25324, 29507, 184, 18339]
DUPLICATES page 4 vs 3: {20612, 20260, 8358, 26763, 16748, 16620, 19191, 26767, 6447, 6448, 16626, 3603, 20563, 2643, 30102, 26612, 8381}
Got 198 courses
... but only 181 distinct
```
