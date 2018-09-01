# getting out the thread name to be used as file name
# testing on how to deal with the fact that there are thread *replies*
# that have a different URL structure to *original posts*

li = [
    "https://discussions.udacity.com/t/logic-improvisation-needed/191902/2",
    "https://discussions.udacity.com/t/so-you-want-to-post-some-code/33561"
    ]

# with number at the end (=reply)
print(len(li[0].split('/')))  # len = 7
# replies need the 3rd-last item
print(li[0].split('/')[-3])

# without number at the end (=original post)
print(len(li[1].split('/')))  # len = 6
# original posts need the 2nd-last item
print(li[1].split('/')[-2])
