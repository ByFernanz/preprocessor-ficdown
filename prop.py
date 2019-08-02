import fileinput
import sys
import os
import shutil

#Control del preprocesador
stage = 0
properties = {}
preline=0


#banderas
ifformat=0

#macros especiales
scene_header=""
scene_footer=""
action_header=""
action_footer=""

# linea de comando
comando="ficdown"
infile=sys.argv[1].replace('.md','')
outfile=infile

archivo = open(sys.argv[1]+'.prop','w')
for line in fileinput.input(sys.argv[1]):
	if line.startswith('---'):
		stage += 1
	elif stage == 1 and line.startswith('@'):
		[macro, config] = line.split(': ')
		config = config.splitlines()[0]
		#configuracion de ficdown
		if (macro=="@format"):
			comando+=" --format "+config
			ifformat=1
			if(config=="epub"):
				outfile=infile+".epub"
		elif (macro=="@template"):
			comando+=" --template \""+config+"\""
		elif (macro=="@images"):
			comando+=" --images \""+config+"\""
		elif (macro=="@author"):
			comando+=" --author \""+config+"\""
		elif (macro=="@bookid"):
			comando+=" --bookid \""+config+"\""
		elif (macro=="@language"):
			comando+=" --language \""+config+"\""
		elif (macro=="@debug" and config=="1"):
			comando+=" --debug"
		elif (macro=="@scene_header"):
			scene_header="\n"+config+"\n"
		elif (macro=="@scene_footer"):
			scene_footer=config+"\n\n"
		elif (macro=="@action_header"):
			action_header="\n"+config+"\n"
		elif (macro=="@action_footer"):
			action_footer=config+"\n\n"
	elif stage == 1:
		[prop, val] = line.split(': ')
		properties[prop] = val.splitlines()[0]
	elif stage == 2:
		for prop in properties:
			# ocurre si se inicia el documento con una scena o una accion
			line = line.replace(''.join(['__', prop, '__']), properties[prop])
		if(line.startswith('## ') and preline==0):
			preline=1
			line=line+scene_header
		elif(line.startswith('### ') and preline==0):
			preline=2
			line=line+action_header
		elif(line.startswith('## ') and preline==1):
			preline=1
			line=scene_footer+line+scene_header
		elif(line.startswith('### ') and preline==2):
			preline=2
			line=action_footer+line+action_header
		elif(line.startswith('## ') and preline==2):
			preline=1
			line=action_footer+line+scene_header
		elif(line.startswith('### ') and preline==1):
			preline=2
			line=scene_footer+line+action_header
		archivo.write(line)
if(preline==1):
	line="\n"+scene_footer
elif(preline==2):
	line="\n"+action_footer
else:
	line=""
archivo.write(line)
archivo.close()
if os.path.isdir(infile):
	shutil.rmtree(infile)
infile+=".md.prop"
if(ifformat==1):
	comando+=" --in \""+infile+"\" --out \""+outfile+"\""
else:
	comando+=" --format html --in \""+infile+"\" --out \""+outfile+"\""
print(comando)
os.system(comando+"&& rm "+infile)
