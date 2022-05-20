# find/ string slicing to extract stuff after the colon
# use float func to convert the extracted into float

str = 'X-DSPAM-Confidence:0.8475'

slice = float(str[19:])
print(slice)

