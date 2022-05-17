#open up sample names file and read in sample names
with open('samplenames.txt') as f:
    lines = f.readlines()

#open up the template file
f= open("cleanedsamplenames.txt","w+")

#write the platform sample id to the cleanedsamplenames file
for line in lines:
    if "!Platform_sample_id" in line:
        f.write(line.split("= ")[1])
