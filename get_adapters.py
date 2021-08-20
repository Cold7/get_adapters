########################################################################
##
##	Python script to remove Adapters found in fastq files using FastQC
##
########################################################################

from glob import glob

if __name__ == "__main__":
	htmlFiles = glob("*.html")
	for htmlFile in htmlFiles:
		f = open(htmlFile,"r")
		for line in f:
			if "Overrepresented sequences" in line:
				try:
					
					sequences = line.split("Overrepresented sequences</h2><table><thead><tr><th>Sequence</th><th>Count</th><th>Percentage</th><th>Possible Source</th></tr></thead><tbody>")[1].split("</tbody></table><")[0].split("<tr>")
					print(">"+htmlFile.replace(".html",""))
					for seq in sequences:
						sequence = seq.split("</td>")[0].replace("<td>","")
						if sequence != "":
							print(sequence)
				except:
					pass
		f.close()
