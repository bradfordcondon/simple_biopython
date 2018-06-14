Currently a learning repo for me to rewrite existing libraries I have into python.

* `Strip_seqs.py`
  - removes sequences from FASTA, leaving just headers
* `split_fasta.py`
  - splits an input FASTA file into n output FASTA files  
* `coords_to_gff.py`
  - a simple gff generator that takes tab-delimited coords file from nucmer as input.

  
  

## coords to gff

example input (note: query reference might get switched once i figure out the input data i'm given.):
```buildoutcfg
jcf7180001222274	Apr 27 2017	955572	NUCMER	/rho-pool1/rhodata1/WalnutComp/Walnut/Genomes/black_walnut.fasta	C10001	922595	922490	1	106	100.000000	100.000000	106	0	0	NULL	0	Minus	106	0	0


```

desired output:

```
jcf7180001222195	maker	gene	15712	17481	.	-	.	ID=WALNUT_00009338;Name=WALNUT_00009338;Alias=PREDICTED: transcription factor bHLH91-like,Interpro:IPR011598,Pfam:PF00010;Note=high_quality_complete_model;
jcf7180001222195	maker	mRNA	15712	17481	.	-	.	ID=Juglans_regia_01182017_WALNUT_00009338-RA_mRNA;Parent=WALNUT_00009338;Name=Juglans_regia_01182017_WALNUT_00009338-RA_mRNA;Alias=PREDICTED: transcription factor bHLH91-like,Interpro:IPR011598,Pfam:PF00010;Note=high_quality_complete_model;

```