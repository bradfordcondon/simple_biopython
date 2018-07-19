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

## generate_biomaterials

A simple script that generates fake biomaterials XML.  There are 5 properties for each biomaterial: one is a constant type with one of two values (ensuring there are properties to compare).  One's value is a number.

Usage:

` python generate_biomaterials.py [number of biomaterials to create]`

example output (formatted for legibility):

```xml
<BioSampleSet>
	<BioSample accession="let" id="billion" submission_date="1987-01-21">
		<IDs db="BioSample" is_primary="1">let</IDs>
		<Description>Individual democratic military far investment feeling.</Description>
		<Owner>
			<Name>Andrew Lowery</Name>
			<Address>15300 Kimberly Cove
New Aimeeberg, WY 70035</Address>
		</Owner>
		<Attributes>
			<Attribute attribute_name="system" display_name="system" harmonized_name="system">short</Attribute>
			<Attribute attribute_name="day" display_name="day" harmonized_name="day">dream</Attribute>
			<Attribute attribute_name="conference" display_name="conference" harmonized_name="conference">north</Attribute>
			<Attribute attribute_name="movie" display_name="movie" harmonized_name="movie">despite</Attribute>
			<Attribute attribute_name="information" display_name="information" harmonized_name="information">forget</Attribute>
			<Attribute attribute_name="relationship">24</Attribute>
		</Attributes>
	</BioSample>
	</BioSampleSet>
```

## generate_expression

Usage:

`python generate_expression.py [biomaterials xml] [fasta file]`

Creates a tab delimited expression dataset (with random values between 1 and 1000).


## minify_dataset

`python minify_dataset.py [number of mRNA to use] [mrna FASTA file] [GFF file]`

Given n, a FASTA file, & a GFF file, trim the FASTA file down to n.  
Then, remove all items from the GFF not containing the mRNA.
Next, run `trim_polypeptide` to trim the polypeptide FASTA down to the mRNA 
(it is a seperate command because a REGEXP is required to link the two.)

## trim polypeptide.py

This script trims one fasta file against another given a regexp.  In our use case, we match the protein sequences against the mRNA, given a Regexp.
The regexp should search the protein name and give the corresponding mRNA name.

   `python trim_polypeptide.py [trimmed mrna FASTA] [polypeptide FASTA] [regexp]`

```shell
python staton_biopy/trim_polypeptide.py mrna_mini.fasta input_data/FexcelsiorAA.minoas.fasta '(FRA.*?)(?=:)'
```