#Variables
material1 = raw_input('What block to you want to use?: ')
#first part of command
cmdnpt1 = ('/execute @a ~ ~ ~ detect ~ ~.2 ~-.4 ')
cmdspt1 = ('/execute @a ~ ~ ~ detect ~ ~.2 ~.4 ')
cmdept1 = ('/execute @a ~ ~ ~ detect ~-.4 ~.2 ~ ')
cmdwpt1 = ('/execute @a ~ ~ ~ detect ~.4 ~.2 ~ ')
#second poart of command
cmdpt2 = (' tp @p ~ ~.5 ~')

output = open("Output.txt", "w")
output.write(cmdnpt1 + material1 + cmdpt2)
output.write('\n')
output.write('\n')
output.write(cmdspt1 + material1 + cmdpt2)
output.write('\n')
output.write('\n')
output.write(cmdept1 + material1 + cmdpt2)
output.write('\n')
output.write('\n')
output.write(cmdwpt1 + material1 + cmdpt2)
output.close()
