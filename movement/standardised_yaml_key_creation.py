
import yaml
import zipfile

zip_file = zipfile.ZipFile("D:/exporty12.zip")
files = zip_file.namelist()
lenfiles = len(files)


keylist = []
for i in range(lenfiles):
    with zip_file.open(files[i]) as yamlfile:
        #print(yamlfile)
        yamlreader = yaml.safe_load(yamlfile)
        sortedkeys = sorted(yamlreader.keys())
        keylist.append(sortedkeys)

print(len(keylist))

b_set = set(map(tuple,keylist))  #need to convert the inner lists to tuples so they are hashable
uniquekeylist = list(map(list,b_set))

#print(b_set)
print(uniquekeylist)
#print(len(b_set))

def longest(list1):
    longest_list = max(len(elem) for elem in list1)
    return longest_list

longestlist = longest(uniquekeylist)

for i in uniquekeylist:
    if len(i)==longestlist:
        longlist = i

extras = []
for i in uniquekeylist:
    new_list = list(set(i).difference(longlist))
    extras.extend(new_list)

uniqueextras = list(set(extras))
longlist.extend(uniqueextras)

print(longlist) #standardised list for yaml keys

#standardised_list = ['allele', 'arena', 'base_name', 'chromosome', 'food', 'frames per second', 'gene', 'habituation', 'identifier', 'lab', 'media', 'number of segmented skeletons', 'preview link', 'protocol', 'sex', 'software', 'stage', 'strain', 'strain_description', 'timestamp', 'total time (s)', 'ventral_side', 'video micrometers per pixel', 'who', 'worm_id', 'days_of_adulthood']

